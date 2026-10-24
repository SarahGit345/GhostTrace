"""Contract checker for output.csv (run before every submission).

    python code/evaluation/validate_output.py [output.csv]

Checks: header, one row per request, sorted case ids, allowed statuses, step schema,
consecutive numbering, phase order, operation/state pairs, ordering inside phases,
evidence rules (findings + COMPLETE verifications cite admissible evidence captured
at/before audit_at; future work cites nothing), NOT_APPLICABLE -> [].
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from ghosttrace.policy import OP_STATE, PHASE_ORDER  # noqa: E402

REPO = HERE.parent.parent
WARNINGS: list[str] = []


def validate(out_path: Path, dataset: Path) -> list[str]:
    errs = []
    reqs = {r["case_id"]: r for r in csv.DictReader(open(dataset / "deletion_requests.csv", encoding="utf8"))}
    files = {r["file_id"]: r["captured_at"] for r in csv.DictReader(open(dataset / "evidence_files.csv", encoding="utf8"))}
    acts = {r["activity_id"]: r["event_time"] for r in csv.DictReader(open(dataset / "system_activity.csv", encoding="utf8"))}
    audits = {r["audit_id"]: r["event_time"] for r in csv.DictReader(open(dataset / "user_audit_log.csv", encoding="utf8"))}
    with open(out_path, encoding="utf8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    if header != ["case_id", "deletion_status", "steps_json"]:
        errs.append(f"bad header {header}")
    ids = [r[0] for r in rows]
    if ids != list(reqs):
        errs.append("rows not in deletion_requests.csv order (natural case_id order: case_33 before case_100)")
    if set(ids) != set(reqs) or len(ids) != len(reqs):
        errs.append(f"row/case mismatch: {len(ids)} rows vs {len(reqs)} requests")
    for cid, status, sj in rows:
        try:
            steps = json.loads(sj)
        except json.JSONDecodeError:
            errs.append(f"{cid}: invalid JSON")
            continue
        if status not in ("COMPLETE", "INCOMPLETE", "NOT_APPLICABLE"):
            errs.append(f"{cid}: bad status {status}")
        if status == "NOT_APPLICABLE" and steps != []:
            errs.append(f"{cid}: NOT_APPLICABLE must have []")
        audit_at = reqs.get(cid, {}).get("audit_at", "")
        last = (-1, -1, "", "")
        for i, s in enumerate(steps, 1):
            if set(s) != {"step_no", "phase", "system_id", "resource_id", "operation", "state", "evidence_id"}:
                errs.append(f"{cid}: step {i} wrong fields")
                continue
            if s["step_no"] != i:
                errs.append(f"{cid}: step numbering")
            if s["phase"] not in PHASE_ORDER or s["operation"] not in PHASE_ORDER[s["phase"]]:
                errs.append(f"{cid}: bad phase/op {s['phase']}/{s['operation']}")
                continue
            if OP_STATE[s["operation"]] != s["state"]:
                errs.append(f"{cid}: state mismatch for {s['operation']}")
            key = (list(PHASE_ORDER).index(s["phase"]), PHASE_ORDER[s["phase"]].index(s["operation"]),
                   s["system_id"], s["resource_id"])
            if key < last:
                errs.append(f"{cid}: ordering violated at step {i}")
            last = key
            ev = s["evidence_id"]
            needs = s["phase"] == "FINDING" or (status == "COMPLETE")
            if needs:
                t = files.get(ev) or acts.get(ev) or audits.get(ev)
                if not t:
                    errs.append(f"{cid}: step {i} cites unknown evidence '{ev}'")
                elif t > audit_at:
                    errs.append(f"{cid}: step {i} cites {ev} captured after audit_at")
            elif ev != "":
                errs.append(f"{cid}: future step {i} must have empty evidence_id")
        if status == "COMPLETE" and any(s["phase"] != "VERIFICATION" for s in steps):
            errs.append(f"{cid}: COMPLETE may only contain verification steps")
        if status == "INCOMPLETE" and not any(s["phase"] == "FINDING" for s in steps):
            WARNINGS.append(f"{cid}: INCOMPLETE without a finding (an UNKNOWN blocked COMPLETE)")
    return errs


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "output.csv"
    errors = validate(out, REPO / "dataset")
    for e in errors:
        print(" -", e)
    for w in WARNINGS:
        print(" ~ note:", w)
    print(f"{out}: {'OK' if not errors else str(len(errors)) + ' problem(s)'}")
    sys.exit(1 if errors else 0)
