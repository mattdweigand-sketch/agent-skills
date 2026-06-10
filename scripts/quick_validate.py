"""Quick stdlib-only checks for the shared skill repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SKILLS_DIR = "skills"
SKILL_FILE = "SKILL.md"
REQUIRED_FRONTMATTER = ("name", "description")
LOCAL_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9_.-])(?:\./)?((?:references|agents)/[A-Za-z0-9_./-]+)"
)


def _repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if (candidate / SKILLS_DIR).is_dir() and (candidate / "README.md").is_file():
            return candidate
    return current


def _skill_dirs(skills_root: Path) -> list[Path]:
    if not skills_root.is_dir():
        return []
    return sorted(path for path in skills_root.iterdir() if path.is_dir())


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse the top YAML-like frontmatter enough for repository checks."""
    if not text.startswith("---\n"):
        return {}

    end = text.find("\n---", 4)
    if end == -1:
        return {}

    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line or line.startswith((" ", "\t", "-")):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key:
            data[key] = value.strip()
    return data


def _readme_included_skills(readme_path: Path) -> set[str]:
    if not readme_path.is_file():
        return set()

    text = _read_text(readme_path)
    match = re.search(r"^## Included Skills\s*$", text, flags=re.MULTILINE)
    if not match:
        return set()

    following = text[match.end() :]
    next_section = re.search(r"^##\s+", following, flags=re.MULTILINE)
    section = following[: next_section.start()] if next_section else following
    skills: set[str] = set()
    for line in section.splitlines():
        match = re.match(r"^\|\s*`([^`|/]+)`\s*\|", line)
        if match:
            skills.add(match.group(1))
    return skills


def _explicit_local_paths(text: str) -> set[str]:
    paths: set[str] = set()
    for match in LOCAL_PATH_RE.finditer(text):
        path = match.group(1).rstrip(".,:;")
        if "*" in path:
            continue
        paths.add(path)
    return paths


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_dir = skill_dir.resolve()
    skill_file = skill_dir / SKILL_FILE

    if not skill_file.is_file():
        return [f"{skill_dir}: missing {SKILL_FILE}"]

    try:
        text = _read_text(skill_file)
    except OSError as exc:
        return [f"{skill_file}: could not read file: {exc}"]

    frontmatter = parse_frontmatter(text)
    for field in REQUIRED_FRONTMATTER:
        if not frontmatter.get(field):
            errors.append(f"{skill_file}: frontmatter missing {field!r}")

    frontmatter_name = frontmatter.get("name")
    if frontmatter_name and frontmatter_name != skill_dir.name:
        errors.append(
            f"{skill_file}: frontmatter name {frontmatter_name!r} "
            f"does not match folder {skill_dir.name!r}"
        )

    for local_path in sorted(_explicit_local_paths(text)):
        target = (skill_dir / local_path).resolve()
        try:
            target.relative_to(skill_dir)
        except ValueError:
            errors.append(f"{skill_file}: local path escapes skill folder: {local_path}")
            continue
        if not target.is_file():
            errors.append(f"{skill_file}: missing referenced local file {local_path}")

    return errors


def validate_repo(repo_root: Path) -> list[str]:
    errors: list[str] = []
    repo_root = repo_root.resolve()
    skills_root = repo_root / SKILLS_DIR
    skill_dirs = _skill_dirs(skills_root)

    if not skills_root.is_dir():
        return [f"{repo_root}: missing {SKILLS_DIR}/ directory"]

    if not skill_dirs:
        errors.append(f"{skills_root}: no skill folders found")

    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    readme_path = repo_root / "README.md"
    listed = _readme_included_skills(readme_path)
    folder_names = {path.name for path in skill_dirs}
    if not readme_path.is_file():
        errors.append(f"{readme_path}: missing README.md")
    elif not listed:
        errors.append(f"{readme_path}: missing or empty Included Skills section")
    else:
        for missing in sorted(folder_names - listed):
            errors.append(f"{readme_path}: Included Skills missing {missing!r}")
        for extra in sorted(listed - folder_names):
            errors.append(f"{readme_path}: Included Skills lists unknown skill {extra!r}")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate shared skill folders and README index."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Repository root or a single skills/<name> folder. Defaults to cwd.",
    )
    args = parser.parse_args(argv)

    path = Path(args.path).resolve()
    if path.name == SKILLS_DIR or (path / SKILLS_DIR).is_dir():
        errors = validate_repo(_repo_root(path))
    elif (path / SKILL_FILE).is_file():
        errors = validate_skill(path)
    else:
        errors = validate_repo(_repo_root(path))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
