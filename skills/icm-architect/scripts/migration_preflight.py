#!/usr/bin/env python3
"""Read-only checks for one file/directory copy; never authorizes removal."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import unicodedata


def folded_name(name: str) -> str:
    """Conservatively catch case and Unicode-normalization collisions."""
    return unicodedata.normalize("NFC", name).casefold()


def check_path_components(path: Path, destination: bool) -> None:
    """Reject symlinks and alternate destination spellings before traversal."""
    current = Path(path.anchor)
    for part in path.parts[1:]:
        if destination and current.is_dir():
            alternatives = [
                item.name for item in current.iterdir()
                if folded_name(item.name) == folded_name(part) and item.name != part
            ]
            if alternatives:
                raise ValueError(f"Destination name collision at {current / part}: {alternatives}")
        current /= part
        if current.is_symlink():
            raise ValueError(f"Symlink path component is unsupported: {current}")
        if current.exists() and current != path and not current.is_dir():
            raise ValueError(f"Path ancestor is not a directory: {current}")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def copy_inventory(root: Path) -> dict:
    """Record exact paths and bytes, including empty directories."""
    inventory = {}
    pending = [root]
    while pending:
        path = pending.pop()
        mode = path.lstat().st_mode
        relative = path.relative_to(root).as_posix()
        if stat.S_ISDIR(mode):
            inventory[relative] = {"type": "directory"}
            children = sorted(path.iterdir())
            names = {}
            for child in children:
                folded = folded_name(child.name)
                if folded in names:
                    raise ValueError(f"Case-folded name collision: {names[folded]} and {child}")
                names[folded] = child
            pending.extend(children)
        elif stat.S_ISREG(mode):
            inventory[relative] = {"type": "file", "sha256": file_sha256(path)}
        else:
            raise ValueError(f"Symlink or special file is unsupported: {path}")
    return inventory


def check_migration(source: Path, destination: Path, verify: bool = False) -> dict:
    """Check one exact copy target, returning JSON-ready evidence."""
    # Do not resolve paths: resolving would hide symlinks before inspection.
    result = {
        "source": str(source), "destination": str(destination),
        "mode": "verify" if verify else "preflight", "passed": False,
    }
    try:
        if ".." in source.parts or ".." in destination.parts:
            raise ValueError("Use explicit paths without parent traversal (..)")
        source = Path(os.path.abspath(source))
        destination = Path(os.path.abspath(destination))
        result.update(source=str(source), destination=str(destination))
        check_path_components(source, destination=False)
        check_path_components(destination, destination=True)
        if source == destination or source in destination.parents or destination in source.parents:
            raise ValueError("Source and destination must be distinct, non-overlapping paths")
        source_inventory = copy_inventory(source)
        result["source_files"] = sum(v["type"] == "file" for v in source_inventory.values())
        if not verify:
            if destination.exists():
                raise ValueError(f"Destination already exists: {destination}")
            result["passed"] = True
            return result
        destination_inventory = copy_inventory(destination)
        result["destination_files"] = sum(v["type"] == "file" for v in destination_inventory.values())
        result["missing"] = sorted(source_inventory.keys() - destination_inventory.keys())
        result["extra"] = sorted(destination_inventory.keys() - source_inventory.keys())
        result["changed"] = sorted(
            key for key in source_inventory.keys() & destination_inventory.keys()
            if source_inventory[key] != destination_inventory[key]
        )
        result["passed"] = not any(result[key] for key in ("missing", "extra", "changed"))
    except (OSError, ValueError) as error:
        result["error"] = str(error)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--verify", action="store_true", help="Verify an unchanged completed copy")
    args = parser.parse_args()
    result = check_migration(args.source, args.destination, args.verify)
    print(json.dumps(result, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
