---
name: "source-command-wave-orchestration"
description: "Run the migrated source command /wave-orchestration. Use when the user says /wave-orchestration, run wave orchestration, start the wave workflow, run all waves, split this build into waves, or wants supervisor/worker/reviewer parallel execution."
---

# source-command-wave-orchestration

Use this skill when the user asks to run the migrated source command
`wave-orchestration`.

## Command Template

Invoke the `wave-orchestration` skill and follow its instructions exactly.

Treat `/wave-orchestration` as the top-level entrypoint for the wave workflow:

1. Shape the target repo goal with the user.
2. Seed `.wave/` with the shared protocol if needed.
3. Write `.wave/spec.md`, bundle files, status files, and the wave dashboard.
4. Output paste-ready prompts for `wave-worker` and `wave-reviewer`.

If the user says "run all the waves" or asks for full execution, do not stop at
planning. Run the defined wave through implementation, review, cleanup, and
verification as far as the current agent runtime allows. Ask only before
consequential actions such as merges, destructive git operations, or cloud
deployments.

## Related Skills

- `wave-orchestration`
- `wave-supervisor`
- `wave-worker`
- `wave-reviewer`
