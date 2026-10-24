"""Human-readable proof certificates + usage accounting."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def write_certificates(results, out_dir: Path):
    """One markdown 'deletion certificate' per run: every condition, its verdict and its evidence."""
    out_dir.mkdir(parents=True, exist_ok=True)
    lines = ["# GhostTrace deletion certificates", "",
             "Each case lists the completion conditions checked by the deterministic verifier. "
             "`PASS` = evidence proves the required state at `audit_at`; `FAIL` = evidence proves a violation "
             "(drives a finding); `UNKNOWN` = no admissible evidence (blocks a COMPLETE claim).", ""]
    for r in results:
        lines.append(f"## {r.case_id} - {r.status}")
        lines.append(f"- subject: `{r.user_id or 'n/a'}`; " + "; ".join(r.notes))
        for s in r.resources:
            lines.append(f"  - `{s.system}/{s.resource_id or '?'}` [{s.category}] state=`{s.state}` "
                         f"evidence=`{s.evidence_id or '-'}` link=`{s.link}`")
        for cond, verdict, ev in r.conditions:
            lines.append(f"  - {verdict}: {cond} ({ev or 'no evidence'})")
        lines.append("")
    (out_dir / "proof_certificates.md").write_text("\n".join(lines), encoding="utf8")


def write_usage(usage: dict, n_requests: int, wall_seconds: float) -> dict:
    u = dict(usage)
    u["requests"] = n_requests
    u["wall_seconds"] = wall_seconds
    u["total_tokens"] = u.get("input_tokens", 0) + u.get("output_tokens", 0)
    u["avg_tokens_per_request"] = u["total_tokens"] / max(n_requests, 1)
    u["estimated_cost_usd"] = 0.0          # local open-source model: no per-token charge
    path = ROOT / "cache" / "usage_last_run.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(u, indent=2), encoding="utf8")
    return u
