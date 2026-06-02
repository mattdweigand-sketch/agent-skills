# Agent Skill Repo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Portable agent skill library for agentic repo work, eval loops, research, writing, and project hygiene. Works with Codex, Claude Code, and other AGENTS-aware tools.

## Included Skills

| Skill | Use |
|---|---|
| `autoresearch` | Optimize an editable surface against a frozen labeled test set. |
| `code-project-structure` | Apply structural rules and scaffold new projects. |
| `consolidate-memory` | Consolidate memory files and prune stale facts. |
| `humanizer` | Remove AI writing patterns and improve clarity. |
| `judgment-audit` | Audit subjective eval criteria and decide which deserve LLM judges, deterministic checks, manual review, or removal. |
| `karpathy-guidelines` | Keep coding work simple, surgical, and verified. |
| `linkedin-post` | Draft LinkedIn posts in a defined voice and structure. |
| `n-agentic-harnesses` | Design and evaluate agentic harnesses. |
| `parallel-refactor` | Coordinate multi-agent refactors through worktrees and review gates. |
| `project-audit` | Audit repo structure against project rules. |
| `ralf-loop` | Run local smoke/eval loops until `pass`, `needs-human`, or `blocked`. |
| `research-synthesis` | Turn source sets into decision-grade synthesis. |
| `skill-creator-v3` | Create, improve, evaluate, and package skills. |
| `source-command-context-audit` | Route the migrated context-audit command. |
| `weekly-signal-diff-ai` | Produce weekly structural diffs on the AI ecosystem. |

## Install

Copy all skills into your personal skills directory:

```bash
cp -R skills/* ~/.agents/skills/
```

Or install one skill:

```bash
cp -R skills/ralf-loop ~/.agents/skills/ralf-loop
```

## Example Triggers

Ask Codex:

```text
run a RALF loop on this repo
```

or:

```text
run the smoke test until it converges
```

```text
audit this project structure
```

```text
run autoresearch on this retrieval config
```

```text
humanize this README
```

## Library Defaults

- Local-first. No cloud deploys unless explicitly authorized.
- Frozen gates before iterative edits.
- Negative controls for retrieval, AI, parser, and workflow tests.
- Small, surgical changes.
- Evidence and source quality over confident prose.

## License

[MIT](LICENSE)
