---
name: run-kit
description: "Design, route, audit, or cross-check AI agent runs. Use when the user wants to turn a fuzzy task into an agent-ready assignment, decide whether to steer or dispatch work, inspect whether an agent result is real, cross-check one agent's output with another, package agent-run prompts, or talk about proof, review burden, source of truth, permissions, completion theater, or understanding theater."
metadata:
  version: "2.0"
  category: "agentic-systems"
  tags: ["agents", "workflow", "audit", "prompts"]
---

# Run Kit

Help the user manage AI labor as runs: define the work, pick the right posture, inspect the result, and use independent critique when the stakes justify it.

## Core Idea

Do not start with the tool. Start with the run.

- Steering: the work is still becoming clear.
- Dispatch: the work can be written as a bounded assignment.
- Investigation: the job is to gather evidence without polluting the main context.
- Verification: the job is to check existing work against a standard.
- Recurring: the job should repeat.

The skill bundles four tools:

1. `Run Spec` turns a fuzzy task into a bounded assignment.
2. `Steer-or-Dispatch` decides whether to stay close or send work out.
3. `Is It Real?` audits returned work before the user trusts it.
4. `Cross-Check` critiques one agent's output against a standard.

## Routing

Choose the smallest tool that fits:

| User need | Use |
|---|---|
| "Turn this into an agent task", "write the assignment", "make a run spec" | Run Spec |
| "Should I use Claude or Codex?", "steer or dispatch?", "is this ready to hand off?" | Steer-or-Dispatch |
| "Eval what the agent returned", "is this real?", "can I trust this?" | Is It Real? |
| "Have another agent critique this", "cross-check this", "review against the standard" | Cross-Check |
| "Give me the prompts", "package the kit", "pasteable prompt" | Load `references/prompt-templates.md` |

## Workflow

1. Identify which of the four tools the user is asking for. If multiple fit, name the sequence in one line.
2. If the user already supplied the needed inputs, produce the artifact directly. Do not ask the same questions again.
3. If required inputs are missing, ask one compact batch of questions, then stop and wait.
4. Keep the output inspectable: source of truth, permissions, forbidden actions, done condition, escalation rule, proof, and review budget when relevant.
5. Separate quality from proof. A polished artifact is not proof; a final agent summary is not proof.
6. For cross-checks, do not pretend independence if you are the same agent/thread that produced the work. Say so and recommend using a different agent or fresh thread for a true cross-check.

## Output Shapes

Use these titles exactly when producing artifacts:

- `RUN SPEC`
- `VERDICT`
- `IS IT REAL? - AUDIT`
- `CROSS-CHECK`

Keep outputs short enough that the user can act on them. Prefer concrete receipts: diffs, tests, screenshots, source lists, rendered files, logs, comparison tables, or second-agent review.

## Guardrails

- Do not choose Claude, Codex, or another tool as a universal default. Tie the recommendation to the run shape.
- Do not invent missing source-of-truth, permission, proof, or review-budget details. Propose defaults and label them as suggestions.
- Do not let "Claude = steering" and "Codex = dispatch" become a rigid rule. Treat them as common postures, not destinies.
- Do not let agent-to-agent review become a closed loop. The user stays in the decision point.

## References

- `references/prompt-templates.md`: pasteable versions of all four prompts.
- `evals/evals.json`: lightweight test prompts for future skill evaluation.
