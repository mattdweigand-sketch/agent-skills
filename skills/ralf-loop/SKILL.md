---
name: ralf-loop
description: >-
  Run a repo-agnostic RALF-style improvement loop: run a smoke test or workflow,
  analyze failures against frozen gates, make one bounded fix, review the change,
  rerun, and stop at a clear terminal point. Use when the user says "RALF loop",
  "loop testing", "multi-agent test loop", "submit/review/analyze/redeploy",
  "tighten this system with agents", "run the smoke test until it converges", or
  asks to repeatedly harden a repo, harness, skill, prompt, test suite, workflow,
  retrieval system, exporter, parser, or agentic product using local tests and
  review gates. Works on any repo with a local command or scorable workflow.
metadata:
  version: "1.0"
  category: "agentic-systems"
  tags: ["ralf", "testing", "multi-agent", "smoke-test", "eval", "harness"]
---

# RALF Loop

Repo-agnostic loop for hardening a local system until it reaches a terminal point.

RALF here means:

| Phase | Meaning |
|---|---|
| Run | Execute the local smoke test, workflow, eval, or reproduction command. |
| Analyze | Score behavior against frozen gates and classify misses. |
| Learn | Convert real failures into one bounded hypothesis. |
| Fix | Make the smallest local change that should improve the score. |
| Rerun | Re-execute the same gates and decide keep, revert, or stop. |

Use subagents only when the user explicitly asks for agents, multi-agent work, delegation, or parallel review. Otherwise run the same phases locally.

## Guardrails

- Do not deploy cloud resources unless the user explicitly asks and the repo allows it.
- Treat "redeploy" as "rerun the local harness" by default.
- Do not send data externally, auto-submit forms, email results, or bypass approval gates.
- Do not use destructive git commands. Revert only your own changes, preferably with `apply_patch`.
- Do not edit the scorer, labels, or expected outputs mid-loop unless you stop and declare a test-harness bug.
- Preserve user changes. Check `git status --short` before editing and track only files you touch.
- Stop instead of guessing if credentials, production systems, paid services, or irreversible changes are required.

## Intake

State assumptions before acting:

- Repo root and working directory.
- Target command or workflow to run.
- Terminal point.
- Maximum iterations.
- Whether subagents are authorized.

If the user did not provide these, infer conservatively:

- Repo root: current working directory.
- Target command: start with obvious scripts: `npm test`, `pnpm test`, `pytest`, `cargo test`, `go test ./...`, or repo-specific smoke scripts.
- Terminal point: all frozen gates pass once. Use three consecutive passes for flaky, retrieval, generative, race-prone, or agentic workflows.
- Maximum iterations: 5.

Ask only when the wrong choice could cause external effects or irreversible work.

## Required Setup

Create a run folder:

```text
deliverables/ralf-loop/<run-tag>/
```

Write or update these artifacts as the loop runs:

```text
deliverables/ralf-loop/<run-tag>/summary.json
deliverables/ralf-loop/<run-tag>/report.md
deliverables/ralf-loop/<run-tag>/iterations/<NN>-run.log
deliverables/ralf-loop/<run-tag>/iterations/<NN>-analysis.md
```

If the repo has its own artifact convention, follow it, but keep the RALF report under `deliverables/ralf-loop/`.

## Frozen Gates

Before making fixes, define the gates. Good gates include:

- Exact command exit code.
- Expected counts, statuses, or files.
- Positive cases that must pass.
- Negative cases that must remain blocked, absent, or refused.
- Security, privacy, approval, or export-readiness constraints.
- No unexpected network, deploy, email, or production writes.

For retrieval, DDQ, parsers, AI workflows, or generators, always include negative controls. A pass without negatives is not a trustworthy pass.

## Baseline

Run the target once before editing.

Record:

- Command.
- Exit code.
- Key output.
- Artifact paths.
- Gate results.
- Failure classification.

Do not start fixing until the baseline is captured.

## Agent Pattern

Only use this when subagents are authorized.

Use small, distinct roles:

| Role | Type | Job |
|---|---|---|
| Submitter | local coordinator or worker | Runs the target command and captures artifacts. |
| Reviewer | explorer | Checks whether the output satisfies the gates and finds unsafe passes. |
| Analyzer | explorer | Classifies failures and proposes the smallest fix. |
| Builder | main agent by default | Applies one bounded change. Use a worker only for a disjoint file slice. |

Recommended prompts:

```text
Reviewer: Inspect the latest RALF artifacts and repo behavior. Do not edit files.
Find false positives, missing gates, approval bypasses, unsafe exports, and test
integrity issues. Return findings with file/artifact paths and required pass gates.
```

```text
Analyzer: Inspect the failing run artifacts. Do not edit files. Classify each failure
as implementation bug, fixture gap, scorer bug, label issue, flaky behavior, or
external blocker. Propose the smallest local change for the next iteration.
```

Never ask multiple agents to edit the same files in the same iteration.

## Loop

For each iteration:

1. Run the frozen command or workflow.
2. Score the frozen gates.
3. If all gates pass, run the terminal confirmation pass if needed.
4. If gates fail, classify misses.
5. Choose exactly one hypothesis.
6. Make one bounded change.
7. Run the smallest relevant check.
8. Run the full frozen gates.
9. Keep the change if the score improves or the system becomes simpler with no score loss.
10. Revert your own change if the score is worse or hides a failure.
11. Log the iteration.

One iteration should have one main fix. If the failure requires a structural redesign, stop and present a plan instead of grinding.

## Stop Conditions

Stop with `pass` when:

- All frozen gates pass.
- Required repeated passes are clean.
- Review finds no blocking safety or test-integrity issue.

Stop with `needs-human` when:

- The next action needs credentials, cloud deployment, production access, paid services, or external submission.
- The scorer or labels are wrong.
- Requirements conflict.
- Approval policy prevents the needed command.

Stop with `blocked` when:

- The same class of failure persists after two reasonable fixes.
- The fix is architectural and no longer loop-shaped.
- The maximum iteration count is reached.

## Report Contract

The final response should be short and include:

- Status: `pass`, `needs-human`, or `blocked`.
- Baseline to final delta.
- Iterations run.
- Files changed.
- Commands run.
- Residual risks.
- `computer://` links to `report.md` and important artifacts when available.

The report should include:

```text
# RALF Loop Report

Status:
Run tag:
Target:
Terminal point:

## Gates
...

## Iterations
...

## Final Result
...

## Residual Risks
...
```

## When Not To Use

Do not use this skill for open-ended research with no runnable target, writing-only tasks with no scorer, cloud deployment, production migrations, or work where the user only asked for a one-time review.
