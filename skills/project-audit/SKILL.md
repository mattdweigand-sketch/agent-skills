---
name: project-audit
description: Audit code projects against the structural rules in the code-project-structure skill. Reports which projects conform, which don't, and what's missing. Use when the user says "audit my projects", "check project structure", "are my projects conforming", "/audit", or wants to migrate an external project into ~/Code/.
metadata:
  version: "2.0"
  category: "tooling"
  tags: ["audit", "project-structure", "quality"]
---

# project-audit

Reports drift, does not auto-fix. The user reads the report and decides which fixes to apply.

## When to invoke
- "audit my projects" / "check structure" / "which projects are conforming"
- "I want to migrate `~/somewhere/foo` into Code" — audit it first, then help move it
- After moving an external project into `~/Code/`, audit before working in it

## Source of truth
The rules live in `~/Code/AGENTS.md`. **Read that file first** every time this skill runs — the rules can change. Do not bake the rule list into this skill.

## Procedure

### Step 1: Load current rules
Read `~/Code/AGENTS.md`. Extract the structural requirements (required files, forbidden files at root, root-count target, AGENTS.md size cap, gitignore requirements).

### Step 2: Determine scope
- If user pointed at a specific project → audit just that one
- If cwd is inside a `~/Code/<project>/` → audit just that project
- Otherwise → audit every direct child of `~/Code/` except `_template/` and any dotfiles

### Step 3: Check each project
For each project, check:

**Required at root** (per the rules in `~/Code/AGENTS.md`):
- `AGENTS.md` present, under ~200 lines
- `README.md` present
- `.gitignore` present and includes `.Codex/settings.local.json` and `.env`
- `.env.example` present
- A stack manifest at root (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, or equivalent) — flag missing but allow if the project is genuinely not code (e.g. notes-only)
- `.Codex/settings.json` present

**Forbidden at root:**
- `ARCHITECTURE.md`, `CONTRIBUTING.md`, `CHANGELOG.md` (belong in `docs/`)
- Domain glossaries, product specs, context files (belong in `docs/context/`)
- Stray Markdown files beyond `AGENTS.md` and `README.md`

**Hygiene:**
- Root file count between 5 and 7 (rough — not a hard fail, just flag if >10)
- `.Codex/settings.local.json` is **not committed** (check via `git ls-files` if repo is initialized)
- No secrets in `.env.example` or `settings.json`

### Step 4: Produce a report

Format the output as a single table with one row per project:

| Project | Status | Missing | Misplaced | Notes |
|---|---|---|---|---|
| open-brain | ✓ pass | — | — | — |
| weekly-signal-diff | ✗ fail | AGENTS.md, .env.example | ARCHITECTURE.md at root | AGENTS.md is 340 lines |

After the table, for any failing project, give a one-block migration plan:

```
weekly-signal-diff
  - Add AGENTS.md (template at ~/Code/_template/AGENTS.md)
  - Add .env.example
  - Move ARCHITECTURE.md → docs/architecture.md
  - Trim AGENTS.md from 340 → ~200 lines (it's read every turn — bloat tax)
```

### Step 5: Offer next steps
Ask whether the user wants you to:
1. Apply the fixes for one specific project (you do them, they review)
2. Apply fixes across all failing projects (riskier — confirm scope first)
3. Just leave the report and act on it themselves later

Never apply fixes without explicit confirmation. Migration touches files the user may have hand-curated.

## Migration of external projects (`~/somewhere/foo` → `~/Code/foo`)

When the user wants to bring an external project in:

1. Confirm the target name and that `~/Code/<name>/` doesn't already exist
2. Move it: `mv ~/somewhere/foo ~/Code/foo` (do not copy — leaves orphan)
3. Run this skill against `~/Code/foo`
4. Walk the user through the migration plan from the report

Do not auto-move without confirmation. Moving a project is reversible but disruptive (breaks any tooling pointing at the old path).

## What this skill does NOT do
- Does not modify `~/Code/AGENTS.md` (the rules) — those are user-curated
- Does not auto-fix without confirmation
- Does not delete files
- Does not run on directories outside `~/Code/` unless the user explicitly points at one

## Failure modes to avoid
- **Don't enforce rules the user hasn't actually written.** Read `~/Code/AGENTS.md` and only check what's there. If the rules are silent on something, don't invent.
- **Don't fail a project for being a different kind of artifact.** A docs-only project legitimately has no `package.json`. Flag, but qualify.
- **Don't run on `_template/`** — that's the source of truth, not a project.
