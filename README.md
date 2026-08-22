# Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Portable skill library for architecture, code quality, prompt maintenance,
research, and multi-agent workflows. These skills work across Codex, Claude
Code, Cursor, and other AGENTS-aware tools.

## Included Skills

Each skill keeps its full workflow in `skills/<skill-name>/SKILL.md`.

| Skill | Description |
|---|---|
| `60-30-10` | Evaluate whether load-bearing judgment is routed to owned data, deterministic code, or prompt-model work. |
| `icm-architect` | Designs processes and knowledge as walkable folder-based workspaces, or restructures existing folders to follow ICM conventions. |
| `karpathy-guidelines` | Keeps coding work simple, scoped, and easy to verify. |
| `skill-tune` | Audit or refactor a skill or prompt artifact for prompt technical debt. |
| `swarm` | Invocation-only workflow for turning a bounded task into a verified planner, worker, checker, and reviewer swarm. |
| `weekly-signal-diff-ai` | Summarizes what structurally changed in AI this week and why it matters. |
| `write-discoverable-code` | Writes and reviews source code with distinctive names and precise public APIs so coding agents can find and use it efficiently. |

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
cp -R skills/icm-architect ~/.agents/skills/icm-architect
```

## License

[MIT](LICENSE)
