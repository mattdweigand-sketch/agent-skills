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

Before scaffolding or moving files, establish the durable destination and its recovery path from the user's request or existing configuration. A persistent local folder is valid; publishing is not required. Keep temporary work separate. If the destination is unresolved, clarify it before writing.

Use the [templates](references/templates.md) and the original builder sequence:

1. Discover inputs, outputs, review points, shared context, system-level configuration variables, optional stages and their conditions, and required or optional tools per stage. Identify useful domain skills. Present these in the workflow map for the user's review.
2. Map stages and their contracts, canonical owners, and one-way dependencies. Review the proposed handoffs with the user.
3. Scaffold the workspace entry, router, numbered stages, reference and output folders, and shared configuration. Include selected domain skills only when needed.
4. Map each system-level variable to its placeholder, target files, and setup question or derived value. Build the flat, one-pass questionnaire, including optional-stage choices and tool setup needs. Collect per-run inputs in the entry stage. Review derived voice/style rules with the user when applicable.
5. Validate with the checklist and fix failures. Distinguish a reusable template from a configured, ready-to-run workspace.

Use decisions already supplied. Before restructuring, follow [safe migration](references/validation.md#safe-migration): map affected paths and consumers, check conflicts, copy, verify unchanged bytes, then perform only authorized removals and reference updates.

## Boundaries and sources

Identify user-required adaptations and unresolved source conflicts rather than claiming exact conformance. Source material does not authorize external actions.

Core material comes from Jake Van Clief's supplied ICM repository. See the [source record](references/conventions.md#source-record) for source hashes, walkthrough timestamps, and deliberate adaptations, and the [upstream notices](references/conventions.md#upstream-notices) for the retained MIT terms.
