"""Does the request authorise deletion?  Hybrid: multilingual rules + local LLM.

* Rules: deletion verbs in the languages seen in requests (en/es/pt/fr/ja/ko/de/it)
  minus explicit non-deletion intents (access, export, correction, marketing
  opt-out ...). Deterministic and free.
* LLM (optional): an open-source model served locally by Ollama
  (default ``qwen2.5:3b``) using ``prompts/intent_classifier.md``. Answers are
  cached on disk, so a re-run costs nothing and is reproducible. Token counts
  are recorded for ``evaluation/usage_report.md``.
* Combination: when both are available and disagree, the LLM wins only with
  confidence >= 0.8; otherwise the rule decision stands. Unknown => DELETION is
  never assumed silently: the disagreement is logged in the case certificate.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache" / "intent_llm.json"
PROMPT = (ROOT / "prompts" / "intent_classifier.md").read_text(encoding="utf8")

DELETE_PATTERNS = [
    r"\bdelet", r"\berase", r"\berasure", r"\bremove (?:my|the|this) (?:account|profile)", r"\bclose (?:my|this|the) account",
    r"\baccount[- ]deletion", r"\bpermanently (?:deleted|delete|close)", r"\bwant it closed", r"\bwould like it closed",
    r"\bclosed\b.*\baccount|\baccount\b.*\bclosed", r"remove (?:records|any remaining|my name)", r"finish the deletion",
    r"\bremove (?:that|the|this|any|my) [\w ]{0,20}(?:result|copy|records?|data|details|export|file|traces?)\b",
    r"eliminaci[oó]n", r"eliminar", r"exclus[aã]o", r"excluir", r"suppression", r"supprimer", r"effacement",
    r"löschen|löschung", r"cancellazione|eliminare", r"削除", r"삭제", r"退会", r"탈퇴",
]
NON_DELETE_PATTERNS = [
    r"marketing lists? only", r"promotional e-?mails", r"\bunsubscribe\b", r"\bopt[- ]?out\b",
    r"\b(?:copy|download|portable|export) (?:of )?(?:my|the)? ?(?:account )?(?:information|data)",
    r"what personal information", r"\binvoices?\b", r"\breset(?:ting)? the login", r"can't access my profile",
    r"\bmisspelled\b", r"\bout of date\b", r"change the email address", r"\bupdate my\b", r"\bcorrect it\b",
    # explicit negation of deletion
    r"not (?:asking|a request) (?:for|to) (?:delet|eras|remov|clos)", r"(?:don't|do not|without) (?:delet|clos|remov|eras)",
    r"\bleave (?:my|the) (?:account|profile)", r"\bkeep the account\b", r"\bcontinue using\b", r"\bstill (?:need|want|use)\b",
    # other languages: access/copy requests and negated deletion
    r"copia de (?:mis|los) datos", r"no (?:quiero|deseo) (?:eliminar|borrar|cerrar)", r"c[oó]pia dos (?:meus )?dados",
    r"n[aã]o (?:quero|desejo) (?:excluir|apagar)", r"copie de mes donn[ée]es", r"ne (?:pas|veux pas) (?:supprimer|fermer)",
    r"削除しないで", r"削除は(?:希望|不要)", r"삭제하지", r"사본", r"kopie meiner daten", r"nicht l[öo]schen",
]


CONTEXT_PATTERNS = [r"\bremov", r"\bgone\b", r"\bdeleted\b", r"\bclose", r"\berased?\b", r"no longer (?:need|use)"]


def rule_intent(text: str) -> tuple[bool, str]:
    """Deletion unless the text carries an explicit non-deletion intent and no deletion verb."""
    t = text.lower()
    neg = [p for p in NON_DELETE_PATTERNS if re.search(p, t)]
    pos = [p for p in DELETE_PATTERNS if re.search(p, t)]
    if neg:   # any explicit non-deletion intent or negated deletion wins over keyword hits
        return False, f"non-deletion cue: {neg[0]}"
    if pos:
        return True, f"deletion cue: {pos[0]}"
    ctx = [p for p in CONTEXT_PATTERNS if re.search(p, t)]
    if ctx:
        return True, f"deletion-context cue: {ctx[0]}"
    return False, "no deletion cue"


class IntentClassifier:
    def __init__(self, model: str | None = None, host: str | None = None, use_llm: bool = True):
        self.model = model or os.environ.get("GHOSTTRACE_LLM_MODEL", "qwen2.5:3b")
        self.host = (host or os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")).rstrip("/")
        self.cache = json.loads(CACHE.read_text(encoding="utf8")) if CACHE.exists() else {}
        self.usage = {"provider": "ollama (local, open-source)", "model": self.model, "calls": 0,
                      "cache_hits": 0, "input_tokens": 0, "output_tokens": 0, "seconds": 0.0}
        self.llm_ok = use_llm and self._ping()

    def _ping(self) -> bool:
        try:
            with urllib.request.urlopen(self.host + "/api/tags", timeout=2) as r:
                tags = json.loads(r.read())
            return any(m.get("name", "").startswith(self.model) for m in tags.get("models", []))
        except Exception:
            return False

    def _llm(self, text: str) -> dict | None:
        key = hashlib.sha256((self.model + "\n" + text).encode()).hexdigest()
        if key in self.cache:
            self.usage["cache_hits"] += 1
            hit = self.cache[key]
            self.usage["input_tokens"] += hit.get("prompt_eval_count", 0)
            self.usage["output_tokens"] += hit.get("eval_count", 0)
            return hit["result"]
        if not self.llm_ok:
            return None
        system, user = PROMPT.split("User:", 1)
        body = {"model": self.model, "stream": False, "format": "json", "options": {"temperature": 0, "seed": 7},
                "messages": [{"role": "system", "content": system.split("System:", 1)[1].strip()},
                             {"role": "user", "content": user.replace("{request_text}", text).strip()}]}
        t0 = time.time()
        try:
            req = urllib.request.Request(self.host + "/api/chat", data=json.dumps(body).encode(),
                                         headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                resp = json.loads(r.read())
            result = json.loads(resp["message"]["content"])
        except Exception:
            return None
        self.usage["calls"] += 1
        self.usage["seconds"] += time.time() - t0
        self.usage["input_tokens"] += resp.get("prompt_eval_count", 0)
        self.usage["output_tokens"] += resp.get("eval_count", 0)
        self.cache[key] = {"result": result, "prompt_eval_count": resp.get("prompt_eval_count", 0),
                           "eval_count": resp.get("eval_count", 0)}
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        CACHE.write_text(json.dumps(self.cache, indent=1, ensure_ascii=False), encoding="utf8")
        return result

    def llm_only(self, text: str) -> bool | None:
        """LLM label alone (for the rules / LLM / hybrid comparison)."""
        llm = self._llm(text)
        if not llm or llm.get("label") not in ("DELETION", "NOT_DELETION"):
            return None
        return llm["label"] == "DELETION"

    def classify(self, text: str) -> tuple[bool, str]:
        rule, why = rule_intent(text)
        llm = self._llm(text)
        if not llm or llm.get("label") not in ("DELETION", "NOT_DELETION"):
            return rule, f"rules ({why})"
        llm_del = llm["label"] == "DELETION"
        if llm_del == rule:
            return rule, f"rules+llm agree ({why}; llm conf {llm.get('confidence')})"
        # Explicit cues (a deletion verb, or an explicit non-deletion / negation phrase) are high-precision;
        # the small local model mislabels follow-ups such as "I deleted my account - verify it is gone".
        # The LLM therefore only decides when the rules had weak or no evidence.
        weak = why.startswith("deletion-context cue") or why == "no deletion cue"
        if weak and float(llm.get("confidence", 0)) >= 0.8:
            return llm_del, f"llm decided (conf {llm.get('confidence')}); rules weak ({why})"
        return rule, f"explicit rule cue kept over llm ({why}; llm said {llm['label']})"
