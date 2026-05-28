# ralf-loop-skill

## What This Is

Small source repo for the reusable `ralf-loop` Codex skill.

## How To Use It

Copy `ralf-loop/` into the active skills directory:

```bash
cp -R ralf-loop ~/.agents/skills/ralf-loop
```

## Conventions

- Keep the repo small.
- The skill source of truth is `ralf-loop/SKILL.md`.
- UI metadata lives at `ralf-loop/agents/openai.yaml`.
- Do not add generated artifacts or local Codex settings.

## Do Not Do Without Asking

- Do not publish secrets.
- Do not add cloud deployment automation.
- Do not add repo-specific test fixtures unless this becomes a test harness repo.
