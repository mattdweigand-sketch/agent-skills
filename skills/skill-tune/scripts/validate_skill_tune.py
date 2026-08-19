#!/usr/bin/env python3
"""Deterministically validate the skill-tune skill directory."""

from __future__ import annotations

import sys
from pathlib import Path


EXPECTED_FILES = {
    "SKILL.md",
    "agents/openai.yaml",
    "references/agentic-skill-safety.md",
    "references/prompt-debt-taxonomy.md",
    "scripts/validate_skill_tune.py",
}
REQUIRED_INTERFACE_FIELDS = {
    "default_prompt",
    "display_name",
    "short_description",
}


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("SKILL.md must begin with YAML frontmatter delimiter '---'.")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("SKILL.md frontmatter has no closing delimiter.") from exc

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def parse_interface_metadata(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "interface:":
        raise ValueError("agents/openai.yaml must begin with 'interface:'.")

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:], 2):
        if not line or line.lstrip().startswith("#"):
            continue
        if not line.startswith("  ") or line.startswith("   ") or ":" not in line[2:]:
            raise ValueError(
                f"Invalid agents/openai.yaml line {line_number}: {line!r}"
            )
        key, value = line[2:].split(":", 1)
        key = key.strip()
        value = value.strip()
        if value[:1] in {'"', "'"} or value[-1:] in {'"', "'"}:
            if len(value) < 2 or value[0] != value[-1]:
                raise ValueError(
                    f"Mismatched quotes in agents/openai.yaml line {line_number}: "
                    f"{line!r}"
                )
            value = value[1:-1]
        if not key or not value:
            raise ValueError(
                f"Empty agents/openai.yaml field on line {line_number}: {line!r}"
            )
        if key in fields:
            raise ValueError(f"Duplicate agents/openai.yaml field: {key!r}")
        fields[key] = value
    return fields


def main() -> int:
    skill_dir = (
        Path(sys.argv[1]).resolve()
        if len(sys.argv) == 2
        else Path(__file__).resolve().parents[1]
    )
    errors: list[str] = []

    if len(sys.argv) > 2:
        errors.append("Usage: validate_skill_tune.py [SKILL_DIRECTORY]")
    if not skill_dir.is_dir():
        errors.append(f"Skill directory does not exist: {skill_dir}")

    skill_file = skill_dir / "SKILL.md"
    if skill_dir.is_dir() and not skill_file.is_file():
        errors.append("Missing SKILL.md.")
    elif skill_file.is_file():
        try:
            frontmatter = parse_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(str(exc))
        else:
            if frontmatter.get("name") != "skill-tune":
                errors.append("Frontmatter name must equal 'skill-tune'.")
            if not frontmatter.get("description"):
                errors.append("Frontmatter must include a non-empty description.")

    interface_file = skill_dir / "agents/openai.yaml"
    if interface_file.is_file():
        try:
            interface_fields = parse_interface_metadata(interface_file)
        except ValueError as exc:
            errors.append(str(exc))
        else:
            missing_interface_fields = sorted(
                REQUIRED_INTERFACE_FIELDS - interface_fields.keys()
            )
            if missing_interface_fields:
                errors.append(
                    "Missing agents/openai.yaml fields: "
                    + ", ".join(missing_interface_fields)
                )

    if skill_dir.is_dir():
        actual_files = {
            path.relative_to(skill_dir).as_posix()
            for path in skill_dir.rglob("*")
            if path.is_file()
        }
        missing = sorted(EXPECTED_FILES - actual_files)
        unexpected = sorted(actual_files - EXPECTED_FILES)
        if missing:
            errors.append(f"Missing expected files: {', '.join(missing)}")
        if unexpected:
            errors.append(f"Unexpected files: {', '.join(unexpected)}")

    if errors:
        print("skill-tune validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"skill-tune validation passed: {skill_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
