---
name: scope
description: Use only before an AI agent creates durable state, sends external output, or changes files/config when a missing source of authority, entity boundary, data flow, or rollback path would materially change the result and no repo/workflow-specific router already answers it. Skip for routine edits, explanations, local reads, and already-bounded tasks.
---

# Scope

Default: skip this skill.

Use it only as a missing-authority gate, not as a planning ritual or enforcement layer.

## Trigger

Use only when all are true:

- The next action creates durable state, sends external output, or changes files/config.
- A missing source of authority, entity boundary, data flow, or rollback path would materially change the result.
- No repo/workflow-specific router already answers the question.

Do not create a scope note for routine code edits, explanations, local reads, or tasks where the user supplied the boundary.

## Scope Note

If triggered, produce at most five lines:

- Goal:
- Source of authority:
- In scope:
- Out of scope:
- Stop / verify / rollback:

If any field requires guessing, ask one question instead of filling it in.

## Boundary

This skill does not enforce compliance. Use existing scripts, tests, schemas, approval gates, or repo workflows for machine-checkable constraints.
