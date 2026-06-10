---
name: runtime-guard
description: Prevents an agent from editing or publishing without clearly defined authority, boundaries, stop conditions, or rollback.
---

# Runtime Guard

Default: skip this skill.

Use this as a runtime behavior guard before an agent takes a consequential
action. Its job is to stop the agent from guessing what it is allowed to do.

This is not a planning ritual, prompt audit, or enforcement layer.

## Trigger

Use only when all are true:

- The next action changes durable files, sends external output, edits shared
  state, or alters risky configuration.
- The source of authority, allowed boundary, excluded boundary, verification
  path, or rollback path is unclear.
- No user instruction, repo workflow, script, approval gate, or task router
  already answers the question.

Do not use this for routine code edits, explanations, local reads, or tasks
where the user already supplied the boundary.

## Guard Note

If triggered, produce at most five lines:

- Goal:
- Source of authority:
- In scope:
- Out of scope:
- Stop / verify / rollback:

If any field requires guessing, ask one question instead of filling it in.

## Boundary

This skill does not enforce compliance. Use existing scripts, tests, schemas, approval gates, or repo workflows for machine-checkable constraints.
