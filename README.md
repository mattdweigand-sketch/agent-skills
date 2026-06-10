# Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Portable skill library for repo work, eval loops, research, writing, and agent
workflow hygiene. These skills are written to work across Codex, Claude Code,
Cursor, and other AGENTS-aware tools.

## Included Skills

Use this table as a routing guide. Each skill has its full workflow in
`skills/<skill-name>/SKILL.md`.

| Skill | What it does | Use when |
|---|---|---|
| `autoresearch` | Runs a measure, edit, re-measure loop against a frozen test set and keeps only changes that improve the score. | You have a prompt, retrieval config, template, ranking rule, or other editable surface with a repeatable metric. |
| `code-project-structure` | Defines how code and knowledge projects under `~/Code/` should be scaffolded and organized. | You are starting a new project, moving files, editing project instructions, or checking whether a project root is shaped correctly. |
| `consolidate-memory` | Reviews memory files, merges duplicates, fixes stale time references, and prunes low-value entries. | The memory layer has grown noisy, overlapping, or out of date and needs a cleanup pass. |
| `criteria` | Audits rubric items and subjective checks, then recommends deterministic checks, LLM judges, manual review, or deletion. | You have eval criteria and need to decide which ones are worth automating. |
| `grade` | Checks whether a system that captures judgment also grades that judgment against real outcomes. | You are reviewing an eval, scoring, recommendation, sales-intelligence, or agent system that may be accumulating unverified patterns. |
| `humanizer` | Edits prose to remove AI writing tells and fix clarity problems while preserving meaning and register. | You are revising emails, docs, posts, READMEs, specs, or reports that sound generic, inflated, or unclear. |
| `karpathy-guidelines` | Keeps coding work simple, scoped, assumption-aware, and tied to verifiable success criteria. | You are implementing, reviewing, or refactoring code and want guardrails against overengineering or hidden assumptions. |
| `linkedin-post` | Drafts a 150 to 300 word LinkedIn post with a hook, one idea per paragraph, and a concrete close. | You want a personal-feed post, not a DM, connection request, email, or campaign sequence. |
| `n-agentic-harnesses` | Designs or evaluates the orchestration layer around AI tools, agents, permissions, memory, state, and evals. | You are building or reviewing an agentic product, copilot, assistant, workflow runner, or tool-using harness. |
| `parallel-refactor` | Splits a large refactor into isolated worktrees, dispatches specialist agents, and reviews the combined result. | A repo change is large enough for multiple independent branches and the merge/review overhead is justified. |
| `project-audit` | Checks projects against the structure rules from `code-project-structure` and reports drift without auto-fixing. | You want to audit one project, all projects under `~/Code/`, or a repo you are migrating into that structure. |
| `ralf-loop` | Runs a local hardening loop: execute a smoke test or workflow, diagnose failure, make one bounded fix, rerun, and stop at a clear state. | You have a command or workflow that can be repeated until it passes, needs a human decision, or is blocked. |
| `research-synthesis` | Turns a defined source set into findings, contradictions, confidence levels, gaps, and next questions. | You have articles, notes, transcripts, reports, or research packets and need a decision-grade brief. |
| `run-kit` | Shapes AI agent work into run specs, decides whether to steer or dispatch, and audits returned work. | You are managing an agent assignment and need clearer scope, proof, review burden, or cross-checking. |
| `skill-creator-v3` | Creates, improves, evaluates, and packages skills, including trigger tuning and optional evals. | You want to turn a repeatable workflow into a reusable skill or sharpen an existing skill. |
| `scope` | Adds a short missing-authority gate before durable state, external output, or file/config changes. | A task could write persistent state or send something externally, and the source of authority, boundary, data flow, or rollback path is unclear. |
| `source-command-context-audit` | Audits startup context, command wrappers, skill routing, memory summaries, and settings for bloat or dead routes. | You ask for `context-audit`, token optimization, settings cleanup, or why an agent session is loading too much context. |
| `skill-tune` | Audits skills, prompts, command wrappers, and instruction files for prompt technical debt. | You want to shorten, de-duplicate, validate, or refactor prompt artifacts without turning them into new doctrine. |
| `weekly-signal-diff-ai` | Produces a weekly structural diff of the AI ecosystem with source-backed shifts and user-specific implications. | You want to know what changed in AI this week, what matters structurally, and what to watch next. |

## Install

Copy all skills into the skill directory used by your agent:

```bash
cp -R skills/* ~/.agents/skills/
```

For Codex, use:

```bash
cp -R skills/* ~/.codex/skills/
```

Install one skill by copying only that folder:

```bash
cp -R skills/ralf-loop ~/.agents/skills/ralf-loop
```

## Example Triggers

Ask your agent:

- `run a RALF loop on this repo`
- `run the smoke test until it converges`
- `audit this project structure`
- `run autoresearch on this retrieval config`
- `humanize this README`
- `use skill-tune to audit this SKILL.md`
- `turn these sources into a research synthesis`
- `run my weekly AI signal diff`

## Library Defaults

- Local-first. No cloud deploys unless explicitly authorized.
- Frozen gates before iterative edits.
- Negative controls for retrieval, AI, parser, and workflow tests.
- Small, surgical changes.
- Evidence and source quality over confident prose.

## License

[MIT](LICENSE)
