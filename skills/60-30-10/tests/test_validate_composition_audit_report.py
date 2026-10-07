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
    def report_with_rules(self, rules: str) -> str:
        return VALID_REPORT.replace(
            "- Pricing policy: current owned data → correct owned data; writer human — checked.",
            rules,
        )

    def test_valid_report_passes(self) -> None:
        self.assertEqual(VALIDATOR_MODULE.validate_composition_audit_report(VALID_REPORT), [])

    def test_ascii_arrow_passes(self) -> None:
        report = VALID_REPORT.replace(" → ", " -> ")
        self.assertEqual(VALIDATOR_MODULE.validate_composition_audit_report(report), [])

    def test_lone_hyphen_and_greater_than_fail(self) -> None:
        for separator in ("-", ">"):
            with self.subTest(separator=separator):
                report = VALID_REPORT.replace(" → ", f" {separator} ")
                self.assertTrue(VALIDATOR_MODULE.validate_composition_audit_report(report))

    def test_multiple_valid_rules_pass(self) -> None:
        rules = (
            "- Pricing policy: current owned data → correct owned data; writer human — checked.\n"
            "- Stage gate: current prompt-model work -> correct deterministic code; writer model — unchecked.\n"
            "- Fixed decision: current prompt-model work → correct delete; writer human — unchecked."
        )
        self.assertEqual(
            VALIDATOR_MODULE.validate_composition_audit_report(self.report_with_rules(rules)), []
        )

    def test_malformed_top_level_rule_fails_in_every_position(self) -> None:
        valid = "- Policy: current owned data → correct owned data; writer human — checked."
        for index in range(3):
            with self.subTest(index=index):
                rules = [valid, valid, valid]
                rules[index] = "- garbage"
                errors = VALIDATOR_MODULE.validate_composition_audit_report(
                    self.report_with_rules("\n".join(rules))
                )
                self.assertEqual(len(errors), 1, errors)
                self.assertIn(f"bullet {index + 1}", errors[0])

    def test_wrapped_rule_passes(self) -> None:
        for indent in ("", "  "):
            with self.subTest(indent=indent):
                rules = (
                    "- Pricing policy: current owned data\n"
                    f"{indent}-> correct owned data;\n"
                    f"{indent}writer human — checked."
                )
                self.assertEqual(
                    VALIDATOR_MODULE.validate_composition_audit_report(
                        self.report_with_rules(rules)
                    ), []
                )

    def test_nested_supporting_detail_passes(self) -> None:
        for marker in ("-", "*", "+", "1."):
            with self.subTest(marker=marker):
                rules = (
                    "- Pricing policy: current owned data → correct owned data; writer human — checked.\n"
                    f"  {marker} Evidence: the record schema passed.\n"
                    "    This continuation describes the evidence, not another rule.\n"
                    "- Routing: current prompt-model work → correct prompt-model work; writer human — unchecked."
                )
                self.assertEqual(
                    VALIDATOR_MODULE.validate_composition_audit_report(
                        self.report_with_rules(rules)
                    ), []
                )

    def test_valid_nested_rule_cannot_rescue_invalid_parent(self) -> None:
        rules = (
            "- garbage\n"
            "  - Pricing policy: current owned data → correct owned data; writer human — checked."
        )
        self.assertTrue(
            VALIDATOR_MODULE.validate_composition_audit_report(self.report_with_rules(rules))
        )

    def test_nested_rule_only_is_not_a_top_level_rule(self) -> None:
        rules = "  - Pricing policy: current owned data → correct owned data; writer human — checked."
        self.assertTrue(
            VALIDATOR_MODULE.validate_composition_audit_report(self.report_with_rules(rules))
        )

    def test_missing_rule_fields_fail(self) -> None:
        for fragment in ("current owned data", "correct owned data", "writer human", "checked"):
            with self.subTest(fragment=fragment):
                report = VALID_REPORT.replace(fragment, "", 1)
                self.assertTrue(VALIDATOR_MODULE.validate_composition_audit_report(report))

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
