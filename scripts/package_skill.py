"""Package one validated skill folder as a .skill zip archive."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

try:
    from scripts.quick_validate import validate_skill
except ModuleNotFoundError:  # pragma: no cover - direct script execution fallback.
    from quick_validate import validate_skill


EXCLUDE_DIRS = {"__pycache__", ".git"}
EXCLUDE_SUFFIXES = {".pyc", ".pyo"}


def _iter_files(skill_dir: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(skill_dir.rglob("*")):
        if not path.is_file():
            continue
        if any(part in EXCLUDE_DIRS for part in path.relative_to(skill_dir).parts):
            continue
        if path.suffix in EXCLUDE_SUFFIXES:
            continue
        files.append(path)
    return files


def package_skill(skill_dir: Path, output: Path | None = None) -> Path:
    skill_dir = skill_dir.resolve()
    errors = validate_skill(skill_dir)
    if errors:
        message = "\n".join(f"- {error}" for error in errors)
        raise ValueError(f"Skill validation failed:\n{message}")

    archive_path = output.resolve() if output else skill_dir.with_suffix(".skill")
    archive_path.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in _iter_files(skill_dir):
            zf.write(path, path.relative_to(skill_dir.parent))

    return archive_path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate and package one skills/<name> folder as a .skill archive."
    )
    parser.add_argument("skill_dir", help="Path to a skill folder containing SKILL.md.")
    parser.add_argument(
        "-o",
        "--output",
        help="Archive path to write. Defaults to a sibling <skill-name>.skill file.",
    )
    args = parser.parse_args(argv)

    try:
        archive_path = package_skill(
            Path(args.skill_dir),
            Path(args.output) if args.output else None,
        )
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    print(f"Wrote {archive_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
