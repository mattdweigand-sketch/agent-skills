# Agent Skill Repo

Portable Codex skill library for agentic repo work, eval loops, research, writing cleanup, and project hygiene.

## Included Skills

| Skill | Use |
|---|---|
| `ralf-loop` | Run local smoke/eval loops until `pass`, `needs-human`, or `blocked`. |
| `autoresearch` | Optimize an editable surface against a frozen labeled test set. |
| `karpathy-guidelines` | Keep coding work simple, surgical, and verified. |
| `n-agentic-harnesses` | Design and evaluate agentic harnesses. |
| `parallel-refactor` | Coordinate multi-agent refactors through worktrees and review gates. |
| `project-audit` | Audit repo structure against project rules. |
| `source-command-context-audit` | Route the migrated context-audit command. |
| `research-synthesis` | Turn source sets into decision-grade synthesis. |
| `weekly-signal-diff-ai` | Produce weekly structural diffs on the AI ecosystem. |
| `humanizer` | Remove AI writing patterns and improve clarity. |
| `consolidate-memory` | Consolidate memory files and prune stale facts. |

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
