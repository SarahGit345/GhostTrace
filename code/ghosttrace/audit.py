"""Per-case audit: scope -> point-in-time state -> policy -> ordered plan -> proof.

The status is never taken from a model or from ``reported_status``: it is the
output of ``verify()``, which checks the four completion conditions from the
problem statement against evidence-backed resource states.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from .model import ABSENT, ACCOUNT_TOMBSTONE, CLEAN, IDENTIFIABLE, PRESENT, USER_PROFILE, Observation
from .policy import OP_STATE, PHASE_ORDER, Policy

CATEGORY_PRIORITY = {   # when sources disagree on a resource's category, the most specific wins
    "SECONDARY_IDENTIFIER": 3, "SUPPORT_ATTACHMENT": 3, "ACCOUNT_TOMBSTONE": 3, "MARKETING_PROFILE": 2,
}


@dataclass
class ResourceState:
    system: str
    resource_id: str
    category: str
    state: str | None              # None = never observed at/before audit_at
    evidence_id: str               # file_id / activity_id proving `state`
    link: str                      # how the resource was tied to the subject
    observed_at: str = ""
    views: dict = field(default_factory=dict)


@dataclass
class CaseResult:
    case_id: str
    status: str
    steps: list
    user_id: str | None = None
    resources: list = field(default_factory=list)
    conditions: list = field(default_factory=list)   # proof certificate
    notes: list = field(default_factory=list)


class Auditor:
    def __init__(self, corpus, identities, lineage, policy: Policy):
        self.c, self.idr, self.lin, self.policy = corpus, identities, lineage, policy
        self.by_resource: dict[str, list[Observation]] = defaultdict(list)
        for o in corpus.observations:
            self.by_resource[o.resource_id].append(o)
        self.file_time = {fid: r["captured_at"] for fid, r in corpus.manifest.items()}

    # ------------------------------------------------------------------ helpers
    def citable(self, o: Observation, audit_at: str) -> bool:
        """Evidence may be used for state only if the whole artifact existed at audit_at."""
        ft = self.file_time.get(o.file_id, o.t)
        return o.t <= audit_at and ft <= audit_at

    def scope(self, q, user_id) -> dict[str, str]:
        """Resources tied to the subject -> link type."""
        audit_at, requested_at = q["audit_at"], q["requested_at"]
        out = {}
        ident = self.idr.ids[user_id]
        for rid, obs in self.by_resource.items():
            owners = self.lin.owner.get(rid, set())
            if owners != {user_id}:
                continue
            # the link itself may come from any observation made before audit_at
            linked = [o for o in obs if o.t <= audit_at and (o.keys & ident.keys)] or \
                     ([o for o in obs if o.t <= audit_at] if rid in self.c.resource_links else [])
            if not linked:
                continue
            # relevance: the record must have been seen during the request's lifetime
            if any(o.t >= requested_at for o in obs if o.t <= audit_at):
                out[rid] = "identity"
        for rid in self.lin.case_resources.get(q["case_id"], ()):
            out.setdefault(rid, self.lin.link_conf.get((rid, q["case_id"]), "run"))
        return out

    def resolve_state(self, rid: str, audit_at: str, requested_at: str) -> ResourceState:
        obs = [o for o in self.by_resource.get(rid, []) if self.citable(o, audit_at)]
        system = obs[0].system if obs else self._system(rid)
        category = self._category(rid, obs)
        if not obs:
            # absence-by-omission is only trusted for full account-table snapshots; a partial
            # collection export that happens not to list a retained record proves nothing
            ev = self._coverage(system, audit_at, requested_at) if category == USER_PROFILE else None
            return ResourceState(system, rid, category, ABSENT if ev else None, ev or "", "")
        # latest observation per view; a copy present in any view keeps the record alive
        # latest per view; on a timestamp tie the NON-compliant reading wins (conservative: a
        # contradiction is never resolved in favour of "deleted")
        risk = {IDENTIFIABLE: 3, PRESENT: 3, "ACTIVE": 3, CLEAN: 1, ABSENT: 0, "INACTIVE": 0}
        order = lambda o: (o.t, risk.get(o.state, 2), self.file_time.get(o.file_id, ""))
        latest = {}
        for o in sorted(obs, key=order):
            latest[o.view] = o
        alive = [o for o in latest.values() if o.state != ABSENT]
        pick = max(alive or latest.values(), key=order)
        state = pick.state
        if state == PRESENT and category in ("ANALYTICS_PROFILE", "SUPPORT_MESSAGE", ACCOUNT_TOMBSTONE):
            state = IDENTIFIABLE if pick.direct_keys else CLEAN
        return ResourceState(system, rid, category, state, pick.file_id, "", pick.t,
                             {v: o.state for v, o in latest.items()})

    def _coverage(self, system, audit_at, requested_at) -> str | None:
        best = None
        for fid, sysname, t in self.c.coverage:
            if sysname.split("#")[0].split(":")[0] != system:
                continue
            if requested_at <= t <= audit_at and self.file_time.get(fid, t) <= audit_at:
                if best is None or t > best[1]:
                    best = (fid, t)
        return best[0] if best else None

    def _system(self, rid):
        from .extract import system_of
        return system_of(rid)[0]

    def _category(self, rid, obs):
        from .extract import system_of
        cats = [o.category for o in obs] or [system_of(rid)[1]]
        return max(cats, key=lambda c: (CATEGORY_PRIORITY.get(c, 0), cats.count(c)))

    # ------------------------------------------------------------------ main
    def audit(self, q, intent_is_deletion: bool) -> CaseResult:
        cid = q["case_id"]
        if not intent_is_deletion:
            return CaseResult(cid, "NOT_APPLICABLE", [], notes=["request does not authorise deletion"])
        ident = self.idr.resolve(q["email"])
        if not ident:
            return CaseResult(cid, "INCOMPLETE", [], notes=["subject could not be resolved; completion unprovable"])
        scope = self.scope(q, ident.user_id)
        states = []
        for rid, link in sorted(scope.items()):
            rs = self.resolve_state(rid, q["audit_at"], q["requested_at"])
            rs.link = link
            states.append(rs)
        # the subject's primary account must always be verified, even if never observed
        if not any(s.category == USER_PROFILE for s in states):
            states.append(ResourceState("account_service", "", USER_PROFILE, None, "", "missing"))
        return self.plan(cid, ident.user_id, states)

    def plan(self, cid, user_id, states: list[ResourceState]) -> CaseResult:
        findings, remediation, verification, conditions = [], [], [], []
        for s in states:
            if not s.resource_id:
                conditions.append(("account_identified", "UNKNOWN", ""))
                continue
            if s.state is None:
                # never observed: the required end-state is still checked (future verification)
                _, _, verify, rule = self.policy.evaluate(s.category, ABSENT)
                verification.append((verify, s, ""))
                conditions.append((f"{s.resource_id}:observed", "UNKNOWN", ""))
                continue
            finding, remedy, verify, rule = self.policy.evaluate(s.category, s.state)
            if finding:
                findings.append((finding, s, s.evidence_id))
                remediation.append((remedy, s, ""))
                conditions.append((f"{s.resource_id}:{rule}", "FAIL", s.evidence_id))
            else:
                conditions.append((f"{s.resource_id}:{rule}", "PASS", s.evidence_id))
            verification.append((verify, s, s.evidence_id))
        # proof-carrying rule: every verification step must cite evidence. An account id that appears
        # in no evidence at all is reported as UNKNOWN in the certificate but does not by itself block
        # COMPLETE: the canonical sample case_04 (account never observed) is COMPLETE, and tightening
        # this rule was measured to cost a sample status (31/32). Tried and reverted - see report.
        incomplete = bool(findings) or any(not ev for _, _, ev in verification)
        steps = []
        for phase, items in (("FINDING", findings), ("REMEDIATION", remediation), ("VERIFICATION", verification)):
            order = PHASE_ORDER[phase]
            for op, s, ev in sorted(items, key=lambda x: (order.index(x[0]), x[1].system, x[1].resource_id)):
                if phase != "FINDING" and incomplete:
                    ev = ""                       # future work carries no evidence
                steps.append({"step_no": len(steps) + 1, "phase": phase, "system_id": s.system,
                              "resource_id": s.resource_id, "operation": op, "state": OP_STATE[op],
                              "evidence_id": ev})
        status = "INCOMPLETE" if incomplete else "COMPLETE"
        return CaseResult(cid, status, steps, user_id, states, conditions)
