"""Policy engine: deletion_rules.csv -> required treatment -> step operations.

The rule table is read from the dataset at runtime; only the mapping from a
rule's ``required_action`` to the allowed output operations lives here.
"""
from __future__ import annotations

import csv
from pathlib import Path

from .model import (ABSENT, ACCOUNT_TOMBSTONE, ACTIVE, BACKUP_ARCHIVE, CLEAN, DATA_FLOW, IDENTIFIABLE, INACTIVE,
                    PRESENT)

# Output operation order inside each phase (problem_statement.md, "Allowed Operations")
FINDING_ORDER = ["REPORT_REMAINING_RECORD", "REPORT_EXPOSED_PII", "REPORT_ACTIVE_DATA_FLOW", "REPORT_RESTORE_RISK"]
REMEDIATION_ORDER = ["DISABLE_DATA_FLOW", "BLOCK_RESTORE", "DELETE_RECORD", "REDACT_RECORD", "ANONYMIZE_RECORD"]
VERIFICATION_ORDER = ["VERIFY_RECORD_ABSENT", "VERIFY_RECORD_PRESENT", "VERIFY_RECORD_REDACTED",
                      "VERIFY_RECORD_ANONYMIZED", "VERIFY_DATA_FLOW_DISABLED", "VERIFY_RESTORE_BLOCKED"]
OP_STATE = {
    "REPORT_REMAINING_RECORD": "PRESENT", "REPORT_EXPOSED_PII": "PRESENT", "REPORT_ACTIVE_DATA_FLOW": "ACTIVE",
    "REPORT_RESTORE_RISK": "ACTIVE", "DISABLE_DATA_FLOW": "DISABLED", "BLOCK_RESTORE": "BLOCKED",
    "DELETE_RECORD": "ABSENT", "REDACT_RECORD": "REDACTED", "ANONYMIZE_RECORD": "ANONYMIZED",
    "VERIFY_RECORD_ABSENT": "ABSENT", "VERIFY_RECORD_PRESENT": "PRESENT", "VERIFY_RECORD_REDACTED": "REDACTED",
    "VERIFY_RECORD_ANONYMIZED": "ANONYMIZED", "VERIFY_DATA_FLOW_DISABLED": "DISABLED",
    "VERIFY_RESTORE_BLOCKED": "BLOCKED",
}
PHASE_ORDER = {"FINDING": FINDING_ORDER, "REMEDIATION": REMEDIATION_ORDER, "VERIFICATION": VERIFICATION_ORDER}

# required_action -> (finding op if violated, remediation op, verification op)
TREATMENT = {
    "DELETE": ("REPORT_REMAINING_RECORD", "DELETE_RECORD", "VERIFY_RECORD_ABSENT"),
    "REDACT": ("REPORT_EXPOSED_PII", "REDACT_RECORD", "VERIFY_RECORD_REDACTED"),
    "ANONYMIZE": ("REPORT_EXPOSED_PII", "ANONYMIZE_RECORD", "VERIFY_RECORD_ANONYMIZED"),
    "RETAIN": (None, None, "VERIFY_RECORD_PRESENT"),
    "BLOCK_RESTORE": ("REPORT_RESTORE_RISK", "BLOCK_RESTORE", "VERIFY_RESTORE_BLOCKED"),
    "DISABLE": ("REPORT_ACTIVE_DATA_FLOW", "DISABLE_DATA_FLOW", "VERIFY_DATA_FLOW_DISABLED"),
}


class Policy:
    def __init__(self, dataset_dir: Path):
        self.rules = {r["data_category"]: r for r in csv.DictReader(open(Path(dataset_dir) / "deletion_rules.csv",
                                                                         encoding="utf8"))}

    def action_for(self, category: str) -> tuple[str, str]:
        """Return (required_action, rule_id) for a data category."""
        if category == DATA_FLOW:
            return "DISABLE", "no-rule:recreation-path"          # active flows must always be stopped
        if category == BACKUP_ARCHIVE:
            return "BLOCK_RESTORE", self.rules[category]["rule_id"]  # RETAIN archive, but block restore
        r = self.rules.get(category)
        if not r:
            return "DELETE", "default"
        return r["required_action"], r["rule_id"]

    def evaluate(self, category: str, state: str):
        """Map (category, observed state) -> (violation finding op | None, remediation op | None, verify op)."""
        action, rule = self.action_for(category)
        finding, remediation, verify = TREATMENT[action]
        if action == "DELETE":
            violated = state in (PRESENT, IDENTIFIABLE, CLEAN)
        elif action in ("REDACT", "ANONYMIZE"):
            violated = state in (IDENTIFIABLE, PRESENT)
            if state == ABSENT:          # over-deleted retained record: nothing left to redact
                verify = "VERIFY_RECORD_ABSENT"
        elif action in ("BLOCK_RESTORE", "DISABLE"):
            violated = state == ACTIVE
        else:                            # RETAIN
            violated = False
        return (finding if violated else None), (remediation if violated else None), verify, rule
