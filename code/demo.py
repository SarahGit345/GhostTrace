"""GhostTrace demo - audit one deletion request and explain the verdict.

Usage (from the repository root):
    python code/demo.py                  # default walkthrough (case_201)
    python code/demo.py --case case_195  # any case from deletion_requests.csv or the samples
    python code/demo.py --list           # show a few interesting cases to try
"""
from __future__ import annotations

import argparse
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ghosttrace.pipeline import GhostTrace  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
WIDTH = 78

SHOWCASE = {
    "case_201": "workflow said PARTIALLY_COMPLETE; account, search entry, support ticket and a live sync remain",
    "case_195": "workflow said COMPLETE and the evidence agrees; retained security record is kept",
    "case_199": "workflow said COMPLETE, but the primary account still exists",
    "case_198": "workflow said NOT_STARTED; support ticket still exposes the email",
    "case_534": "not a deletion request at all -> NOT_APPLICABLE",
}


def rule(title: str = ""):
    print(f"\n-- {title} " + "-" * max(0, WIDTH - len(title) - 4) if title else "-" * WIDTH)


def wrap(text: str, indent: str = "  "):
    print(textwrap.fill(text, WIDTH, initial_indent=indent, subsequent_indent=indent))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--case", default="case_201")
    ap.add_argument("--list", action="store_true", help="list showcase cases and exit")
    ap.add_argument("--no-llm", action="store_true", help="rules-only intent check")
    args = ap.parse_args()

    if args.list:
        for cid, why in SHOWCASE.items():
            print(f"  {cid:10} {why}")
        return

    gt = GhostTrace(REPO / "dataset", use_llm=not args.no_llm)
    requests = {q["case_id"]: q for q in gt.samples + gt.requests}
    q = requests.get(args.case)
    if not q:
        sys.exit(f"unknown case {args.case!r}; try --list")
    res = gt.run([q])[0]

    print("=" * WIDTH)
    print(f"GhostTrace audit  |  {q['case_id']}".center(WIDTH))
    print("=" * WIDTH)

    rule("1. The request")
    print(f"  from      {q['email']}")
    print(f"  requested {q['requested_at']}   audited as of {q['audit_at']}")
    wrap(f'"{q["request_text"]}"')
    print(f"  intent    {next((n[8:] for n in res.notes if n.startswith('intent: ')), '-')}")

    rule("2. What the old workflow claimed")
    print(f"  reported_status = {q['reported_status']}   (a claim, not proof)")

    if res.status == "NOT_APPLICABLE":
        rule("Verdict")
        print("  NOT_APPLICABLE - the person did not ask for deletion, so nothing is deleted or verified.")
        return

    ident = gt.identities.resolve(q["email"])
    rule("3. Who the person is")
    if ident:
        print(f"  subject   {ident.user_id}")
        print(f"  knows     {len(ident.keys)} current + historical identifiers (emails, phones, hashes, names)")

    rule("4. Every copy found, and its state at audit time")
    print(f"  {'system':20} {'record':20} {'state':13} {'evidence':12} link")
    for s in res.resources:
        if not s.resource_id:
            continue
        print(f"  {s.system:20} {s.resource_id:20} {(s.state or 'not seen'):13} {(s.evidence_id or '-'):12} {s.link}")

    rule("5. Proof certificate (checked by the deterministic verifier)")
    for name, verdict, ev in res.conditions:
        print(f"  {verdict:8} {name}" + (f"  ({ev})" if ev else ""))

    rule("6. Ordered steps written to output.csv")
    for st in res.steps:
        ev = f"  <- {st['evidence_id']}" if st["evidence_id"] else ""
        print(f"  {st['step_no']:>2}. {st['phase']:12} {st['operation']:26} {st['resource_id']}{ev}")

    rule("Verdict")
    claim, verdict = q["reported_status"], res.status
    print(f"  workflow claimed {claim}  ->  GhostTrace verified {verdict}")
    if verdict == "INCOMPLETE":
        n = sum(1 for st in res.steps if st["phase"] == "FINDING")
        wrap(f"{n} finding(s) prove the user's data is not fully gone; the remediation steps above "
             "fix it in a safe order (stop syncs and restores first), then the checks confirm it.")
    else:
        wrap("Every copy has the treatment the policy requires, each check cites evidence captured "
             "before the audit time, and retained records are still available.")
    print("=" * WIDTH)


if __name__ == "__main__":
    main()
