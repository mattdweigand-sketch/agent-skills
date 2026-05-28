---
name: n-agentic-harnesses
description: >-
  Design, evaluate, and improve agentic harnesses — the orchestration layer
  around LLM-powered tools, agents, assistants, copilots, workflow runtimes,
  and AI-driven product features. Use this skill whenever the user mentions
  building an agentic system, structuring tool use, adding permissions or
  approval gates, designing multi-step AI workflows, managing context windows
  or memory, making agents durable or resumable, evaluating or pressure-testing
  an existing harness, planning phased implementation for an AI product,
  reviewing agent architecture, improving agent UX or observability, or asking
  how to know if their harness is actually good. Also use when the user
  describes problems that imply harness gaps — like agents doing unexpected
  things, context getting stale, sessions not surviving crashes, tools running
  without permission, or costs spiraling — even if they do not use the word
  "harness."
version: "2.0"
category: "agentic-systems"
tags: ["harness", "architecture", "multi-agent", "evaluation", "design"]
---

# N Agentic Harnesses

Router for designing, building, and evaluating agentic harnesses. Read only the files you need.

**Default posture:** Lean, solo-maintainable architecture. Single-agent design unless constraints justify more. Require an evaluation plan even for greenfield builds. Explicit system boundaries and permission policy over prompt cleverness.

## Step 0: Gather Context

| Request Type | Confirm |
|---|---|
| Design | Product/system served, agent actions, users, constraints (solo dev / team / stack / timeline) |
| Evaluation | Access to codebase, AGENTS.md, settings, skills, hooks, or architecture docs |
| Vague | Ask 1-2 clarifying questions, then pick a mode |

## Step 1: Classify the Request

| Mode | Use When | Default Reads |
|------|----------|---------------|
| `design` | New harness, major rebuild, architecture, MVP, or implementation sequencing | 01, 02, 08 |
| `evaluation` | Existing harness — gaps, risks, missing primitives, UX/ops upgrades | 01, 09 |
| `design + evaluation` | Target architecture + comparison to current state, acceptance criteria | 01, 02, 08, 09 |

## Step 2: Classify the Product Shape

- code agent / chat assistant / workflow orchestrator / internal copilot / embedded AI product feature / hybrid system

Pick the closest shape and state the assumption if ambiguous.

## Step 3: Read the Smallest Useful Reference Set

| File | Read When |
|------|-----------|
| `references/01-principles-and-solo-dev-defaults.md` | Almost every request — defines default decision posture |
| `references/02-harness-shapes-and-architecture.md` | System shape, boundaries, lifecycle, transports, deployment |
| `references/03-tools-execution-and-permissions.md` | Tool registries, tool calling, approval gates, sandboxes, trust tiers |
| `references/04-state-sessions-and-durability.md` | Sessions, resumability, retries, idempotency, approval waits, long-running work |
| `references/05-context-memory-and-evaluation.md` | Context windows, retrieval, memory, provenance, evals, replay tests |
| `references/06-agents-and-extensibility.md` | Multi-agent design, plugins, hooks, skills, extension surfaces |
| `references/07-ux-observability-and-operations.md` | Streaming UX, health checks, logs, analytics, budgets, supportability |
| `references/08-design-and-build-playbook.md` | Build-ready plan from idea to implementation |
| `references/09-evaluation-and-improvement-playbook.md` | Findings, missing primitives, upgrade priorities, acceptance tests |
| `references/10-example-requests-and-output-patterns.md` | Prompt examples or response structure examples |
| `references/11-codex-translation-notes.md` | Adapting to Codex or mapping between environments |

Do not rely on reference-to-reference chains. This file is the index.

## Output Contract

**design:** recommended shape, core primitives, MVP boundary, phased plan, verification criteria
**evaluation:** findings by severity, missing/weak primitives, UX/ops gaps, upgrade path, tests
**design + evaluation:** target architecture, comparison vs current, phases, acceptance criteria, eval plan

## Operating Rules

- Convert vague ambitions into concrete harness primitives.
- Push back on unnecessary complexity.
- Treat workflow state, permissions, context assembly, and evaluation as first-class architecture.
- For evaluation: findings first, improvement sequence second.
- For design: include how the design will be tested before calling it done.

## Final Check Before Responding

Before writing the response, verify:

- [ ] Request was classified — mode is explicitly chosen (design / evaluation / design+evaluation)
- [ ] Multi-agent was not recommended unless the user's constraints make single-agent insufficient
- [ ] Eval plan is present — design responses include acceptance criteria; evaluation responses include upgrade sequencing
