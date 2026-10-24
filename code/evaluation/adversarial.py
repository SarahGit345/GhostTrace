"""Adversarial / mutation evaluation cases created for GhostTrace.

Each case takes a real sample request whose correct answer is known, injects a
controlled change into the evidence (or the request), and asserts how the
verdict must react. This tests the *reasoning*, not memorised answers: a system
that copied sample labels would fail every mutation.

Run:  python code/evaluation/main.py --adversarial
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from ghosttrace.model import ACTIVE, CLEAN, IDENTIFIABLE, PRESENT, Observation  # noqa: E402
from ghosttrace.pipeline import GhostTrace  # noqa: E402


def _inject(fid, captured_at, origin, obs_list):
    def mutate(gt):
        gt.corpus.manifest[fid] = {"file_id": fid, "file_path": f"synthetic/{fid}", "origin": origin,
                                   "captured_at": captured_at}
        gt.corpus.observations.extend(obs_list)
    return mutate


def _req(gt, cid, **changes):
    q = dict(next(r for r in gt.samples if r["case_id"] == cid))
    q.update(changes)
    return q


CASES = [
    {
        "name": "A1 hidden replica copy (ghost account in a read replica)",
        "why": "A primary 404 is not proof: a replica row still holds the profile.",
        "case": "case_21",
        "mutate": _inject("evidence_adv1", "2026-09-14T08:00:00Z", "customer_data_read_replica_capture", [
            Observation("evidence_adv1", "2026-09-14T08:00:00Z", "account_service", "account_6440", "USER_PROFILE",
                        PRESENT, frozenset({"amara-okeke@proton.me", "user_21"}), view="replica:read_replica",
                        method="adversarial")]),
        "expect_status": "INCOMPLETE",
        "expect_steps": [("FINDING", "account_6440", "REPORT_REMAINING_RECORD", "evidence_adv1"),
                         ("REMEDIATION", "account_6440", "DELETE_RECORD", "")],
    },
    {
        "name": "A2 re-enabled connector (resurrection path)",
        "why": "An active sync can recreate deleted data; it must be disabled before records are touched.",
        "case": "case_26",
        "mutate": _inject("evidence_adv2", "2026-09-15T11:50:00Z", "integration_management_service", [
            Observation("evidence_adv2", "2026-09-15T11:50:00Z", "integration_service", "data_flow_6244", "DATA_FLOW",
                        ACTIVE, frozenset({"user_26"}), method="adversarial")]),
        "expect_status": "INCOMPLETE",
        "expect_steps": [("FINDING", "data_flow_6244", "REPORT_ACTIVE_DATA_FLOW", "evidence_adv2"),
                         ("REMEDIATION", "data_flow_6244", "DISABLE_DATA_FLOW", "")],
        "expect_first_remediation": "DISABLE_DATA_FLOW",
    },
    {
        "name": "A3 evidence captured after audit_at must be ignored",
        "why": "Point-in-time audit: a later capture cannot change the answer.",
        "case": "case_21",
        "mutate": _inject("evidence_adv3", "2026-09-16T08:00:00Z", "customer_data_read_replica_capture", [
            Observation("evidence_adv3", "2026-09-16T08:00:00Z", "account_service", "account_6440", "USER_PROFILE",
                        PRESENT, frozenset({"amara-okeke@proton.me"}), method="adversarial")]),
        "expect_status": "COMPLETE",
        "forbid_evidence": "evidence_adv3",
    },
    {
        "name": "A4 look-alike decoy identity",
        "why": "'.jr' variant belongs to someone else and must not be attributed to the subject.",
        "case": "case_21",
        "mutate": _inject("evidence_adv4", "2026-09-15T10:00:00Z", "search_index_service", [
            Observation("evidence_adv4", "2026-09-15T10:00:00Z", "search_service", "search_99901", "SEARCH_INDEX_ENTRY",
                        PRESENT, frozenset({"amara-okeke.jr@proton.me"}), method="adversarial")]),
        "expect_status": "COMPLETE",
        "forbid_resource": "search_99901",
    },
    {
        "name": "A5 historical identifier (old email hash) still exposed",
        "why": "Identity resolution must use audit-log history, not only the current email.",
        "case": "case_25",
        "mutate": _inject("evidence_adv5", "2026-09-15T10:30:00Z", "analytics_platform", [
            Observation("evidence_adv5", "2026-09-15T10:30:00Z", "analytics_platform", "analytics_99902",
                        "ANALYTICS_PROFILE", IDENTIFIABLE, frozenset({"__HIST__"}), method="adversarial")]),
        "hist_key_of": "user_25",
        "expect_status": "INCOMPLETE",
        "expect_steps": [("FINDING", "analytics_99902", "REPORT_EXPOSED_PII", "evidence_adv5"),
                         ("REMEDIATION", "analytics_99902", "ANONYMIZE_RECORD", "")],
    },
    {
        "name": "A6 non-deletion request (access request in Spanish)",
        "why": "Personal data existing is not authorisation to delete it.",
        "case": "case_24",
        "request_text": "Quisiera recibir una copia de mis datos personales. No quiero eliminar mi cuenta.",
        "expect_status": "NOT_APPLICABLE",
    },
    {
        "name": "A7 retention trap: tombstone keeps the user_id, loses the email",
        "why": "ACCOUNT_TOMBSTONE must be REDACTED, never deleted; security record must stay PRESENT.",
        "case": "case_31",
        "mutate": _inject("evidence_adv7", "2026-09-15T11:00:00Z", "identity_service", [
            Observation("evidence_adv7", "2026-09-15T12:00:00Z", "identity_service", "tombstone_440", "ACCOUNT_TOMBSTONE",
                        IDENTIFIABLE, frozenset({"user_541", "a.eze08@gmail.com"}), method="adversarial")]),
        "expect_status": "INCOMPLETE",
        "expect_steps": [("FINDING", "tombstone_440", "REPORT_EXPOSED_PII", "evidence_adv7"),
                         ("REMEDIATION", "tombstone_440", "REDACT_RECORD", "")],
        "forbid_ops": [("tombstone_440", "DELETE_RECORD"), ("audit_record_6909", "DELETE_RECORD")],
    },
]


def run_adversarial(dataset: Path, verbose=True):
    results = []
    for case in CASES:
        mutate = case.get("mutate")
        if case.get("hist_key_of"):
            base = mutate

            def mutate(gt, base=base, uid=case["hist_key_of"]):
                ident = gt.identities.ids[uid]
                hist = sorted(k for k, src in ident.key_source.items() if src != "current" and len(k) == 64)
                key = hist[0] if hist else sorted(ident.keys)[0]
                base(gt)
                o = gt.corpus.observations[-1]
                o.keys = frozenset({key})
        gt = GhostTrace(dataset, use_llm=False, overrides={"mutate": mutate} if mutate else None)
        q = _req(gt, case["case"], **({"request_text": case["request_text"]} if "request_text" in case else {}))
        res = gt.run([q])[0]
        steps = [(s["phase"], s["resource_id"], s["operation"], s["evidence_id"]) for s in res.steps]
        checks = [res.status == case["expect_status"]]
        for exp in case.get("expect_steps", []):
            checks.append(exp in steps)
        if case.get("forbid_evidence"):
            checks.append(all(s[3] != case["forbid_evidence"] for s in steps))
        if case.get("forbid_resource"):
            checks.append(all(s[1] != case["forbid_resource"] for s in steps))
        for rid, op in case.get("forbid_ops", []):
            checks.append(all(not (s[1] == rid and s[2] == op) for s in steps))
        if case.get("expect_first_remediation"):
            rem = [s for s in steps if s[0] == "REMEDIATION"]
            checks.append(bool(rem) and rem[0][2] == case["expect_first_remediation"])
        ok = all(checks)
        results.append({"name": case["name"], "case": case["case"], "status": res.status, "pass": ok})
        if verbose:
            print(f"[{'PASS' if ok else 'FAIL'}] {case['name']}  ({case['case']} -> {res.status})")
            if not ok:
                print("      steps:", json.dumps(steps))
    passed = sum(r["pass"] for r in results)
    print(f"adversarial: {passed}/{len(results)} passed")
    return results


if __name__ == "__main__":
    run_adversarial(HERE.parent.parent / "dataset")
