"""Identity resolution: request email -> stable user_id -> every identifier ever held.

``user_identities.csv`` is the current snapshot; ``user_audit_log.csv`` records
historical field changes (old/new email, phone, email_hash, name). A request
email may be either a current or a historical value. Matching is exact on
normalised values only - look-alike decoys (``x.jr@...``, similar names) must
never be merged.
"""
from __future__ import annotations

import csv
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from .model import norm_key


@dataclass
class Identity:
    user_id: str
    keys: set = field(default_factory=set)            # all normalised identifiers (incl. user_id)
    key_source: dict = field(default_factory=dict)    # key -> "current" | audit_id
    names: set = field(default_factory=set)


class IdentityResolver:
    FIELDS = ("email", "phone", "email_hash", "name")

    def __init__(self, dataset_dir: Path):
        root = Path(dataset_dir)
        self.users = {r["user_id"]: r for r in csv.DictReader(open(root / "user_identities.csv", encoding="utf8"))}
        self.audit = list(csv.DictReader(open(root / "user_audit_log.csv", encoding="utf8")))
        self.by_key: dict[str, set[str]] = defaultdict(set)   # identifier -> user_ids that ever held it
        self.ids: dict[str, Identity] = {}
        for uid, r in self.users.items():
            ident = self.ids.setdefault(uid, Identity(uid))
            self._add(ident, uid, "current")
            for f in self.FIELDS:
                self._add(ident, r.get(f), "current")
        for a in self.audit:
            ident = self.ids.setdefault(a["user_id"], Identity(a["user_id"]))
            for v in (a["old_value"], a["new_value"]):
                self._add(ident, v, a["audit_id"])

    def _add(self, ident: Identity, value, source):
        k = norm_key(value)
        if not k:
            return
        ident.keys.add(k)
        ident.key_source.setdefault(k, source)
        self.by_key[k].add(ident.user_id)

    def resolve(self, email: str) -> Identity | None:
        """Return the unique identity holding ``email`` (current or historical)."""
        uids = self.by_key.get(norm_key(email) or "", set())
        if len(uids) != 1:
            return None          # unknown or ambiguous -> never guess
        return self.ids[next(iter(uids))]

    def owners(self, key: str) -> set[str]:
        return self.by_key.get(key, set())
