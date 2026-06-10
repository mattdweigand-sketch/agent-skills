---
name: code-project-structure
description: Structural rules and scaffolding workflow for projects under ~/Code/. Source of truth for what belongs at a project root, where files go, how AGENTS.md is shaped, and how new projects get scaffolded. Invoke when starting a new project under ~/Code/, creating or moving files inside a project under ~/Code/, editing a project's AGENTS.md, modifying .Codex/settings.json or .Codex/settings.local.json, or auditing project structure. Distinguishes code projects from knowledge projects (wikis, corpus stores, markdown-only) and applies different rules to each.
metadata:
  version: "2.0"
  category: "tooling"
  tags: ["project-structure", "scaffolding", "Codex-md", "settings"]
---

# Code project structure

Source of truth for projects under `~/Code/`. Rules + scaffolding in one place.

## Project types

Two shapes of project live under `~/Code/`:
- **Code projects** — source, tests, build steps, or runtime config. All rules apply.
- **Knowledge projects** — personal wikis, corpus stores, content collections, markdown-only. Only universal rules apply.

Rules marked **(code)** apply only to code projects. The project's own `AGENTS.md` should declare its type if it isn't obvious.

## Starting a new project

```bash
mkdir ~/Code/your-project && cd ~/Code/your-project && git init
```

Then write the files below. For knowledge projects, stop after `AGENTS.md`. For cloned repos, inherit upstream layout.

→ Starter templates for AGENTS.md, .Codex/settings.json, and .gitignore: [references/templates.md](references/templates.md)

## Required at every code project root

- `AGENTS.md` — project brain, kept under ~200 lines (universal)
- `README.md` — human-facing intro (universal)
- `.gitignore` — required if git-tracked; must include `.Codex/settings.local.json` and `.env`
- `.env.example` — **(code)** template for env vars; `.env` itself is never committed
- One stack manifest — **(code)** `package.json`, `pyproject.toml`, `Cargo.toml`, or `go.mod`
- One lockfile — **(code)** committed alongside the manifest

5-7 files at root for code projects; fewer is fine for knowledge projects.

## Where things go (not at root)

| Content | Location |
|---|---|
| Architecture, ADRs, glossaries, specs | `docs/` |
| Project-specific Codex config | `.Codex/` |
| Slash commands for this repo only | `.Codex/commands/` |
| Subagents for this repo only | `.Codex/agents/` |
| Code | `src/` |
| Tests | `tests/` |
| Automation | `scripts/` |

`ARCHITECTURE.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, domain glossaries, and product specs do **not** belong at the root.

## AGENTS.md discipline

- One `AGENTS.md` at project root. Add one inside a subdirectory for per-subsystem guidance.
- Treat it like a prompt, not documentation. Bloat costs tokens every turn.
- Sections: what this is / how to run it / non-obvious conventions / never-do-without-asking / pointers to deeper context.

## Permissions discipline

- `.Codex/settings.json` — committed, shared. Safe-by-default rules only.
- `.Codex/settings.local.json` — gitignored. Personal overrides, expanded permissions.
- Never commit `settings.local.json`. Never put secrets in either file.

## What to skip on day one

Don't pre-fill `commands/`, `agents/`, or ADRs. Add them when friction justifies them.

**Minimum viable project:**
- **Code:** `AGENTS.md` + `README.md` + `.Codex/settings.json` + stack manifest
- **Knowledge:** `AGENTS.md` (that's enough if it orients well)

## Skill vs command vs subagent

- Reusable across projects → **skill** in `~/.Codex/skills/`
- This repo only → **slash command** in `.Codex/commands/`
