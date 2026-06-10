#!/usr/bin/env python3
"""Create and validate lightweight RALF loop artifacts."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ALLOWED_STATUSES = {"running", "pass", "needs-human", "blocked"}
REQUIRED_SUMMARY_KEYS = {
    "run_tag",
    "status",
    "target",
    "terminal_point",
    "max_iterations",
    "iterations",
    "gates",
    "created_at",
}


def default_run_tag() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def safe_run_tag(value: str) -> str:
    if not re.fullmatch(r"[a-zA-Z0-9._-]+", value):
        raise SystemExit("ERROR: run tag may contain only letters, numbers, dot, underscore, and dash")
    return value


def run_dir(root: Path, run_tag: str) -> Path:
    return root / "deliverables" / "ralf-loop" / run_tag


def init_run(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    if args.max_iterations < 1:
        raise SystemExit("ERROR: max iterations must be a positive integer")
    tag = safe_run_tag(args.run_tag or default_run_tag())
    target_dir = run_dir(root, tag)
    iterations_dir = target_dir / "iterations"
    iterations_dir.mkdir(parents=True, exist_ok=True)

    summary_path = target_dir / "summary.json"
    report_path = target_dir / "report.md"

    if summary_path.exists() and not args.force:
        raise SystemExit(f"ERROR: summary already exists: {summary_path}")
    if report_path.exists() and not args.force:
        raise SystemExit(f"ERROR: report already exists: {report_path}")

    summary = {
        "run_tag": tag,
        "status": "running",
        "target": args.target_command,
        "terminal_point": args.terminal_point,
        "max_iterations": args.max_iterations,
        "iterations": [],
        "gates": [],
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    report = "\n".join(
        [
            "# RALF Loop Report",
            "",
            "Status: running",
            f"Run tag: {tag}",
            f"Target: {args.target_command}",
            f"Terminal point: {args.terminal_point}",
            "",
            "## Gates",
            "",
            "- TODO: freeze gates before fixing.",
            "",
            "## Iterations",
            "",
            "- Baseline not captured yet.",
            "",
            "## Final Result",
            "",
            "TBD",
            "",
            "## Residual Risks",
            "",
            "TBD",
            "",
        ]
    )
    report_path.write_text(report, encoding="utf-8")

    print(f"created: {target_dir}")
    print(f"summary: {summary_path}")
    print(f"report: {report_path}")
    return 0


def load_summary(path: Path) -> tuple[Path, dict[str, Any]]:
    summary_path = path / "summary.json" if path.is_dir() else path
    try:
        data = json.loads(summary_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise SystemExit(f"ERROR: cannot read summary: {summary_path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: invalid JSON in {summary_path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"ERROR: summary must be a JSON object: {summary_path}")
    return summary_path, data


def validate_summary(args: argparse.Namespace) -> int:
    summary_path, data = load_summary(Path(args.path).resolve())
    target_dir = summary_path.parent
    errors: list[str] = []

    missing = sorted(REQUIRED_SUMMARY_KEYS - data.keys())
    if missing:
        errors.append(f"missing keys: {', '.join(missing)}")
    if data.get("status") not in ALLOWED_STATUSES:
        errors.append(f"invalid status: {data.get('status')!r}")
    if not isinstance(data.get("iterations"), list):
        errors.append("iterations must be a list")
    if not isinstance(data.get("gates"), list):
        errors.append("gates must be a list")
    if not isinstance(data.get("max_iterations"), int) or data.get("max_iterations", 0) < 1:
        errors.append("max_iterations must be a positive integer")
    if not (target_dir / "report.md").exists():
        errors.append("missing report.md")
    if not (target_dir / "iterations").is_dir():
        errors.append("missing iterations/ directory")

    print(f"summary: {summary_path}")
    if errors:
        print("status: INVALID")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("status: VALID")
    print(f"run_tag: {data.get('run_tag')}")
    print(f"iterations_recorded: {len(data.get('iterations', []))}")
    print(f"gates_recorded: {len(data.get('gates', []))}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Bootstrap or validate RALF loop artifacts.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="create a RALF run artifact scaffold")
    init_parser.add_argument("--root", default=".", help="repo root for deliverables/ralf-loop")
    init_parser.add_argument("--run-tag", help="run tag to use; defaults to UTC timestamp")
    init_parser.add_argument("--target-command", default="TBD", help="frozen command or workflow")
    init_parser.add_argument("--terminal-point", default="all frozen gates pass once")
    init_parser.add_argument("--max-iterations", type=int, default=5)
    init_parser.add_argument("--force", action="store_true", help="overwrite summary/report if present")
    init_parser.set_defaults(func=init_run)

    validate_parser = subparsers.add_parser("validate", help="validate summary.json and run folder")
    validate_parser.add_argument("path", help="run directory or summary.json path")
    validate_parser.set_defaults(func=validate_summary)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
