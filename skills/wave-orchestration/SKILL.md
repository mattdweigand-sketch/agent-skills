---
name: wave-orchestration
description: "Run the full wave orchestration workflow for large parallel repo work. Use when the user says /wave-orchestration, wave orchestration, run all waves, start a wave, split this build into bundles, coordinate parallel agents, or wants supervisor/worker/reviewer execution. Routes through wave-supervisor, wave-worker, and wave-reviewer."
version: "2.0"
category: "agentic-systems"
tags: ["waves", "multi-agent", "orchestration", "coding"]
---

# Wave Orchestration

Top-level entrypoint for wave-based parallel repo work.

Use this skill to decide whether a task should become a wave, initialize the
wave control plane, route to the supervisor, and carry the work through as far
as the current runtime allows.

## Contract

**Produces:** a wave plan and coordination files under `.wave/`, plus worker and
reviewer prompts. If asked for execution, drives the defined wave through
implementation, review, cleanup, and verification.

**Consumes:** the user's build goal, target repo state, repo instructions,
available wave role skills, and `.wave/` files if they already exist.

**Does not produce:** automatic merges, destructive git operations, or cloud
deployments without explicit human approval.

## When To Use

Use a wave when the work is broad enough to split into independent bundles:
- repo-wide docs/spec cleanup
- cross-module refactors with separable ownership
- migration work across several folders
- audit-plus-fix passes with clear acceptance criteria
- large feature work where parallel branches can stay mostly disjoint

Do not use a wave for one-file edits, ambiguous strategy work, or changes where
every step depends on the previous result.

## Process

1. **State the routing decision.**
   Say whether the task is wave-worthy. If not, do the work directly.

2. **Invoke `wave-supervisor`.**
   Follow `wave-supervisor` exactly. It shapes the spec, seeds `.wave/`, writes
   bundles, and creates worker/reviewer prompts.

3. **Dispatch workers.**
   Use the prompts produced by the supervisor. Each worker runs `wave-worker` for
   exactly one bundle.

4. **Run review.**
   Start `wave-reviewer` after workers open PRs or local branches. Reviewer
   verdicts are written to `.wave/reviews/`.

5. **Drive cleanup.**
   Supervisor reads reviewer output, writes cleanup prompts, and updates the wave
   dashboard.

6. **Verify integration.**
   Run the agreed tests or smoke checks after cleanup. The human owns merge
   decisions unless they explicitly delegate them.

## Execution Rule

If the user says "run all the waves" or asks for full execution, do not stop at
planning. Complete the defined wave end to end where tools and permissions allow:
planning, worker execution, review, cleanup, and verification.

Ask before merges, destructive git operations, deployments, or any action the
target repo forbids without approval.

## Related Skills

- `wave-supervisor`: spec, bundle split, worker dispatch, cleanup prompts
- `wave-worker`: one bundle, one branch/worktree, one PR or local branch
- `wave-reviewer`: review worker branches against acceptance criteria
