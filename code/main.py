"""GhostTrace AI - proof-carrying deletion audit agent.

Usage (from the repository root):
    python code/main.py                 # audit dataset/deletion_requests.csv -> ./output.csv
    python code/main.py --no-llm        # rules-only intent (no local model needed)
    python code/main.py --input dataset/sample_deletion_requests.csv --output sample_pred.csv
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ghosttrace.pipeline import GhostTrace, read_csv, write_output  # noqa: E402
from ghosttrace.report import write_certificates, write_usage  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default=str(REPO / "dataset"))
    ap.add_argument("--input", default=None, help="requests CSV (default: dataset/deletion_requests.csv)")
    ap.add_argument("--output", default=str(REPO / "output.csv"))
    ap.add_argument("--no-llm", action="store_true", help="disable the local LLM intent check")
    ap.add_argument("--certificates", default=str(REPO / "code" / "evaluation" / "certificates"),
                    help="directory for per-case proof certificates ('' to skip)")
    args = ap.parse_args()

    t0 = time.time()
    gt = GhostTrace(Path(args.dataset), use_llm=not args.no_llm)
    requests = read_csv(Path(args.input)) if args.input else gt.requests
    results = gt.run(requests)
    write_output(results, Path(args.output))
    if args.certificates:
        write_certificates(results, Path(args.certificates))
    usage = write_usage(gt.intent.usage, len(results), time.time() - t0)
    counts = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
    print(f"wrote {len(results)} rows to {args.output}  {json.dumps(counts)}  "
          f"llm={'on' if gt.intent.llm_ok else 'off (rules only / cache)'}  {usage['wall_seconds']:.1f}s")


if __name__ == "__main__":
    main()
