#!/usr/bin/env python3
"""Preflight checks for the parallel-refactor skill.

Reports dirty working-tree files and, when planned files are supplied, files
where uncommitted user work overlaps a planned builder partition.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_git(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def git_root(root: Path) -> Path:
    result = run_git(root, ["rev-parse", "--show-toplevel"])
    if result.returncode != 0:
        raise SystemExit(f"ERROR: not a git repository: {root}")
    return Path(result.stdout.strip()).resolve()


def dirty_paths(root: Path) -> set[str]:
    result = run_git(root, ["status", "--porcelain=v1", "-uall"])
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or "ERROR: git status failed")

    paths: set[str] = set()
    for line in result.stdout.splitlines():
        if not line:
            continue
        path = line[3:]
        if " -> " in path:
            old_path, new_path = path.split(" -> ", 1)
            paths.add(normalize_path(old_path))
            paths.add(normalize_path(new_path))
        else:
            paths.add(normalize_path(path))
    return paths


def normalize_path(value: str) -> str:
    return value.strip().replace("\\", "/").lstrip("./")


def load_planned_files(args: argparse.Namespace) -> set[str]:
    planned = {normalize_path(path) for path in args.planned_file}
    for list_path in args.planned_files_from:
        source = Path(list_path)
        try:
            lines = source.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            raise SystemExit(f"ERROR: cannot read planned files from {source}: {exc}") from exc
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                planned.add(normalize_path(stripped))
    return {path for path in planned if path}


def print_list(title: str, values: set[str]) -> None:
    print(f"{title}:")
    if not values:
        print("  none")
        return
    for value in sorted(values):
        print(f"  {value}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check dirty-tree and planned-file collisions before a parallel refactor."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="repository root or a path inside it (default: cwd)",
    )
    parser.add_argument(
        "--planned-file",
        action="append",
        default=[],
        help="file path a builder partition is expected to touch; repeat as needed",
    )
    parser.add_argument(
        "--planned-files-from",
        action="append",
        default=[],
        metavar="PATH",
        help="newline-delimited file containing planned builder paths",
    )
    parser.add_argument(
        "--fail-on-risk",
        action="store_true",
        help="exit non-zero when the tree is dirty or planned-file collisions exist",
    )
    args = parser.parse_args(argv)

    root = git_root(Path(args.root).resolve())
    dirty = dirty_paths(root)
    planned = load_planned_files(args)
    collisions = dirty & planned if planned else set()

    print("PARALLEL REFACTOR PREFLIGHT")
    print(f"root: {root}")
    print(f"dirty_tree: {'yes' if dirty else 'no'}")
    print(f"planned_file_count: {len(planned)}")
    print_list("dirty_files", dirty)
    if planned:
        print_list("planned_dirty_collisions", collisions)
    else:
        print("planned_dirty_collisions: not checked (no planned files supplied)")

    if collisions:
        print("status: COLLISION")
    elif dirty:
        print("status: DIRTY_TREE")
    else:
        print("status: CLEAN")

    if args.fail_on_risk and (dirty or collisions):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
