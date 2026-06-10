#!/usr/bin/env python3
"""Deterministic root-hygiene check for repo-structure-audit."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


CODE_MANIFESTS = {
    "package.json",
    "pyproject.toml",
    "Cargo.toml",
    "go.mod",
    "pom.xml",
    "build.gradle",
    "Makefile",
}
MISPLACED_ROOT_DOCS = {
    "ARCHITECTURE.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "GLOSSARY.md",
    "SPEC.md",
    "SPECS.md",
    "DESIGN.md",
    "ROADMAP.md",
}
SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*=\s*['\"]?[A-Za-z0-9_./+=-]{12,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
]


def git_output(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def is_git_repo(root: Path) -> bool:
    return git_output(root, ["rev-parse", "--is-inside-work-tree"]).returncode == 0


def tracked_files(root: Path) -> set[str]:
    result = git_output(root, ["ls-files"])
    if result.returncode != 0:
        return set()
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def gitignore_entries(root: Path) -> set[str]:
    path = root / ".gitignore"
    if not path.exists():
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def infer_project_type(root: Path, root_names: set[str]) -> str:
    if root_names & CODE_MANIFESTS or (root / "src").is_dir() or (root / "tests").is_dir():
        return "code"
    if (root / "wiki").is_dir() or (root / "raw").is_dir() or (root / "notes").is_dir():
        return "knowledge"
    if list(root.glob("*.md")) and not (root_names & CODE_MANIFESTS):
        return "knowledge"
    return "unknown"


def scan_env_example(root: Path) -> list[str]:
    path = root / ".env.example"
    if not path.exists():
        return []
    findings: list[str] = []
    for index, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if any(pattern.search(line) for pattern in SECRET_PATTERNS):
            findings.append(f".env.example:{index}")
    return findings


def build_report(root: Path) -> dict[str, Any]:
    root = root.resolve()
    if not root.is_dir():
        raise SystemExit(f"ERROR: not a directory: {root}")
    root_entries = [path for path in root.iterdir() if path.name != ".git"]
    root_names = {path.name for path in root_entries}
    git_repo = is_git_repo(root)
    tracked = tracked_files(root) if git_repo else set()
    ignored = gitignore_entries(root)
    project_type = infer_project_type(root, root_names)

    missing: list[str] = []
    if "AGENTS.md" not in root_names:
        missing.append("AGENTS.md")
    if "README.md" not in root_names:
        missing.append("README.md")
    if git_repo and ".gitignore" not in root_names:
        missing.append(".gitignore")
    if project_type == "code":
        if ".env.example" not in root_names:
            missing.append(".env.example")
        if not (root_names & CODE_MANIFESTS):
            missing.append("stack manifest")

    hygiene: list[str] = []
    if git_repo and ".gitignore" in root_names:
        for required in (".env", ".Codex/settings.local.json"):
            if required not in ignored:
                hygiene.append(f".gitignore missing {required}")
    for sensitive in (".env", ".Codex/settings.local.json"):
        if sensitive in tracked:
            hygiene.append(f"tracked local-only file: {sensitive}")
    for finding in scan_env_example(root):
        hygiene.append(f"possible secret value in {finding}")

    misplaced = sorted(name for name in root_names if name in MISPLACED_ROOT_DOCS)
    root_file_count = sum(1 for path in root_entries if path.is_file())
    sprawl = root_file_count > 12

    status = "pass"
    if missing or misplaced or hygiene or sprawl:
        status = "fail"

    return {
        "root": str(root),
        "project_type": project_type,
        "git_repo": git_repo,
        "status": status,
        "root_file_count": root_file_count,
        "missing": missing,
        "misplaced_root_docs": misplaced,
        "hygiene": hygiene,
        "sprawl": sprawl,
    }


def print_report(report: dict[str, Any]) -> None:
    print("REPO STRUCTURE CHECK")
    print(f"root: {report['root']}")
    print(f"project_type: {report['project_type']}")
    print(f"git_repo: {'yes' if report['git_repo'] else 'no'}")
    print(f"root_file_count: {report['root_file_count']}")
    print(f"status: {report['status'].upper()}")
    for key, title in (
        ("missing", "missing"),
        ("misplaced_root_docs", "misplaced_root_docs"),
        ("hygiene", "hygiene"),
    ):
        print(f"{title}:")
        values = report[key]
        if not values:
            print("  none")
        else:
            for value in values:
                print(f"  {value}")
    print(f"sprawl: {'yes' if report['sprawl'] else 'no'}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check root-file and local-settings hygiene.")
    parser.add_argument("root", nargs="?", default=".", help="repo root to inspect")
    parser.add_argument("--json", action="store_true", help="emit JSON report")
    parser.add_argument("--fail-on-drift", action="store_true", help="exit non-zero on fail status")
    args = parser.parse_args(argv)

    report = build_report(Path(args.root))
    if args.json:
        print(json.dumps(report, indent=2) + "\n")
    else:
        print_report(report)
    if args.fail_on_drift and report["status"] != "pass":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
