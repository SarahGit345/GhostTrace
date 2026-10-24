"""Scoring functions shared by the evaluation scripts."""
from __future__ import annotations

import json
from collections import Counter

import csv


def read_csv(path):
    with open(path, encoding="utf8", newline="") as f:
        return list(csv.DictReader(f))


FIELDS = ("phase", "system_id", "resource_id", "operation", "state", "evidence_id")


def tup(s):
    return tuple(s[f] for f in FIELDS)


def score(pred: dict, gold: dict, verbose=False):
    m = Counter()
    per_case = []
    for cid, (gst, gsteps) in sorted(gold.items()):
        pst, psteps = pred.get(cid, ("MISSING", []))
        m["cases"] += 1
        m["status_ok"] += pst == gst
        m[f"gold_{gst}"] += 1
        m[f"ok_{gst}"] += pst == gst
        gc, pc = Counter(map(tup, gsteps)), Counter(map(tup, psteps))
        inter = sum((gc & pc).values())
        m["tp"] += inter
        m["gold_steps"] += sum(gc.values())
        m["pred_steps"] += sum(pc.values())
        m["seq_ok"] += [tup(s) for s in gsteps] == [tup(s) for s in psteps] and pst == gst
        gres = {s["resource_id"] for s in gsteps}
        pres = {s["resource_id"] for s in psteps}
        m["res_gold"] += len(gres)
        m["res_hit"] += len(gres & pres)
        m["res_pred"] += len(pres)
        # field-level: align on (phase, resource, operation)
        pidx = {(s["phase"], s["resource_id"], s["operation"]): s for s in psteps}
        for s in gsteps:
            p = pidx.get((s["phase"], s["resource_id"], s["operation"]))
            for f in FIELDS:
                m[f"field_total"] += 1
                m[f"field_ok"] += bool(p) and p[f] == s[f]
        ok = pst == gst and gc == pc
        per_case.append((cid, gst, pst, ok, sorted(gc - pc), sorted(pc - gc)))
    P = m["tp"] / max(m["pred_steps"], 1)
    R = m["tp"] / max(m["gold_steps"], 1)
    summary = {
        "cases": m["cases"],
        "status_accuracy": m["status_ok"] / m["cases"],
        "status_by_class": {k[5:]: f'{m["ok_" + k[5:]]}/{v}' for k, v in m.items() if k.startswith("gold_") and k != "gold_steps"},
        "step_precision": P, "step_recall": R, "step_f1": 2 * P * R / max(P + R, 1e-9),
        "field_accuracy": m["field_ok"] / max(m["field_total"], 1),
        "sequence_accuracy": m["seq_ok"] / m["cases"],
        "resource_recall": m["res_hit"] / max(m["res_gold"], 1),
        "resource_precision": m["res_hit"] / max(m["res_pred"], 1),
    }
    return summary, per_case


def load_gold(path: Path):
    return {r["case_id"]: (r["deletion_status"], json.loads(r["steps_json"])) for r in read_csv(path)}


