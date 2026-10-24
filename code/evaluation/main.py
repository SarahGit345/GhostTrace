"""Evaluation workflow for GhostTrace.

    python code/evaluation/main.py              # score sample requests vs dataset/sample_output.csv
    python code/evaluation/main.py --adversarial  # + mutation tests (see adversarial.py)

Metrics
  * case accuracy      - deletion_status exact match
  * step P/R/F1        - multiset match on full step tuples (phase, system, resource, op, state, evidence)
  * field accuracy     - for steps matched on (phase, resource_id, operation): agreement of every field
  * sequence accuracy  - steps_json identical (order included) per case
  * resource recall    - expected resource_ids discovered
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

from ghosttrace.pipeline import GhostTrace  # noqa: E402
from metrics import load_gold, score  # noqa: E402

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default=str(HERE.parent.parent / "dataset"))
    ap.add_argument("--no-llm", action="store_true")
    ap.add_argument("--adversarial", action="store_true")
    ap.add_argument("--show", action="store_true", help="print per-case diffs")
    args = ap.parse_args()
    D = Path(args.dataset)
    gt = GhostTrace(D, use_llm=not args.no_llm)
    results = gt.run(gt.samples)
    pred = {r.case_id: (r.status, r.steps) for r in results}
    summary, per_case = score(pred, load_gold(D / "sample_output.csv"))
    print(json.dumps(summary, indent=2))
    if args.show:
        for cid, g, p, ok, missing, extra in per_case:
            if not ok:
                print(f"\n{cid}: gold={g} pred={p}")
                for x in missing:
                    print("   - missing", x)
                for x in extra:
                    print("   + extra  ", x)
    if args.adversarial:
        from adversarial import run_adversarial  # noqa: E402
        run_adversarial(D)


if __name__ == "__main__":
    main()
