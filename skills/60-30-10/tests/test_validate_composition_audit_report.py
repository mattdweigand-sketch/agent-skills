"""Tests for the 60-30-10 saved-verdict structural validator."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


SKILL_DIRECTORY = Path(__file__).parents[1]
VALIDATOR_PATH = SKILL_DIRECTORY / "scripts" / "validate_composition_audit_report.py"
SPEC = importlib.util.spec_from_file_location("composition_audit_validator", VALIDATOR_PATH)
assert SPEC and SPEC.loader
VALIDATOR_MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR_MODULE)


VALID_REPORT = """\
**Verdict:** healthy. The rules are correctly placed.

**Estimated shape:** ~40/40/20 (owned data/deterministic code/prompt-model work). High confidence from the audited rules.

**Rule basis:**
- Pricing policy: current owned data → correct owned data; writer human — checked.

**Bucket findings:**
- Owned data (~40): Pricing policy is owned here; nothing material is missing.
- Deterministic code (~40): Validation is enforced here; nothing material is missing.
- Prompt-model work (~20): Interpretation is here; nothing material is relocatable.

**Unnecessary live judgment:** none found.

**Writer exposure:** none

**Cross-target duplication:** none found within the supplied target.

**Biggest misallocation:** No material misallocation.

**Punch list (lowest risk first):**
1. Leave: Keep interpretation in prompt-model work.
"""


class ValidateCompositionAuditReportTests(unittest.TestCase):
    def test_valid_report_passes(self) -> None:
        self.assertEqual(VALIDATOR_MODULE.validate_composition_audit_report(VALID_REPORT), [])

    def test_bad_shape_and_missing_leave_fail(self) -> None:
        report = VALID_REPORT.replace("~40/40/20", "~40/40/10").replace(
            "1. Leave:", "1. Safe now:"
        )
        errors = VALIDATOR_MODULE.validate_composition_audit_report(report)
        self.assertIn(
            "Estimated shape integers must sum to approximately 100 (95–105).", errors
        )
        self.assertIn("Punch list needs at least one `Leave:` item.", errors)

    def test_missing_rule_basis_fails(self) -> None:
        report = VALID_REPORT.replace(
            "**Rule basis:**\n"
            "- Pricing policy: current owned data → correct owned data; writer human — checked.\n\n",
            "",
        )
        self.assertIn(
            "`Rule basis` must be present and non-empty.",
            VALIDATOR_MODULE.validate_composition_audit_report(report),
        )

    def test_bundled_worked_example_passes(self) -> None:
        example_text = (SKILL_DIRECTORY / "references" / "worked-example.md").read_text(
            encoding="utf-8"
        )
        self.assertEqual(VALIDATOR_MODULE.validate_composition_audit_report(example_text), [])
