# GhostTrace AI - Usage report (final full-dataset run)

Source: `code/cache/usage_last_run.json`, written by `python code/main.py` for the run that produced `output.csv`.

| provider | model | where it runs | model calls | of which served from cache | input tokens | output tokens | total tokens | avg tokens / request | est. cost |
|---|---|---|---|---|---|---|---|---|---|
| ollama (local, open-source) | `qwen2.5:3b` | local CPU | 518 | 518 | 130313 | 12423 | 142736 | 275.6 | $0.00 |
| (none) | deterministic rules + OCR (easyocr) | local CPU | 0 | - | 0 | 0 | 0 | 0 | $0.00 |
| **overall** | | | **518** | **518** | **130313** | **12423** | **142736** | **275.6** | **$0.00 total / $0.00 per request** |

* Requests in the run: 518; wall time 1.7 s. Each request needs exactly one intent call; answers
  are generated live by the local model (~2.4 s/call on a laptop CPU, ~22 min for the dataset) and cached on disk, so the
  final reproducible run that wrote `output.csv` read them from `code/cache/intent_llm.json`. Token counts are the real
  prompt/completion counts reported by Ollama when each answer was generated.
* Model usage is limited to **request-intent classification** (one short call per request,
  prompt in `code/prompts/intent_classifier.md`). Evidence parsing, identity resolution, lineage,
  policy and the COMPLETE/INCOMPLETE verdict are deterministic and consume no tokens.
* Cost: open-source model (`qwen2.5` family, Apache-2.0) served by Ollama on the laptop - no per-token
  charge. For reference, the same token volume on a hosted small model (~$0.10 / 1M input,
  ~$0.40 / 1M output) would cost about $0.0180.
* If the local model is not running, the pipeline falls back to the rule classifier and the table shows 0 calls;
  answers are cached in `code/cache/intent_llm.json`, so re-runs are free and reproducible.
