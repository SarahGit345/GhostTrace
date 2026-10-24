"""Core data structures shared by every GhostTrace layer.

An ``Observation`` is one evidence-backed fact about one resource at one point
in time, e.g. "account_994 existed in the read replica at 2026-09-21T10:00Z
(evidence_05)". Every downstream decision is derived from observations, so each
one keeps its provenance (file_id + extraction method).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# Canonical observation states -------------------------------------------------
PRESENT = "PRESENT"            # record exists (identifying content unknown/irrelevant)
ABSENT = "ABSENT"              # record verified not to exist
IDENTIFIABLE = "IDENTIFIABLE"  # record exists and still carries direct identifiers
CLEAN = "CLEAN"                # record exists with identifiers removed (redacted/anonymized)
ACTIVE = "ACTIVE"              # data flow enabled / backup restorable
INACTIVE = "INACTIVE"          # data flow disabled / backup restore blocked

# Data categories (match deletion_rules.csv)
USER_PROFILE = "USER_PROFILE"
SECONDARY_IDENTIFIER = "SECONDARY_IDENTIFIER"
SEARCH_INDEX_ENTRY = "SEARCH_INDEX_ENTRY"
CACHE_ENTRY = "CACHE_ENTRY"
SUPPORT_MESSAGE = "SUPPORT_MESSAGE"
SUPPORT_ATTACHMENT = "SUPPORT_ATTACHMENT"
ANALYTICS_PROFILE = "ANALYTICS_PROFILE"
PRODUCT_TELEMETRY = "PRODUCT_TELEMETRY"
USER_EXPORT = "USER_EXPORT"
MARKETING_PROFILE = "MARKETING_PROFILE"
EMAIL_DELIVERY_LOG = "EMAIL_DELIVERY_LOG"
SECURITY_AUDIT_LOG = "SECURITY_AUDIT_LOG"
LEGAL_HOLD_RECORD = "LEGAL_HOLD_RECORD"
BACKUP_ARCHIVE = "BACKUP_ARCHIVE"
ACCOUNT_TOMBSTONE = "ACCOUNT_TOMBSTONE"
DATA_FLOW = "DATA_FLOW"

_PHONE_RE = re.compile(r"^\+?[\d\s().-]{7,}$")
_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
_USER_RE = re.compile(r"^user_\d+$")

NULLISH = {"", "null", "none", "nan", "[redacted]", "no direct identifier", "-"}


def norm_key(value) -> str | None:
    """Normalise an identifier so that the same identity always compares equal.

    Emails/user refs/hashes are lower-cased; phone numbers are reduced to digits
    (``tel:<digits>``) because the corpus formats them inconsistently.
    """
    if value is None:
        return None
    s = str(value).strip().strip('"').strip()
    if s.lower() in NULLISH:
        return None
    if _PHONE_RE.match(s) and sum(c.isdigit() for c in s) >= 7 and "@" not in s:
        return "tel:" + re.sub(r"\D", "", s)
    return s.lower()


def is_direct_identifier(key: str) -> bool:
    """Direct identifiers = values that identify a person on their own.

    The stable internal ``user_N`` reference is deliberately *not* a direct
    identifier: policy (ACCOUNT_TOMBSTONE / retained records) allows it to remain.
    """
    return bool(key) and not _USER_RE.match(key)


def emails_in(text: str) -> list[str]:
    return [m.lower() for m in _EMAIL_RE.findall(text or "")]


@dataclass
class Observation:
    file_id: str                 # participant-visible evidence id (file_id or activity_id)
    t: str                       # ISO time the fact was observed
    system: str                  # system_id as used in steps_json
    resource_id: str
    category: str
    state: str
    keys: frozenset = frozenset()   # normalised identifiers linking the record to a person
    view: str = "primary"        # e.g. "primary", "replica:eu_west", "failover"
    method: str = ""             # extraction method, for provenance / debugging
    attrs: dict = field(default_factory=dict)

    @property
    def direct_keys(self) -> set[str]:
        return {k for k in self.keys if is_direct_identifier(k)}
