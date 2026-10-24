"""Evidence ingestion: turn every supplied artifact into ``Observation`` objects.

Supported formats (all discovered through ``evidence_files.csv``):
  * SQL snapshots   - executed in an in-memory SQLite DB; primary / replica /
                      failover tables are kept apart (``view``) so replication
                      drift can be detected.
  * JSON records    - snapshot bundles, service exports, record ledgers, jobs.
  * Plain text      - pipe-delimited handover reports.
  * Logs            - six syntaxes (logfmt, JSON, pipe, bracket, syslog, nested
                      cloud ``message=``). Lines are stitched by trace id so that
                      a lookup key seen on a "started" line is attached to the
                      result on the "completed" line.
  * PDFs / images   - text is extracted (pdftotext / OCR, see ``media.py``) and
                      mined for resource ids and identifiers.

Nothing here decides deletion status - it only records grounded facts.
"""
from __future__ import annotations

import csv
import json
import re
import sqlite3
from collections import defaultdict
from pathlib import Path

from .model import (ABSENT, ACCOUNT_TOMBSTONE, ACTIVE, ANALYTICS_PROFILE, BACKUP_ARCHIVE, CLEAN,
                    DATA_FLOW, IDENTIFIABLE, INACTIVE, LEGAL_HOLD_RECORD, MARKETING_PROFILE, PRESENT,
                    SEARCH_INDEX_ENTRY, SECONDARY_IDENTIFIER, SECURITY_AUDIT_LOG, SUPPORT_ATTACHMENT,
                    SUPPORT_MESSAGE, USER_EXPORT, USER_PROFILE, Observation, emails_in, norm_key)

# resource-id prefix -> (system_id, default category)
PREFIX = [
    ("audit_record_", "security_service", SECURITY_AUDIT_LOG),
    ("data_flow_", "integration_service", DATA_FLOW),
    ("legal_hold_", "legal_service", LEGAL_HOLD_RECORD),
    ("tombstone_", "identity_service", ACCOUNT_TOMBSTONE),
    ("account_", "account_service", USER_PROFILE),
    ("search_", "search_service", SEARCH_INDEX_ENTRY),
    ("analytics_", "analytics_platform", ANALYTICS_PROFILE),
    ("support_", "support_platform", SUPPORT_MESSAGE),
    ("export_", "export_service", USER_EXPORT),
    ("backup_", "backup_service", BACKUP_ARCHIVE),
    ("marketing_", "marketing_platform", MARKETING_PROFILE),
    ("object_", "object_storage", SUPPORT_ATTACHMENT),
]
RESOURCE_RE = re.compile(r"\b(?:audit_record|data_flow|legal_hold|tombstone|account|search|analytics|support|"
                         r"export|backup|marketing|object)_\d+\b")
USER_REF_RE = re.compile(r"\buser_\d+\b")
HASH_RE = re.compile(r"\b[0-9a-f]{64}\b")
PHONE_RE = re.compile(r"\+\d[\d ()-]{6,}\d")

RESULT_STATE = {
    "FOUND": PRESENT, "NOT_FOUND": ABSENT, "IDENTIFIABLE": IDENTIFIABLE, "ANONYMIZED": CLEAN,
    "REDACTED": CLEAN, "ACTIVE": ACTIVE, "DISABLED": INACTIVE, "BLOCKED": INACTIVE, "PRESENT": PRESENT,
    "ABSENT": ABSENT,
}
IDENT_FIELDS = ("email", "phone", "email_hash", "full_name", "name", "display_name", "requester_email",
                "requester_phone", "requester_name", "owner_email", "owner_phone", "customer_email",
                "uploaded_by", "subject_selector")
REF_FIELDS = ("customer_reference", "subject_reference", "user_id", "subject_ref")


def system_of(resource_id: str) -> tuple[str, str]:
    for prefix, system, cat in PREFIX:
        if resource_id.startswith(prefix):
            return system, cat
    return "unknown", "UNKNOWN"


def _keys(values) -> frozenset:
    out = set()
    for v in values:
        k = norm_key(v)
        if k:
            out.add(k)
    return frozenset(out)


def _truthy(v) -> bool:
    return str(v).strip().strip('"').lower() in ("true", "1", "yes", "allow", "allowed")


class Corpus:
    """All observations, coverage claims and identity links extracted from the dataset."""

    def __init__(self, dataset_dir: Path, media_text: dict[str, str] | None = None, known_keys=()):
        self.root = Path(dataset_dir)
        # compact (alphanumeric-only) form of every known email / phone -> normalised key, for OCR matching
        self.known_compact = {}
        for k in known_keys:
            if "@" in k:
                self.known_compact[re.sub(r"[^a-z0-9]", "", k)] = k
            elif k.startswith("tel:"):
                self.known_compact[k[4:]] = k
        self.observations: list[Observation] = []
        # (file_id, system, time): a full snapshot of `system` - anything not listed is absent
        self.coverage: list[tuple[str, str, str]] = []
        # resource_id -> set of identity keys asserted by catalog links / aliases
        self.resource_links: dict[str, set[str]] = defaultdict(set)
        self.aliases: dict[str, str] = {}          # alias text (e.g. statement no.) -> resource_id
        self.manifest = {r["file_id"]: r for r in csv.DictReader(open(self.root / "evidence_files.csv", encoding="utf8"))}
        self.media_text = media_text or {}
        self.unparsed: list[str] = []

    # ------------------------------------------------------------------ helpers
    def add(self, file_id, t, resource_id, state, keys=(), category=None, view="primary", method="", **attrs):
        system, default_cat = system_of(resource_id)
        self.observations.append(Observation(
            file_id=file_id, t=t, system=system, resource_id=resource_id, category=category or default_cat,
            state=state, keys=_keys(keys), view=view, method=method, attrs=attrs))

    def add_record(self, file_id, t, rec: dict, view="primary", method="record", store=None, collection=""):
        """Map one structured record (snapshot row, export entry) to an observation."""
        rid = rec.get("resource_id")
        if not rid:
            return
        doc = rec.get("document") if isinstance(rec.get("document"), dict) else {}
        flat = {**rec, **doc}
        idents = [flat.get(f) for f in IDENT_FIELDS]
        refs = [flat.get(f) for f in REF_FIELDS]
        text = " ".join(str(flat.get(f) or "") for f in ("message_text", "message_excerpt"))
        idents += emails_in(text)
        direct = _keys(idents)
        system, cat = system_of(rid)
        coll = (collection or "").lower()
        if "attachment" in coll or flat.get("storage_class") == "ticket_attachment":
            cat = SUPPORT_ATTACHMENT

        if cat == DATA_FLOW:
            state = ACTIVE if _truthy(flat.get("enabled")) else INACTIVE
        elif cat == BACKUP_ARCHIVE:
            state = ACTIVE if _truthy(flat.get("restore_allowed")) else INACTIVE
        elif cat == USER_EXPORT:
            avail = flat.get("download_available", flat.get("available", True))
            state = PRESENT if _truthy(avail) else ABSENT
        elif cat in (ANALYTICS_PROFILE,):
            state = IDENTIFIABLE if (direct or _keys(refs)) else CLEAN
        elif cat in (SUPPORT_MESSAGE, ACCOUNT_TOMBSTONE):
            state = IDENTIFIABLE if direct else CLEAN
        else:
            state = PRESENT
        self.add(file_id, t, rid, state, idents + refs, category=cat, view=view, method=method,
                 status=flat.get("account_status"), source=flat.get("source_resource_id"),
                 retain_until=flat.get("retention_until") or flat.get("retained_until"))

    def add_lookup_row(self, file_id, t, rec: dict, method):
        """Rows shaped like {system, resource_id, record_type, result, subject_reference|lookup_value}."""
        rid = rec.get("resource_id")
        state = RESULT_STATE.get(str(rec.get("result", "")).upper())
        if not rid or not state:
            self.unparsed.append(f"{file_id}: {rec}")
            return
        key = rec.get("subject_reference", rec.get("lookup_value"))
        self.add(file_id, rec.get("recorded_at") or t, rid, state, [key], category=rec.get("record_type"),
                 method=method)

    # ------------------------------------------------------------------ loaders
    def load(self):
        for fid, row in sorted(self.manifest.items()):
            path = self.root / row["file_path"]
            t = row["captured_at"]
            ext = path.suffix.lower()
            if ext == ".sql":
                self._sql(fid, path, t)
            elif ext == ".json":
                self._json(fid, path, t)
            elif ext == ".log":
                self._log(fid, path, t)
            elif ext == ".txt":
                self._text(fid, path.read_text(encoding="utf8"), t, method="text_report")
            elif ext in (".pdf", ".png", ".jpg", ".jpeg"):
                text = self.media_text.get(fid, "")
                if text:
                    self._media(fid, text, t, ext)
        return self

    # SQL ---------------------------------------------------------------------
    def _sql(self, fid, path, t):
        con = sqlite3.connect(":memory:")
        con.executescript(path.read_text(encoding="utf8"))
        con.row_factory = sqlite3.Row
        tables = [r[0] for r in con.execute("select name from sqlite_master where type='table'")]
        scope = {}
        if "snapshot_scope" in tables:
            scope = {r["origin_system"]: r["captured_at"] for r in con.execute("select * from snapshot_scope")}
            for system, st in scope.items():
                self.coverage.append((fid, system, st))
        table_system = {"customer_profiles": "account_service", "customer_search_documents": "search_service",
                        "customer_analytics_profiles": "analytics_platform", "support_records": "support_platform",
                        "customer_exports": "export_service", "connector_subscriptions": "integration_service",
                        "backup_restore_entries": "backup_service", "security_audit_records": "security_service"}
        for tab in tables:
            if tab == "snapshot_scope":
                continue
            rows = [dict(r) for r in con.execute(f'select * from "{tab}"')]
            view = "primary"
            m = re.match(r"(?:customer_data|customer_profiles|search_documents)_(.+)", tab)
            if m and tab not in table_system:
                view = m.group(1)
                if view != "primary":
                    view = "replica:" + view
            if tab.startswith("customer_profiles_"):         # failover account snapshot
                self.coverage.append((fid, "account_service:" + view, t))
            if tab == "search_documents_primary":
                self.coverage.append((fid, "search_service", t))
            if rows and "record_json" in rows[0]:            # full customer-data table: covers every system in it
                for system in {r["origin_system"] for r in rows}:
                    self.coverage.append((fid, f"{system}:{view}", t))
            for r in rows:
                if "record_json" in r:
                    rec = json.loads(r["record_json"])
                    self.add_record(fid, t, rec, view=view, method=f"sql:{tab}", collection=r.get("collection_name"))
                else:
                    st = scope.get(table_system.get(tab, ""), t)
                    if "enabled" in r:
                        r["enabled"] = bool(r["enabled"])
                    if "restore_allowed" in r:
                        r["restore_allowed"] = bool(r["restore_allowed"])
                    self.add_record(fid, st, r, view=view, method=f"sql:{tab}", collection=tab)

    # JSON --------------------------------------------------------------------
    def _json(self, fid, path, t):
        d = json.loads(path.read_text(encoding="utf8"))
        if "snapshots" in d:
            for s in d["snapshots"]:
                st = s.get("captured_at", t)
                if s.get("collection") == "operational_record_history":
                    for r in s["records"]:
                        self.add_lookup_row(fid, r.get("recorded_at", st), r, method="bundle:history")
                    continue
                self.coverage.append((fid, f'{s["data_store"]}#{s["collection"]}', st))
                for r in s["records"]:
                    self.add_record(fid, st, r, method=f'bundle:{s["data_store"]}', store=s["data_store"],
                                    collection=s["collection"])
        elif "service_exports" in d:
            for system, colls in d["service_exports"].items():
                for coll, recs in colls.items():
                    for r in recs:
                        self._service_export(fid, system, r, r.get("observed_at", t))
        elif isinstance(d.get("records"), list) and d["records"] and "record_type" in d["records"][0]:
            for r in d["records"]:
                self.add_lookup_row(fid, r.get("recorded_at", t), r, method="ledger")
        elif isinstance(d.get("records"), list):
            st = d.get("captured_at", t)
            for r in d["records"]:
                self.add_record(fid, st, r, method=f'json:{d.get("collection", "")}', collection=d.get("collection", ""))
        else:
            self.unparsed.append(f"{fid}: unknown json shape")

    def _service_export(self, fid, system, r, t):
        rid = r["resource_id"]
        if "status_code" in r:   # profile lookup
            prof = r.get("profile") or {}
            state = PRESENT if r["status_code"] == 200 else ABSENT
            self.add(fid, t, rid, state, [prof.get(k) for k in IDENT_FIELDS + REF_FIELDS], method="export:lookup")
        elif "hits" in r:        # search query
            docs = r["hits"].get("documents", [])
            for doc in docs:
                self.add_record(fid, t, doc, method="export:search")
            if not docs:
                self.add(fid, t, rid, ABSENT, [r.get("query")], method="export:search")
        else:
            self.add_record(fid, t, r, method=f"export:{system}")

    # Text reports --------------------------------------------------------------
    def _text(self, fid, text, t, method):
        for line in text.splitlines():
            parts = [p.strip() for p in line.lstrip("- ").split("|")]
            if len(parts) == 6 and RESOURCE_RE.fullmatch(parts[2]):
                self.add_lookup_row(fid, parts[0], {"resource_id": parts[2], "record_type": parts[3],
                                                    "result": parts[4], "subject_reference": parts[5]}, method)

    # Logs ----------------------------------------------------------------------
    KV_RE = re.compile(r'(\w+)=("(?:[^"\\]|\\.)*"|\S+)')

    def _parse_line(self, line: str) -> dict | None:
        m = re.match(r"^(\d{4}-\d\d-\d\dT[\d:]+Z)\s+(.*)$", line)
        if not m:
            return None
        ts, rest = m.groups()
        rec = {"ts": ts}
        if rest.startswith("{"):
            try:
                rec.update(json.loads(rest))
            except json.JSONDecodeError:
                return None
            rec.setdefault("service", rec.get("logger"))
            return rec
        b = re.match(r"^\[(\w+)\] \[([^\]]+)\] \[([^\]]+)\] (\w+): (.*)$", rest)
        p = rest[2:].split(" | ") if rest.startswith("| ") else []
        s = re.match(r"^<\d+>1 \S+ (\S+) (\S+) - - (.*)$", rest)
        if b:
            rec.update(level=b[1], service=b[2], trace_id=b[3], event=b[4])
            rest = b[5]
        elif len(p) >= 5:
            rec.update(level=p[0], service=p[1], trace_id=p[2], event=p[3])
            rest = " | ".join(p[4:])
        elif s:
            rec.update(service=s[1], trace_id=s[2])
            rest = s[3]
        for k, v in self.KV_RE.findall(rest):
            if v.startswith('"'):
                v = v[1:-1].replace('\\"', '"')
            if k == "message" and "=" in v:
                for k2, v2 in self.KV_RE.findall(v):
                    rec[k2] = v2.strip('"')
            else:
                rec[k] = v
        rec.setdefault("service", rec.get("function"))
        rec.setdefault("trace_id", rec.get("requestId"))
        return rec

    LOOKUP_FIELDS = ("lookup_key", "match_key", "subject_key", "scan_key", "owner_key", "subject_ref",
                     "correlation_key", "matched_value", "subject_reference")

    def _log(self, fid, path, t_file):
        recs = [r for r in (self._parse_line(l) for l in path.read_text(encoding="utf8").splitlines()) if r]
        trace_keys = defaultdict(set)
        for r in recs:
            tr = r.get("trace_id")
            if tr and r.get("event", "").endswith("_started"):
                for f in self.LOOKUP_FIELDS:
                    if r.get(f) not in (None, "null"):
                        trace_keys[tr].add(r[f])
        for r in recs:
            self._log_event(fid, r, trace_keys.get(r.get("trace_id"), set()))

    def _log_event(self, fid, r, tkeys):
        ev, rid, t = r.get("event", ""), r.get("resource_id"), r["ts"]
        if not rid or not RESOURCE_RE.fullmatch(rid) or ev.endswith("_started"):
            return
        keys = set(tkeys) | {r[f] for f in self.LOOKUP_FIELDS if r.get(f) not in (None, "null")}
        keys |= {r[f] for f in IDENT_FIELDS + REF_FIELDS if r.get(f) not in (None, "null")}
        add = lambda state, cat=None: self.add(fid, t, rid, state, keys, category=cat, method=f"log:{ev}")
        rows = r.get("rows")
        if ev == "profile_lookup_completed":
            add(PRESENT if (rows not in (None, "0") or r.get("http_status") == "200") else ABSENT)
        elif ev == "index_query_completed":
            add(PRESENT if r.get("result") == "hit" else ABSENT)
        elif ev == "audit_record_read_completed":
            add(PRESENT if rows != "0" else ABSENT)
        elif ev == "message_pii_scan":
            add(IDENTIFIABLE, SUPPORT_MESSAGE)
        elif ev == "attachment_pii_scan":
            add(PRESENT, SUPPORT_ATTACHMENT)
        elif ev == "support_ticket_read_completed":
            ident = any(r.get(f) not in (None, "null") for f in ("requester_email", "requester_name", "requester_phone"))
            add(IDENTIFIABLE if ident else CLEAN, SUPPORT_MESSAGE)
        elif ev == "message_read":
            txt = r.get("message_text", "")
            add(IDENTIFIABLE if (emails_in(txt) or PHONE_RE.search(txt)) else CLEAN, SUPPORT_MESSAGE)
        elif ev in ("contact_query_completed",):
            add(PRESENT if rows != "0" else ABSENT, SECONDARY_IDENTIFIER)
        elif ev == "analytics_identity_scan":
            add(IDENTIFIABLE if r.get("direct_identifiers", "1") != "0" else CLEAN)
        elif ev == "analytics_profile_read":
            add(IDENTIFIABLE if r.get("direct_identifiers", "0") != "0" else CLEAN)
        elif ev == "analytics_profile_read_completed":
            ident = any(r.get(f) not in (None, "null") for f in ("email", "phone", "email_hash", "customer_reference"))
            add(IDENTIFIABLE if ident else CLEAN)
        elif ev == "contact_lookup_completed":
            add(PRESENT if rows != "0" else ABSENT, SECONDARY_IDENTIFIER)
        elif ev in ("connector_config_read_completed", "connector_heartbeat", "connector_config_loaded"):
            on = _truthy(r.get("enabled")) and r.get("scheduler_registered", "true") != "false"
            add(ACTIVE if on else INACTIVE)
        elif ev == "restore_policy_read_completed":
            add(ACTIVE if _truthy(r.get("restore_allowed")) else INACTIVE)
        elif ev == "restore_candidate_evaluated":
            add(ACTIVE if _truthy(r.get("eligible")) and not _truthy(r.get("deletion_block")) else INACTIVE)
        elif ev == "restore_authorization_completed":
            add(INACTIVE if r.get("decision") == "deny" else ACTIVE)
        elif ev in ("export_download_check_completed", "export_metadata_read_completed"):
            add(PRESENT if _truthy(r.get("available")) else ABSENT)
        elif ev == "retained_order_loaded":
            add(PRESENT)
        elif ev == "record_lookup":
            self.add_lookup_row(fid, t, {"resource_id": rid, "record_type": r.get("record_type"),
                                         "result": r.get("result"), "subject_reference": r.get("subject_reference")},
                                method="log:record_lookup")
        elif ev == "deletion_marker_check":
            if r.get("marker_found") == "false":
                add(PRESENT, SECONDARY_IDENTIFIER)
        # other events (thumbnails, retries, ...) carry no resource state

    # Media (PDF / images) ------------------------------------------------------
    FUZZY_RID_RE = re.compile(r"(audit[\s_|.-]*record|data[\s_|.-]*flow|legal[\s_|.-]*hold|tombstone|account|search|"
                              r"analytics|support|export|backup|marketing|object)[\s_|.-]{0,3}(\d{2,5})\b(?!-\d)", re.I)
    ACTIVE_CUES = re.compile(r"continuous|healthy|enabled|running|live\b|scheduled", re.I)
    INACTIVE_CUES = re.compile(r"disabled|paused|stopped|blocked|deny|denied|restore (?:access )?(?:off|disabled)", re.I)
    GONE_CUES = re.compile(r"expired|not found|deleted|purged|no longer available", re.I)

    def _media(self, fid, text, t, ext):
        """Mine OCR/PDF text: resource ids, nearby identifiers, and category-specific state cues.

        OCR drops punctuation ("jane doe@mail com"), so identifiers are matched against the
        *known* identity vocabulary on alphanumeric-only text; look-alike decoys still fail
        because their compact form differs.
        """
        lines = [l for l in text.splitlines() if l.strip()]
        compact = [re.sub(r"[^a-z0-9]", "", l.lower()) for l in lines]
        origin_system = self.manifest[fid].get("origin", "")
        hits: dict[str, list[int]] = defaultdict(list)
        joined = "\n".join(lines)
        starts = [0]
        for l in lines:
            starts.append(starts[-1] + len(l) + 1)
        # OCR may split an id over lines ("data" / "flow_1121"): match on the joined text, map back to a line
        for m in self.FUZZY_RID_RE.finditer(joined):
            prefix = re.sub(r"[\s|.-]+", "_", m.group(1).lower())
            line_no = max(i for i, s in enumerate(starts[:-1]) if s <= m.end(2) - 1)
            hits[f"{prefix}_{m.group(2)}"].append(line_no)
        joined = joined.lower()
        for alias, rid in self.aliases.items():
            is_user_ref = bool(USER_REF_RE.fullmatch(alias))
            if is_user_ref and system_of(rid)[0] != origin_system:
                continue            # a bare user_N only names a tombstone inside the identity system's own UI
            pat = re.escape(alias.lower())
            for i, l in enumerate(lines):
                if re.search(rf"(?<![\w-]){pat}(?![\w-])", l.lower()):
                    hits[rid].append(i)
        if not hits and len(joined) < 20:
            return
        hits = {r: i for r, i in hits.items() if system_of(r)[0] != "unknown"}
        # identifiers per line, then each identifier belongs to the *nearest* resource mention (<= 3 lines)
        line_keys = defaultdict(set)
        for i, comp in enumerate(compact):
            for c, orig in self.known_compact.items():
                if len(c) >= 8 and c in comp:
                    line_keys[i].add(orig)
            for u in USER_REF_RE.findall(lines[i].replace(" ", "_")):
                line_keys[i].add(u.lower())
        owned = defaultdict(set)
        for i, ks in line_keys.items():
            dist = {r: min(abs(i - j) for j in idx) for r, idx in hits.items()}
            if not dist:
                break
            best = min(dist.values())
            if best <= 3:
                for r, d in dist.items():
                    if d == best:
                        owned[r] |= ks
        focus_keys = set().union(*(self.resource_links[r] for r in hits if r in self.resource_links)) if hits else set()
        for rid, idx in sorted(hits.items()):
            window = set()
            for i in idx:
                window.update(range(max(0, i - 3), min(len(lines), i + 4)))
            near_text = " ".join(lines[i] for i in sorted(window))
            seen = set(owned[rid])                             # identifiers actually visible next to the record
            if rid in self.resource_links:                    # a catalog link names the page's subject explicitly
                linked = self.resource_links[rid]
                page_keys = set().union(*line_keys.values()) if line_keys else set()
                seen = {k for k in page_keys if k in linked}   # subject identifiers shown anywhere on the page
                keys = seen or set(linked)
            else:                                             # other rows must not inherit the page subject
                keys = seen = seen - focus_keys
            system, cat = system_of(rid)
            if rid.startswith("support_") and ext == ".pdf":
                cat = SUPPORT_ATTACHMENT          # a document held by the support platform is an attachment
            direct = any("@" in k or k.startswith("tel:") for k in seen)
            if cat == DATA_FLOW:
                state = INACTIVE if self.INACTIVE_CUES.search(near_text) else ACTIVE
            elif cat == BACKUP_ARCHIVE:
                state = INACTIVE if self.INACTIVE_CUES.search(near_text) else ACTIVE
            elif cat in (ANALYTICS_PROFILE, SUPPORT_MESSAGE, ACCOUNT_TOMBSTONE):
                state = IDENTIFIABLE if direct else CLEAN
            elif cat in (USER_EXPORT, USER_PROFILE, SEARCH_INDEX_ENTRY, MARKETING_PROFILE, SUPPORT_ATTACHMENT):
                state = ABSENT if self.GONE_CUES.search(near_text) and not self.ACTIVE_CUES.search(near_text) else PRESENT
            else:
                state = PRESENT
            self.add(fid, t, rid, state, keys, category=cat, method=f"media{ext}", text_excerpt=near_text[:160])

    # Activity stream -------------------------------------------------------------
    def load_activity_links(self, activities: list[dict]):
        """Catalog-link activities are identity assertions (not state claims)."""
        for a in activities:
            if a["event_type"] != "LINK_RESOURCE_IDENTITY":
                continue
            d = a["details"]
            m = re.search(r"\b(\S+) \(([^)]+)\)", d)
            for k in emails_in(d) + USER_REF_RE.findall(d):
                self.resource_links[a["resource_id"]].add(k.lower())
            if m and m.group(2) != a["resource_id"]:
                self.aliases[m.group(2)] = a["resource_id"]
        return self
