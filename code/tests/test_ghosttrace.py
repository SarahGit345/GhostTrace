"""Unit tests for GhostTrace building blocks (run: python -m pytest code/tests -q).

Each test pins one design decision so a regression is caught before it reaches output.csv.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

CODE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(CODE))
DATASET = CODE.parent / "dataset"

from ghosttrace.audit import ResourceState  # noqa: E402
from ghosttrace.extract import Corpus, system_of  # noqa: E402
from ghosttrace.intent import rule_intent  # noqa: E402
from ghosttrace.lineage import circ, sec_offset  # noqa: E402
from ghosttrace.model import (ABSENT, ACTIVE, CLEAN, IDENTIFIABLE, INACTIVE, PRESENT, Observation,  # noqa: E402
                              is_direct_identifier, norm_key)
from ghosttrace.policy import OP_STATE, PHASE_ORDER, Policy  # noqa: E402

needs_data = pytest.mark.skipif(not DATASET.exists(), reason="dataset/ not present")


# ---------------------------------------------------------------- identifiers
def test_norm_key_normalises_case_and_phone_formats():
    assert norm_key("  Jane.Doe@Mail.COM ") == "jane.doe@mail.com"
    assert norm_key("+34 612 847 593") == norm_key("+34-612-847-593") == "tel:34612847593"
    assert norm_key("null") is None and norm_key("[REDACTED]") is None


def test_user_reference_is_not_a_direct_identifier():
    # a tombstone may keep user_N; emails/phones are direct identifiers
    assert not is_direct_identifier("user_541")
    assert is_direct_identifier("a.eze08@gmail.com")


def test_resource_prefix_maps_to_system():
    assert system_of("audit_record_12")[0] == "security_service"
    assert system_of("data_flow_9")[0] == "integration_service"
    assert system_of("tombstone_1")[0] == "identity_service"


# ---------------------------------------------------------------- intent
@pytest.mark.parametrize("text,expected", [
    ("Please permanently delete the account associated with this email address.", True),
    ("このメールアドレスに関連するアカウントの完全な削除を依頼します。", True),
    ("Solicito la eliminación permanente de la cuenta asociada a este correo.", True),
    ("My account page is gone, but my old profile still appears. Can you remove that search result too?", True),
    ("Please stop the promotional emails. I still need the account.", False),
    ("Could you send me a copy of the information held on my account? Please don't delete it.", False),
    ("Quisiera recibir una copia de mis datos personales. No quiero eliminar mi cuenta.", False),
    ("Please apply the correct treatment to records covered by the request and delete my account.", True),
])
def test_rule_intent(text, expected):
    assert rule_intent(text)[0] is expected


# ---------------------------------------------------------------- policy
@needs_data
def test_policy_from_rules_file():
    p = Policy(DATASET)
    assert p.evaluate("USER_PROFILE", PRESENT)[:3] == ("REPORT_REMAINING_RECORD", "DELETE_RECORD", "VERIFY_RECORD_ABSENT")
    assert p.evaluate("ANALYTICS_PROFILE", IDENTIFIABLE)[1] == "ANONYMIZE_RECORD"
    assert p.evaluate("ANALYTICS_PROFILE", CLEAN)[:3] == (None, None, "VERIFY_RECORD_ANONYMIZED")
    assert p.evaluate("ACCOUNT_TOMBSTONE", IDENTIFIABLE)[1] == "REDACT_RECORD"      # never DELETE
    assert p.evaluate("SECURITY_AUDIT_LOG", PRESENT)[:3] == (None, None, "VERIFY_RECORD_PRESENT")
    assert p.evaluate("BACKUP_ARCHIVE", ACTIVE)[1] == "BLOCK_RESTORE"
    assert p.evaluate("DATA_FLOW", INACTIVE)[:3] == (None, None, "VERIFY_DATA_FLOW_DISABLED")


def test_operation_table_is_complete_and_consistent():
    ops = [op for phase in PHASE_ORDER.values() for op in phase]
    assert len(ops) == 15 and set(ops) == set(OP_STATE)
    # flows and restores are neutralised before records are touched
    rem = PHASE_ORDER["REMEDIATION"]
    assert rem.index("DISABLE_DATA_FLOW") < rem.index("DELETE_RECORD")
    assert rem.index("BLOCK_RESTORE") < rem.index("DELETE_RECORD")


# ---------------------------------------------------------------- lineage fingerprint
def test_seconds_offset_is_circular():
    assert sec_offset("2026-09-02T11:31:08Z", "2026-09-02T10:48:27Z") == 41
    assert circ(59, 1) == 2 and circ(41, 40) == 1


# ---------------------------------------------------------------- log parsing
@needs_data
def test_log_parser_handles_all_syntaxes():
    c = Corpus(DATASET)
    lines = [
        '2026-09-15T11:51:19Z level=INFO service=account_service trace_id=tr-1 resource_id=account_1 event=profile_lookup_completed rows=0',
        '2026-07-03T07:51:32Z | DEBUG | security_service | tr-2 | audit_record_read_completed | resource_id="audit_record_2" rows="1"',
        '2026-07-28T05:51:21Z [INFO] [account_service] [tr-3] profile_lookup_completed: resource_id="account_3" rows="0"',
        '2026-04-19T06:51:13Z {"service":"search_service","trace_id":"tr-4","event":"index_query_completed","resource_id":"search_4","result":"hit"}',
        '2026-03-25T08:55:00Z <12>1 node-3 integration_service tr-5 - - level=WARN resource_id="data_flow_5" event="connector_heartbeat" enabled="true"',
        '2026-06-08T09:51:18Z requestId=tr-6 level=WARN function=integration_service message="resource_id=\\"data_flow_6\\" event=\\"connector_heartbeat\\" enabled=\\"true\\""',
    ]
    parsed = [c._parse_line(l) for l in lines]
    assert [p["resource_id"] for p in parsed] == ["account_1", "audit_record_2", "account_3", "search_4",
                                                  "data_flow_5", "data_flow_6"]
    assert parsed[1]["trace_id"] == "tr-2" and parsed[4]["service"] == "integration_service"


# ---------------------------------------------------------------- verifier behaviour
@needs_data
def test_conservative_tie_break_and_time_cutoff():
    from ghosttrace.audit import Auditor
    from ghosttrace.identity import IdentityResolver

    class _Lin:
        owner, case_resources, link_conf = {}, {}, {}

    c = Corpus(DATASET)
    c.manifest = {"e1": {"captured_at": "2026-01-02T00:00:00Z"}, "e2": {"captured_at": "2026-01-02T00:00:00Z"},
                  "late": {"captured_at": "2026-03-01T00:00:00Z"}}
    c.observations = [
        Observation("e1", "2026-01-02T00:00:00Z", "identity_service", "tombstone_1", "ACCOUNT_TOMBSTONE", CLEAN),
        Observation("e2", "2026-01-02T00:00:00Z", "identity_service", "tombstone_1", "ACCOUNT_TOMBSTONE", IDENTIFIABLE,
                    frozenset({"x@y.com"})),
        Observation("late", "2026-03-01T00:00:00Z", "account_service", "account_1", "USER_PROFILE", PRESENT),
    ]
    a = Auditor(c, IdentityResolver(DATASET), _Lin(), Policy(DATASET))
    tomb = a.resolve_state("tombstone_1", "2026-02-01T00:00:00Z", "2026-01-01T00:00:00Z")
    assert tomb.state == IDENTIFIABLE                     # same-time contradiction -> unsafe reading wins
    acc = a.resolve_state("account_1", "2026-02-01T00:00:00Z", "2026-01-01T00:00:00Z")
    assert acc.state is None                              # evidence after audit_at is never used


def test_complete_requires_evidence_for_every_check():
    from ghosttrace.audit import Auditor
    a = Auditor.__new__(Auditor)
    a.policy = Policy(DATASET) if DATASET.exists() else pytest.skip("dataset/ not present")
    proven = [ResourceState("account_service", "account_1", "USER_PROFILE", ABSENT, "evidence_1", "identity")]
    unproven = proven + [ResourceState("security_service", "audit_record_1", "SECURITY_AUDIT_LOG", None, "", "run")]
    assert a.plan("c1", "user_1", proven).status == "COMPLETE"
    assert a.plan("c2", "user_1", unproven).status == "INCOMPLETE"   # UNKNOWN blocks COMPLETE


def test_case_order_is_natural_like_the_request_file():
    from ghosttrace.pipeline import case_sort_key
    ids = ["case_100", "case_33", "case_550", "case_34", "case_99"]
    assert sorted(ids, key=case_sort_key) == ["case_33", "case_34", "case_99", "case_100", "case_550"]
