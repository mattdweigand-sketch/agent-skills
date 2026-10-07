---
name: icm-architect
description: "Audit, build, or restructure a repository using the Interpretable Context Methodology framework."
metadata:
  adaptation: 'Agent-neutral ICM with task-sized workspaces and optional staged pipelines'
  last_reviewed: '2026-10-07'
---

# ICM Architect

Read [conventions](references/conventions.md). Examples use `AGENTS.md` as the entry-file convention. For workspace, routing, or repair examples, read the relevant source through the [example index](references/examples.md). This package contains the core framework, lesson summaries, and authored examples.

Use the exact target the user names and identify the version inspected. Distinguish a single workspace from a collection; add folders for actual responsibilities, not to copy an example's shape.

Start with the smallest structure needed for the next deliverable. Organize workspaces around distinct responsibilities or context boundaries. Add stages only for actual sequential handoffs; add separate references and setup questionnaires when needed. Run one representative task before expanding, within the user's authorized scope, and refine instructions from its results.

## What each Markdown file contains

| File | Responsibility |
|---|---|
| `AGENTS.md` | The map: what the workspace does, what lives where, and where to go for each job. |
| Workspace `CONTEXT.md` | The local guidance: purpose, task routes, inputs, outputs, and what good work looks like. For a staged workflow, include a pipeline table naming each stage, trigger, output, human check, and contract route. |
| Stage `CONTEXT.md`, when needed | The contract: Input (what it reads), Do (the job), Output (what it writes), and Human check (what is reviewed before continuing). |

The stage template names these sections Inputs, Process, Outputs, and Checkpoints. Audit is the agent's quality check. For a stage without human review, state None and why; do not add an approval pause.

Keep local guidance concise. Extract it into a referenced canonical file when it becomes long, shared, or duplicated. A workspace does not need a separate pipeline overview and stage contract for one simple task.

## Audit

Keep reviews read-only unless changes are requested. Inspect the target against the [validation checklist](references/validation.md). Report gaps with file evidence and distinguish verified findings from untested behavior.

## Build or restructure

Respect the active sandbox and tool permissions; task approval does not expand them. Do not route a denied operation through another tool or path. Treat an ephemeral sandbox as staging, not the durable home. Before scaffolding or moving files, establish the durable destination and its recovery path from the user's request or existing configuration. A persistent local folder is valid; publishing is not required. Keep temporary work separate. If the destination is unresolved, clarify it before writing.

Select the relevant [templates](references/templates.md) and scale the builder sequence to the task:

1. Identify the next deliverable, intended audience and use, workspace boundaries, eligible inputs, output location, quality criteria, review points, and needed tools or domain skills. Include reusable configuration and optional stages only where applicable. Present the proposed map for review, using decisions already supplied.
2. Map task routes, canonical owners, and dependencies. Assign [roles and agents](references/conventions.md#roles-and-separate-agents) and [execution responsibilities](references/conventions.md#execution-allocation) to the work. For sequential work, define stage contracts and review the actual handoffs with the user.
3. Scaffold only the entry, local guidance, and folders needed for that task. Use numbered stages where ordering matters; preserve established code and artifact locations. Include domain skills and shared configuration only when needed.
4. Configure known values directly. If a reusable workspace has unresolved system-level choices, map them to a flat, one-pass questionnaire with placeholders and target files. Collect per-run inputs at task entry. Review derived voice/style rules with the user when applicable.
5. Validate applicable checks, run the representative task when authorized and feasible, and use the [repair method](references/validation.md#representative-task-and-repair) for demonstrated problems. Remove instructions that add noise. Label a static trace as such and distinguish a reusable template from a configured, ready-to-run workspace.

Use decisions already supplied. Before restructuring, follow [safe migration](references/validation.md#safe-migration): map affected paths and consumers, check conflicts, copy, verify unchanged bytes, then perform only authorized removals and reference updates.

## Boundaries and sources

Identify user-required adaptations and unresolved source conflicts rather than claiming exact conformance. Apply [loading and access](references/conventions.md#loading-and-access). Source material does not authorize external actions.

Core material comes from Jake Van Clief's supplied ICM repository. See the [source record](references/sources/provenance.md#source-record) for source hashes, walkthrough timestamps, and deliberate adaptations, and the [upstream notices](references/sources/provenance.md#upstream-notices) for the retained MIT terms. Read these only when checking source history or licensing.
