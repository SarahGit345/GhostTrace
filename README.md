# GhostTrace AI — HackerRank Orchestrate: a proof-carrying deletion-audit agent

*HackerRank Orchestrate (October 2026), "Ghost Data Still Exists". The challenge contract is in
[`problem_statement.md`](./problem_statement.md).*

> Don't trust a deletion success message. Check the evidence, trace every path that could bring the data
> back, and produce a proof someone else can check.

GhostTrace audits each deletion request in `dataset/deletion_requests.csv`. It decides
`COMPLETE`, `INCOMPLETE` or `NOT_APPLICABLE`, and writes the ordered findings, remediation and verification steps to
`output.csv`. A deterministic verifier makes the final call. A model can help read messy inputs, but it can never
mark a deletion complete by itself.

## Quick start

```bash
# Python 3.10+ (tested on 3.13, Windows 11, CPU only)
pip install -r code/requirements.txt          # easyocr (screenshots), pypdf (PDFs); both optional

python code/main.py                            # -> ./output.csv (518 rows) + proof certificates
python code/evaluation/validate_output.py      # contract check, must print OK
python code/evaluation/main.py --show          # score vs dataset/sample_output.csv
python code/evaluation/main.py --adversarial   # + 7 mutation tests
python code/evaluation/write_reports.py        # regenerate evaluation_report.md / usage_report.md
python -m pytest code/tests -q                 # 18 unit tests (parsers, intent, policy, verifier rules)
```

**Optional local LLM (free, open-source).** Install [Ollama](https://ollama.com), then run `ollama pull qwen2.5:3b`.
`main.py` detects the model automatically and uses it as a second opinion on request intent. Use `--no-llm` to run
with rules only. Answers are cached in `code/cache/`, so re-runs are free and give the same output. The agent
needs no API keys. It reads the optional variables `OLLAMA_HOST` and `GHOSTTRACE_LLM_MODEL`.

The first run reads text from the 11 screenshots with easyocr. This takes about 1–2 minutes on CPU, and the
result is cached in `code/cache/media_text.json`. After that, a full run takes about 2 seconds.

**Runs fully offline (sandbox-safe).** No API keys, no external calls. If the local LLM, network, easyocr or pypdf
are unavailable, the pipeline uses its rules and the cached media text and produces a **byte-identical**
`output.csv` (verified with all sockets blocked and those libraries removed). The local model is an optional
second opinion only; nothing depends on it.

## Architecture

```
dataset/ ──► 1. Ingestion (extract.py, media.py)      SQL·JSON·TXT·6 log syntaxes·PDF·PNG(OCR) ──► Observations
                                                       (file_id, time, system, resource, category, state, identifiers, view)
          ─► 2. Identity resolver (identity.py)        current + historical email/phone/hash/name ─► exact, decoy-safe
          ─► 3. Temporal lineage (lineage.py)          identity links ∪ catalog links ∪ worker-run reconstruction
          ─► 4a. Intent (intent.py + prompts/)         multilingual rules ⊕ local LLM (Ollama), cached
          ─► 4b. Policy engine (policy.py)             deletion_rules.csv → treatment → allowed operations
          ─► 5. Proof-carrying verifier (audit.py)     state at audit_at → findings / plan / checks → status
          ─► 6. Output + certificates (pipeline.py, report.py) ─► output.csv, certificates/proof_certificates.md
```

**1. Evidence ingestion.** Every file listed in `evidence_files.csv` becomes an `Observation`, and each one keeps
its source `file_id` and extraction method.
- **SQL snapshots** are executed in SQLite. Primary, replica and failover tables are kept apart, so an account that
  exists only in a replica is caught (replication drift).
- **Logs** come in six syntaxes. Each line is linked to the others with the same `trace_id`: the lookup key from the
  "started" line is attached to the result on the "completed" line.
- **Screenshots** are read with OCR. The text is matched against the *known* identity vocabulary with punctuation
  stripped, so `jane doe@mail com` still matches but `jane.jr@mail.com` (a look-alike decoy) does not.

**2. Identity.** A request email can be a current or a historical address. The resolver collects every value the
person has ever held: emails, phone numbers, email hashes and names. A record is attributed to a person only when
its identifier belongs to exactly one person.

**3. Lineage: who owns which record.**
- **Direct links:** identifier evidence and catalog links (`LINK_RESOURCE_IDENTITY`).
- **Worker-run reconstruction:** some records have no identifier, for example an analytics profile that was already
  anonymised. These are linked through the deletion worker's activity.
  - A run's account submission happens 0–90 minutes before the case's `reported_at`.
  - Its result must match the status the workflow later reported (SUCCESS↔COMPLETE, PARTIAL↔PARTIALLY_COMPLETE,
    FAILED↔NOT_STARTED).
  - Links are fixed first by identity and then by elimination.
- **Timing fingerprint:** within one run, every policy action keeps a constant seconds-offset from that run's
  account submission. The offset is learned without labels, as the peak of a histogram over all candidate pairs.
  It resolves the remaining ambiguity.
- Every inferred link is labelled in the certificate (`identity`, `run-elimination`, `run-fingerprint`,
  `run-ambiguous`).

**4. Policy.** The required treatment comes from `deletion_rules.csv` at runtime:
- delete, redact, anonymise or retain;
- account tombstones keep only the internal `user_id`;
- backups are kept, but restore is blocked;
- active data flows are always disabled.

**5. Verifier.**
- Only evidence captured at or before `audit_at` counts.
- The latest observation in each view wins.
- A copy that is still alive in *any* replica keeps the record alive.
- If two readings conflict at the same timestamp, the non-compliant one wins.
- Absence is inferred from a snapshot only when the snapshot is a full account table.
- `COMPLETE` requires an evidence-backed `PASS` for every condition. An `UNKNOWN` condition blocks it.

Steps are ordered as findings, then remediation, then verification. Within each phase they follow the operation
order in the problem statement, then `system_id`, then `resource_id`. Remediation therefore disables flows and blocks
restores before any record is changed.

## Evaluation (details: `code/evaluation/evaluation_report.md`)

| configuration (32 public samples) | status acc. | step F1 | exact sequence |
|---|---|---|---|
| identity evidence only | 1.000 | 0.922 | 0.344 |
| + worker-run reconstruction | 1.000 | 0.965 | 0.656 |
| **+ learned timing fingerprints (final)** | **1.000** | **0.992** | **0.906** |

- All 7 custom adversarial mutation tests pass:
  - hidden replica copy
  - re-enabled connector
  - evidence captured after `audit_at`
  - look-alike decoy identity
  - historical email hash
  - Spanish access request
  - tombstone retention trap
- The only remaining sample misses are records that appear in no participant-visible evidence.
- Token use and cost are in `code/evaluation/usage_report.md`. The model is local and open-source, so the cost is $0.

## Repository layout (submission)

```
README.md                       this file
code/main.py                    entry point
code/requirements.txt
code/ghosttrace/                model, extract, media, identity, lineage, intent, policy, audit, pipeline, report
code/prompts/intent_classifier.md
code/tests/test_ghosttrace.py   18 unit tests pinning each design decision
code/evaluation/                main.py (scoring), metrics.py, adversarial.py, validate_output.py, write_reports.py,
                                evaluation_report.md, usage_report.md, certificates/proof_certificates.md
```

## Assumptions and limitations

- **Reported statuses and activity results are treated as claims, not proof.** They are used only to work out which
  worker run belongs to which case, never to decide the state of a record.
- **Some ambiguous links are guesses.** When two runs cannot be told apart, the link is a deterministic guess marked
  `run-ambiguous`. The certificate shows it, so a reviewer can see it.
- **Screenshots are interpreted with OCR and cue words.** A vision model can replace this layer without changing the
  verifier.
- **The audit covers only the supplied evidence.** GhostTrace cannot vouch for copies that exist outside the supplied
  dataset.
