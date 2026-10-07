#!/usr/bin/env python3
"""Validate the mechanically checkable contract for a saved 60-30-10 verdict."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


VERDICT_LABELS = (
    "inverted",
    "prose-heavy",
    "mid-migration",
    "roughly balanced",
    "healthy",
)
REQUIRED_REPORT_SECTIONS = (
    "Rule basis",
    "Bucket findings",
    "Unnecessary live judgment",
    "Writer exposure",
    "Cross-target duplication",
    "Biggest misallocation",
    "Punch list (lowest risk first)",
)
COMPOSITION_BUCKET = r"(?:owned data|deterministic code|prompt-model work)"
COMPOSITION_HOME = rf"{COMPOSITION_BUCKET}(?:\s*\+\s*{COMPOSITION_BUCKET})*"
RULE_BASIS_PATTERN = re.compile(
    rf".+?:\s*current\s+{COMPOSITION_HOME}\s*(?:→|->)\s*correct\s+"
    rf"(?:{COMPOSITION_HOME}|delete);?\s+writer\s+(?:human|code|model)\s+—\s+"
    r"(?:checked|unchecked)\.?",
    re.IGNORECASE,
)


def rule_basis_items(section_body: str) -> list[str]:
    """Collect top-level `- ` rules, joining wraps but excluding nested detail."""
    items: list[str] = []
    current: list[str] = []
    nested_detail = False
    for line in section_body.splitlines():
        if line.startswith("- "):
            if current:
                items.append(" ".join(current))
            current = [line[2:].strip()]
            nested_detail = False
        elif current and re.match(r"^[ \t]+(?:[-+*]|\d+[.)])\s+", line):
            nested_detail = True
        elif current and line.strip() and not nested_detail:
            current.append(line.strip())
    if current:
        items.append(" ".join(current))
    return items


def report_section_body(report_text: str, heading: str) -> str | None:
    """Return one bold-label section body from a rendered 60-30-10 verdict."""
    pattern = re.compile(
        rf"^\*\*{re.escape(heading)}:\*\*[ \t]*(.*?)(?=^\*\*[^\n]+:\*\*|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(report_text)
    if not match:
        return None
    body = match.group(1)
    return body.strip("\r\n") if body.strip() else ""


def validate_composition_audit_report(report_text: str) -> list[str]:
    """Return format failures without deciding whether the audit's judgment is sound."""
    errors: list[str] = []

    verdict = re.search(r"^\*\*Verdict:\*\*\s*([^\n.]+)", report_text, re.MULTILINE)
    if not verdict or verdict.group(1).strip() not in VERDICT_LABELS:
        errors.append(f"Verdict must be one of: {', '.join(VERDICT_LABELS)}.")

    estimated_shape = report_section_body(report_text, "Estimated shape")
    shape = (
        re.search(
            r"~(\d+)/(\d+)/(\d+)\s*"
            r"\(owned data/deterministic code/prompt-model work\)",
            estimated_shape,
        )
        if estimated_shape
        else None
    )
    if not shape:
        errors.append(
            "Estimated shape must be formatted "
            "`~X/Y/Z (owned data/deterministic code/prompt-model work)`.")
    else:
        shares = [int(value) for value in shape.group(1, 2, 3)]
        if not 95 <= sum(shares) <= 105:
            errors.append("Estimated shape integers must sum to approximately 100 (95–105).")
        if not re.search(r"\b(low|medium|high)\b", estimated_shape, re.IGNORECASE):
            errors.append("Estimated shape must state low, medium, or high confidence.")

    for heading in REQUIRED_REPORT_SECTIONS:
        if not report_section_body(report_text, heading):
            errors.append(f"`{heading}` must be present and non-empty.")

    rule_basis = report_section_body(report_text, "Rule basis")
    if rule_basis:
        items = rule_basis_items(rule_basis)
        if not items:
            errors.append("Rule basis needs at least one top-level `- ` rule bullet.")
        for index, item in enumerate(items, start=1):
            if not RULE_BASIS_PATTERN.fullmatch(item):
                errors.append(
                    f"Rule basis bullet {index} needs current home, correct home or "
                    "delete, a `→` or `->` separator, and writer/check status.")

    bucket_findings = report_section_body(report_text, "Bucket findings")
    if bucket_findings:
        for bucket in ("Owned data", "Deterministic code", "Prompt-model work"):
            if not re.search(
                rf"^-\s+{bucket}\s*\(~\d+\):", bucket_findings, re.MULTILINE
            ):
                errors.append(
                    f"Bucket findings must include a `{bucket} (~N):` bullet.")

    punch_list = report_section_body(report_text, "Punch list (lowest risk first)")
    if punch_list:
        labels = re.findall(
            r"^\d+\.\s+(Safe now|Gated on evidence|Leave):\s+\S",
            punch_list,
            re.MULTILINE,
        )
        if not labels:
            errors.append("Punch list needs at least one labeled numbered item.")
        elif "Leave" not in labels:
            errors.append("Punch list needs at least one `Leave:` item.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a saved 60-30-10 audit verdict's structural contract."
    )
    parser.add_argument("report_file", type=Path, help="UTF-8 text report to validate")
    args = parser.parse_args()

    try:
        report_text = args.report_file.read_text(encoding="utf-8")
    except OSError as error:
        print(f"Cannot read {args.report_file}: {error}", file=sys.stderr)
        return 2

    errors = validate_composition_audit_report(report_text)
    if errors:
        print("Invalid 60-30-10 verdict:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Valid 60-30-10 verdict: {args.report_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
