---
name: swarm
description: "Invocation-only workflow. Use only when the user explicitly invokes `swarm` as a command or asks to swarm a task. Do not trigger for broader agent, harness, judge, checker, orchestration, or multi-agent requests unless the literal `swarm` invocation is present."
---

# Swarm

Invocation-only workflow for turning a bounded task into a verified swarm: planner, workers, checks, appeals, and a review packet.

The core rule: do not trust the agents. Build the institution around them.

## Trigger Boundary

Use this skill only when the user explicitly invokes `swarm`, for example:

- `swarm this`
- `run swarm on this workflow`
- `swarm: <task>`
- `/swarm <task>`

Do not use this skill for incidental mentions of agents, multi-agent design, orchestration, checkers, judges, Ringer, or harnesses unless the user uses `swarm` as the invocation keyword.

## Default Posture

Swarm is not the default answer. A task earns a swarm only when it can be split into bounded lanes and checked cheaply enough that parallelism reduces review burden instead of multiplying it.

If the task is not swarm-ready, return `DO NOT SWARM` with the smallest better alternative.

## Workflow

### 1. Capture The Job

Identify:

- goal
- source of truth
- allowed actions
- forbidden actions
- durable/external side effects
- done condition
- review budget

If any of these are missing and cannot be inferred safely, ask one compact batch of questions before designing the swarm.

### 2. Run The Readiness Gate

Classify the task:

- `SWARM`: multiple bounded lanes, independent outputs, clear checks, manageable merge.
- `SINGLE RUN`: one agent/thread should do it; parallelism adds overhead.
- `STEER FIRST`: the work is still too ambiguous.
- `DO NOT RUN`: permission, source-of-truth, safety, or rollback path is missing.

Use `SWARM` only when all are true:

- Work can be decomposed into lanes with explicit boundaries.
- Each lane has a concrete artifact or answer.
- Each lane has an executable, citeable, or inspectable check.
- Merge can be reviewed against a written standard.
- Side effects are gated before execution.

### 3. Write The Constitution

Define 5 to 14 testable rules for done-right work.

Each rule must include:

- the standard
- the evidence needed
- the check method
- who decides if the check is disputed

Prefer deterministic checks. Use LLM judges only where judgment is real and the evidence is available.

### 4. Design The Org Chart

Assign:

- `Planner`: decomposes the work, writes lane specs, does not execute worker tasks by default.
- `Workers`: execute one bounded lane each; no global authority; no external side effects unless explicitly allowed.
- `Checkers`: verify worker outputs against the constitution; deterministic checks first, LLM judges second.
- `Reviewer`: merges outputs, resolves contradictions, and prepares the review packet.
- `Owner`: the human or named authority who accepts, rejects, or escalates the final result.

No rank escapes verification. Planner, worker, checker, and reviewer outputs can all be wrong.

### 5. Build The Appeals Path

Checks can fail incorrectly. Include a process for:

- worker retry after a valid failure
- checker correction after an invalid failure
- escalation when evidence is insufficient
- human review for high-stakes or ambiguous boundaries

The appeal must preserve the reason for the original check and the reason for changing it.

### 6. Produce The Review Packet

The review packet is the product. Final prose is only a receipt.

Include:

- task and scope
- constitution
- lane specs
- worker outputs or expected artifacts
- checks run or proposed
- failures, retries, and appeals
- unresolved risks
- final recommendation

## Output Shape

Use this heading:

`SWARM PLAN`

Then include:

- `Verdict`: SWARM / SINGLE RUN / STEER FIRST / DO NOT RUN
- `Why`: short reason for the verdict
- `Constitution`: numbered testable rules
- `Org Chart`: planner, workers, checkers, reviewer, owner
- `Worker Lanes`: lane name, task, input, output, forbidden actions
- `Checks`: command, citation check, deterministic check, LLM judge, or human review
- `Appeals`: retry, checker correction, escalation path
- `Review Packet`: what the final packet must contain
- `Execution Notes`: exact next prompts, commands, or dispatch instructions if execution is requested

## Guardrails

- Do not turn every task into a swarm.
- Do not let worker self-reports count as proof.
- Do not let a persuasive explanation substitute for evidence.
- Do not allow external writes, sends, deletes, purchases, permission changes, production commands, or public posts without explicit permission.
- Do not hide uncertainty inside the final recommendation.
- Do not create a closed loop where the same agent that produced work is treated as an independent checker.
- If execution is requested but the available environment cannot run real parallel agents, produce pasteable worker and checker prompts instead.
