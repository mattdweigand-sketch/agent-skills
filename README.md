# Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Portable skill library for repo work, eval loops, research, writing, and agent
workflow hygiene. These skills are written to work across Codex, Claude Code,
Cursor, and other AGENTS-aware tools.

## Included Skills

Each skill keeps its full workflow in `skills/<skill-name>/SKILL.md`.

| Skill | Description |
|---|---|
| `60-30-10` | Evaluate where a project keeps its judgment, and whether the allocation matches the durable shape: mostly owned data, partly deterministic code, only a thin layer of live model. |
| `autoresearch` | Improves a prompt, config, or workflow by testing one change at a time against a fixed score. |
| `context-window-audit` | Finds startup context, settings, wrappers, and memory entries that waste context-window space. |
| `cyborg-check` | Audits whether a judgment system closes the loop between captured patterns and real outcomes, or is spreading unverified judgment. |
| `humanizer` | Rewrites prose so it sounds clearer, more natural, and less AI-generated. |
| `karpathy-guidelines` | Keeps coding work simple, scoped, and easy to verify. |
| `n-agentic-harnesses` | Helps design or review the system around AI agents, tools, memory, permissions, and evals. |
| `parallel-refactor` | Coordinates a large refactor across multiple isolated worktrees. |
| `ralf-loop` | Runs a repeatable test-and-fix loop until the work passes, blocks, or needs a decision. |
| `repo-structure-audit` | Defines and audits a clean repo layout for code and knowledge projects. |
| `research-synthesis` | Turns a source set into clear findings, contradictions, gaps, and next questions. |
| `quality-check-eval` | Sorts AI output quality checks into four buckets: automate in code, judge with an LLM, keep for human review, or remove. |
| `run-kit` | Turns fuzzy agent work into a scoped run, then helps review or cross-check the result. |
| `runtime-guard` | Prevents an agent from editing or publishing without clearly defined authority, boundaries, stop conditions, or rollback. |
| `skill-creator-v3` | Creates, improves, tests, and packages reusable skills. |
| `skill-tune` | Audit or refactor a skill or prompt artifact for prompt technical debt. |
| `weekly-signal-diff-ai` | Summarizes what structurally changed in AI this week and why it matters. |

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

## License

[MIT](LICENSE)
