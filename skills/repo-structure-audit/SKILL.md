---
name: repo-structure-audit
description: "Define and audit repo structure for code and knowledge projects. Use when starting a repo, moving a project into a standard layout, editing AGENTS.md or agent settings, checking root-file sprawl, auditing projects under Code, or asking whether a repo is organized correctly."
metadata:
  version: "2.0"
  category: "tooling"
  tags: ["repo-structure", "audit", "scaffolding", "project-hygiene"]
---

# Repo Structure Audit

One skill owns both sides of the workflow: the repo structure standard and the
audit against that standard. Use it to scaffold, inspect, and clean up project
shape without turning root docs into prompt bloat.

## Contract

**Produces:** a repo-structure report, a migration plan, or a small scaffold.

**Does not produce:** automatic file moves, deletes, broad rewrites, or changes
to user-curated structure rules unless the user explicitly asks.

## Project Types

- **Code project:** source, tests, build steps, runtime config, or deployable
  software. Apply the full standard.
- **Knowledge project:** wiki, corpus, notes, markdown collection, or research
  store. Apply only the universal rules.

If the project type is unclear, infer from the files and state the assumption.

## Standard Shape

Root should stay small and predictable.

Universal root files:

- `AGENTS.md` - agent operating map, kept short enough to load every session
- `README.md` - human-facing intro
- `.gitignore` - if git-tracked; must ignore `.Codex/settings.local.json` and `.env`

Code-project root files:

- `.env.example` - template only; never commit `.env`
- one stack manifest - `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, or equivalent
- one lockfile, committed next to the manifest when the stack uses one
- optional `.Codex/settings.json` for shared, safe-by-default agent settings

Put deeper material outside the root:

| Content | Location |
|---|---|
| Architecture, ADRs, specs, glossaries | `docs/` |
| Project-specific agent config | `.Codex/` |
| Repo-local commands | `.Codex/commands/` |
| Repo-local subagents | `.Codex/agents/` |
| Source code | `src/` |
| Tests | `tests/` |
| Automation | `scripts/` |

Avoid root sprawl: `ARCHITECTURE.md`, `CONTRIBUTING.md`, `CHANGELOG.md`,
domain glossaries, product specs, and context files usually belong in `docs/`.

## AGENTS.md Discipline

- Use one root `AGENTS.md`; add nested `AGENTS.md` only for real subsystem differences.
- Treat it like startup context, not a complete manual.
- Include: what this is, how to run it, non-obvious conventions, approval
  boundaries, and pointers to deeper docs.
- Keep bulky examples, architecture notes, and reference material out of startup context.

## Audit Procedure

1. Determine scope.
   - If the user points at a repo, audit that repo.
   - If the current directory is inside a project, audit that project.
   - If the user asks to audit projects under `~/Code`, audit direct child
     projects and skip templates/dotfiles.

2. Inventory the root.
   - Required files present or missing
   - Misplaced root files that belong in `docs/`
   - Agent config files and local settings hygiene
   - Root file count, flagging obvious sprawl rather than enforcing a hard quota

3. Check safety.
   - `.env` and `.Codex/settings.local.json` are not tracked
   - no secrets appear in `.env.example` or shared settings
   - no destructive moves or deletes are proposed without approval

4. Report drift.

Use this table:

| Project | Status | Missing | Misplaced | Notes |
|---|---|---|---|---|
| example | pass/fail | ... | ... | ... |

For each failing project, add a short migration plan:

```text
example
  - Add AGENTS.md from the starter template.
  - Move ARCHITECTURE.md to docs/architecture.md.
  - Add .env.example.
  - Trim AGENTS.md if it has become a manual instead of a startup map.
```

5. Ask before applying fixes.
   - Applying fixes to one named project is usually fine after confirmation.
   - Applying fixes across many projects needs explicit scope.
   - Moving an external project into `~/Code` also needs confirmation.

## Scaffolding

When creating a new project, start minimal:

- Code: `AGENTS.md`, `README.md`, `.gitignore`, stack manifest, optional
  `.Codex/settings.json`
- Knowledge: `AGENTS.md` and `README.md` if useful

Do not pre-fill commands, subagents, ADRs, or elaborate docs until friction
justifies them.

Starter templates live in `references/templates.md`.
