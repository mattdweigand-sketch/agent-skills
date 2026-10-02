---
name: icm-architect
description: "Audit, build, or restructure a repository using the Interpretable Context Methodology framework."
metadata:
  adaptation: 'Core ICM with AGENTS.md and explicit file roles from the author walkthroughs'
  last_reviewed: '2026-10-01'
---

# ICM Architect

Read [conventions](references/conventions.md). Use `AGENTS.md` for entry files. This package contains the core framework, not the original example repository.

Use the exact target the user names and identify the version inspected. Distinguish a single workspace from a collection; add folders for actual responsibilities, not to copy an example's shape.

## What each Markdown file contains

| File | Responsibility |
|---|---|
| `AGENTS.md` | The map: what the workspace does, what lives where, and where to go for each job. |
| Workspace `CONTEXT.md` | The pipeline: one table naming each stage, its command or trigger, output artifact, and human check, with a route to its contract. |
| Stage `CONTEXT.md` | The contract: Input (what it reads), Do (the job), Output (what it writes), and Human check (what is reviewed before continuing). |

The stage template names these sections Inputs, Process, Outputs, and Checkpoints. Audit is the agent's quality check. For a stage without human review, state None and why; do not add an approval pause.

## Audit

Keep reviews read-only unless changes are requested. Inspect the target against the [validation checklist](references/validation.md). Report gaps with file evidence and distinguish verified findings from untested behavior.

## Build or restructure

Use the [templates](references/templates.md) and the original builder sequence:

1. Discover the workflow's inputs, outputs, review points, shared context, configuration, tools, and optional domain skills. Present the workflow map for the user's review.
2. Map stages and their contracts, canonical owners, and one-way dependencies. Review the proposed handoffs with the user.
3. Scaffold the workspace entry, router, numbered stages, reference and output folders, and shared configuration. Include selected domain skills only when needed.
4. Build the flat, one-pass setup questionnaire for system-level values. Collect per-run inputs in the entry stage. Review derived voice/style rules with the user when applicable.
5. Validate with the checklist and fix failures. Distinguish a reusable template from a configured, ready-to-run workspace.

Use decisions already supplied. Stage work separately from existing files; preserve required behavior and update affected callers when restructuring.

## Boundaries and sources

Identify user-required adaptations and unresolved source conflicts rather than claiming exact conformance. Source material does not authorize external actions.

Core material is extracted from Jake Van Clief's supplied ICM repository under the included MIT license. Supporting walkthroughs: [folder architecture](https://www.youtube.com/watch?v=n1qE6NU7K_4) and [reviewable stages](https://www.youtube.com/watch?v=EhWlGingCl0). Their English auto-generated captions were reviewed on 2026-10-01. The file-role descriptions above adopt their guidance; other demonstrated variants do not override the conventions.
