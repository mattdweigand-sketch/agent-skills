# agent-skill-repo

## What This Is

Portable agent skill library for reusable agent workflows.

## How To Use It

Copy all skills into the active skills directory:

```bash
cp -R skills/* ~/.agents/skills/
```

## Conventions

- Keep the repo small.
- Each skill lives under `skills/<skill-name>/`.
- Each skill's source of truth is its `SKILL.md`.
- Preserve bundled `references/`, `scripts/`, `agents/`, and other skill-local resources.
- Do not flatten skill folders.
- Do not add generated artifacts or local agent settings.

## Do Not Do Without Asking

- Do not publish secrets.
- Do not add cloud deployment automation.
- Do not add repo-specific test fixtures unless this becomes a test harness repo.
- Do not rewrite imported skills unless the user asks to modify that skill.
