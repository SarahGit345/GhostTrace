"""Temporal data-lineage: who owns which resource, and which worker run belongs to which case.

Three independent sources of ownership, strongest first:

1. **Identity evidence** - an observation of the resource carries an identifier
   (current/historical email, phone, email hash, user_id) held by exactly one user.
2. **Catalog links** - ``LINK_RESOURCE_IDENTITY`` activities assert resource -> person.
3. **Worker-run reconstruction** - the deletion worker processes a batch of
   requests around their shared ``reported_at``. Activities on resources that
   carry no identity (e.g. an already-anonymised analytics profile) are
   attributed to a case by solving a small constraint problem:
     * time window: the run's account submission happens shortly before the
       case's ``reported_at``;
     * the account submission's result must agree with the workflow status the
       case later reported (SUCCESS<->COMPLETE, PARTIAL<->PARTIALLY_COMPLETE,
       FAILED<->NOT_STARTED; CLASSIFY_REQUEST<->no destructive action);
     * identity-linked pairs are fixed first, then elimination;
     * remaining ties use a **timing fingerprint**: every action of one run
       keeps a constant seconds-offset (per system and phase) from that run's
       account submission. The offsets are learned *unsupervised* as the peak of
       the offset histogram over all candidate pairs - no labels, no constants.
   Every inferred link records how it was made so the certificate can show it.
"""
from __future__ import annotations

import datetime as dt
from collections import Counter, defaultdict

from .identity import IdentityResolver

STATUS_OF_RESULT = {"SUCCESS": "COMPLETE", "PARTIAL": "PARTIALLY_COMPLETE", "FAILED": "NOT_STARTED"}
SLOT_WINDOW = (-10, 90)          # minutes before reported_at in which a run submits the account
ACTION_WINDOW = (-360, 90)       # policy actions: up to 90 min before / 6 h after reported_at
MAX_FINGERPRINT_ERR = 2          # seconds
REPORT_WINDOW = (-10, 30)        # an operation report precedes its workflow's status report


def ts(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def minutes_before(later: str, earlier: str) -> float:
    return (ts(later) - ts(earlier)).total_seconds() / 60


def sec_offset(t_action: str, t_slot: str) -> int:
    return round((ts(t_action) - ts(t_slot)).total_seconds()) % 60


def is_operation_report(act) -> bool:
    """'...reported the requested operation as completed. Target resource: X' - a single-operation report."""
    return "Target resource:" in act.get("details", "")


def circ(a: int, b: int) -> int:
    d = (a - b) % 60
    return min(d, 60 - d)


class Lineage:
    def __init__(self, corpus, identities: IdentityResolver, activities: list[dict], requests: list[dict]):
        self.c, self.idr, self.acts = corpus, identities, activities
        self.reqs = {q["case_id"]: q for q in requests}
        self.owner: dict[str, set[str]] = defaultdict(set)        # resource -> user_ids (evidence)
        self.link_conf: dict[tuple[str, str], str] = {}          # (resource, case) -> how linked
        self.case_resources: dict[str, set[str]] = defaultdict(set)
        self.case_slot: dict[str, dict] = {}                     # case -> account-submission activity
        self.case_classified: dict[str, dict] = {}               # case -> CLASSIFY_REQUEST activity
        self.case_user = {}
        for cid, q in self.reqs.items():
            ident = identities.resolve(q["email"])
            self.case_user[cid] = ident.user_id if ident else None
        self.offsets: dict[tuple[str, str], int] = {}
        self.worker = [a for a in activities if a["source_system"] == "deletion_worker"
                       and a["target_system"] != "account_service"]

    # ------------------------------------------------------------------ evidence ownership
    def build_owner_map(self):
        for o in self.c.observations:
            for k in o.keys:
                owners = self.idr.owners(k)
                if len(owners) == 1:
                    self.owner[o.resource_id] |= owners
        for rid, keys in self.c.resource_links.items():
            for k in keys:
                owners = self.idr.owners(k)
                if len(owners) == 1:
                    self.owner[rid] |= owners
        return self

    def _phase(self, cid, act):
        return "pre" if act["event_time"] <= self.reqs[cid]["reported_at"] else "post"

    # ------------------------------------------------------------------ worker runs
    def _slot_cases(self, act):
        out = []
        for cid, q in self.reqs.items():
            m = minutes_before(q["reported_at"], act["event_time"])
            if not (SLOT_WINDOW[0] <= m <= SLOT_WINDOW[1]):
                continue
            if act["event_type"] == "CLASSIFY_REQUEST":
                if q["reported_status"] != "NOT_STARTED":
                    continue
            elif is_operation_report(act):
                pass            # per-operation report: its own result, not the run's overall status
            elif STATUS_OF_RESULT.get(act["reported_result"]) not in (None, q["reported_status"]):
                continue
            out.append(cid)
        return out

    def _action_cases(self, act):
        return [cid for cid in self.case_slot
                if ACTION_WINDOW[0] <= minutes_before(self.reqs[cid]["reported_at"], act["event_time"]) <= ACTION_WINDOW[1]]

    def assign_runs(self):
        slots = [a for a in self.acts if (a["event_type"] == "DELETE_RECORD" and a["target_system"] == "account_service"
                                          and a["source_system"] == "deletion_worker")
                 or a["event_type"] == "CLASSIFY_REQUEST"]
        self._slots = {a["activity_id"]: a for a in slots}
        cand = {a["activity_id"]: set(self._slot_cases(a)) for a in slots}
        assigned: dict[str, str] = {}
        # 1. identity-linked slots
        for aid, cs in cand.items():
            owners = self.owner.get(self._slots[aid]["resource_id"], set())
            hit = [c for c in cs if self.case_user.get(c) in owners]
            if len(hit) == 1:
                assigned[aid] = hit[0]
                self.link_conf[(self._slots[aid]["resource_id"], hit[0])] = "identity+run"
            elif owners:
                cand[aid] = set()       # belongs to someone outside this batch
        # 2. elimination to a fixed point (a case has exactly one run)
        self._eliminate(cand, assigned)
        self._commit(assigned)
        self._cand, self._assigned = cand, assigned
        return self

    def _eliminate(self, cand, assigned):
        changed = True
        while changed:
            changed = False
            taken = set(assigned.values())
            for aid, cs in cand.items():
                if aid in assigned:
                    continue
                free = [c for c in cs if c not in taken]
                if len(free) == 1:
                    assigned[aid] = free[0]
                    taken.add(free[0])
                    self.link_conf[(self._slots[aid]["resource_id"], free[0])] = "run-elimination"
                    changed = True

    def _commit(self, assigned):
        for aid, cid in assigned.items():
            a = self._slots[aid]
            if a["event_type"] == "CLASSIFY_REQUEST":
                self.case_classified[cid] = a
            else:
                self.case_slot[cid] = a
                self.case_resources[cid].add(a["resource_id"])

    def learn_offsets(self):
        """Unsupervised: per (system, phase) the true offset is the histogram peak over candidate pairs."""
        hist = defaultdict(Counter)
        for a in self.worker:
            for cid in self._action_cases(a):
                w = 5 if self.case_user.get(cid) in self.owner.get(a["resource_id"], set()) else 1
                hist[(a["target_system"], self._phase(cid, a))][sec_offset(a["event_time"], self.case_slot[cid]["event_time"])] += w
        for key, h in hist.items():
            # smooth over +-1 s (timestamps are rounded), then demand a clear peak vs any non-adjacent bin
            smooth = {v: h[(v - 1) % 60] + h[v] + h[(v + 1) % 60] for v in range(60)}
            val = max(range(60), key=lambda v: (smooth[v], h[v]))
            rival = max((smooth[v] for v in range(60) if circ(v, val) > 2), default=0)
            if smooth[val] >= 3 and smooth[val] >= 1.5 * rival:
                self.offsets[key] = val
        return self

    def _fingerprint_score(self, cid, slot_time) -> int:
        """How many identity-linked actions of the case's user line up with a slot at slot_time."""
        u = self.case_user.get(cid)
        rep = self.reqs[cid]["reported_at"]
        n = 0
        for a in self.worker:
            if u not in self.owner.get(a["resource_id"], set()):
                continue
            if not (ACTION_WINDOW[0] <= minutes_before(rep, a["event_time"]) <= ACTION_WINDOW[1]):
                continue
            want = self.offsets.get((a["target_system"], "pre" if a["event_time"] <= rep else "post"))
            if want is not None and circ(sec_offset(a["event_time"], slot_time), want) <= MAX_FINGERPRINT_ERR:
                n += 1
        return n

    def resolve_ambiguous_slots(self):
        cand, assigned = self._cand, self._assigned
        for _ in range(3):
            taken = set(assigned.values())
            progress = False
            for aid in sorted(cand, key=lambda a: self._slots[a]["event_time"]):
                if aid in assigned:
                    continue
                free = [c for c in cand[aid] if c not in taken]
                if not free:
                    continue
                scores = {c: self._fingerprint_score(c, self._slots[aid]["event_time"]) for c in free}
                best = max(scores.values())
                top = [c for c in free if scores[c] == best]
                if best > 0 and len(top) == 1:
                    assigned[aid] = top[0]
                    taken.add(top[0])
                    self.link_conf[(self._slots[aid]["resource_id"], top[0])] = "run-fingerprint"
                    progress = True
            self._eliminate(cand, assigned)
            if not progress:
                break
        # last resort: deterministic order, flagged as ambiguous
        taken = set(assigned.values())
        for aid in sorted(cand, key=lambda a: self._slots[a]["event_time"]):
            if aid in assigned:
                continue
            free = sorted((c for c in cand[aid] if c not in taken), key=lambda c: self.reqs[c]["requested_at"])
            if free:
                assigned[aid] = free[0]
                taken.add(free[0])
                self.link_conf[(self._slots[aid]["resource_id"], free[0])] = "run-ambiguous"
        self.case_slot.clear()
        self.case_classified.clear()
        self._commit(assigned)
        return self

    def assign_policy_actions(self):
        """Attribute worker actions on resources that carry no identity, via the timing fingerprint."""
        for a in self.worker:
            rid = a["resource_id"]
            if self.owner.get(rid):
                continue                      # identity evidence decides, never timing
            if is_operation_report(a):
                near = [cid for cid, q in self.reqs.items()
                        if REPORT_WINDOW[0] <= minutes_before(q["reported_at"], a["event_time"]) <= REPORT_WINDOW[1]]
                if len(near) == 1:
                    self.case_resources[near[0]].add(rid)
                    self.link_conf[(rid, near[0])] = "operation-report"
                continue
            scored = []
            for cid in self._action_cases(a):
                want = self.offsets.get((a["target_system"], self._phase(cid, a)))
                if want is None:
                    continue
                err = circ(sec_offset(a["event_time"], self.case_slot[cid]["event_time"]), want)
                if err <= MAX_FINGERPRINT_ERR:
                    scored.append((err, cid))
            if not scored:
                continue
            scored.sort()
            conf = "run-fingerprint" if len(scored) == 1 or scored[1][0] > scored[0][0] else "run-ambiguous"
            best = scored[0][1]
            self.case_resources[best].add(rid)
            self.link_conf[(rid, best)] = conf
        return self

    def run(self, mode: str = "full"):
        """mode: 'identity' (evidence links only) | 'runs' (+ worker-run elimination) | 'full' (+ fingerprints)."""
        self.build_owner_map()
        if mode == "identity":
            return self
        self.assign_runs()
        if mode == "runs":
            return self
        self.learn_offsets().resolve_ambiguous_slots()
        self.offsets.clear()
        return self.learn_offsets().assign_policy_actions()
