---
name: quality-check-eval
description: "Sort AI output quality checks into four buckets: automate in code, judge with an LLM, keep for human review, or remove. Use when reviews are too manual, evals are vague, a workflow needs clearer quality gates, or the user wants to decide which AI output checks are worth automating. Not for checking whether a system grades encoded judgment against real outcomes; use cyborg-check for that."
metadata:
  version: "2.0"
  category: "analysis"
  tags: ["evals", "checks", "judges", "quality"]
---

# Quality Check Eval

Use this when an AI workflow has quality checks, review notes, rubric items, or
acceptance criteria, and you need to decide how each one should be handled.

The skill sorts each check into one of four buckets: automate in code, judge
with an LLM, keep for human review, or remove.

This is useful when reviews are too manual, evals are vague, or a team is unsure
which quality checks are worth automating.

Load `references/eval-check-routing.md` when auditing. That file owns the stable
recommendation taxonomy, scoring fields, deterministic alternatives, and report
template.

## Use This When

Use this skill when the user asks to:
- audit `type: judge`, manual, rubric, or subjective eval checks
- decide whether to build an LLM-judge runner
- review skipped eval coverage
- rank eval checks by frequency, stakes, and automation value
- convert subjective checks into deterministic checks where possible

## Contract

**Produces:** a markdown audit report in the current repo, plus a short chat summary.

**Does not produce:** runner implementation, schema migration, scheduler changes, or production writes unless the user explicitly asks after the audit.

## Assumptions To State

Before acting, state:
- which repo/worktree you are auditing
- where eval checks live
- where eval logs or recent artifacts live
- what report path you will write

If any of these are unclear and not discoverable from local files, ask one concise question.

## Audit Workflow

1. **Find eval checks.**
   Use `rg` and local file inspection. Look for terms such as `type: judge`, `type: manual`, `success_criteria`, `rubric`, `judge`, `manual`, `criteria`, and `eval`.

2. **Catalog eval checks.**
   Build a table with: check id, parent job/file, type, rubric/check text, expected evidence, and current evaluator path if any.

3. **Scan execution signal.**
   Read eval logs, run reports, or recent output artifacts. Count how often each check is skipped, manually reviewed, failed, or would have been relevant. Prefer actual logs over speculation.

4. **Check deterministic alternatives.**
   Use the deterministic alternatives in `references/eval-check-routing.md`.

5. **Spot-check real artifacts.**
   Inspect 2 to 5 recent representative outputs. Ask whether each check would have caught a real quality issue. If it would not have fired, call that out.

6. **Score each check.**
   Use the scoring fields in `references/eval-check-routing.md`.

7. **Recommend one action.**
   For each check, choose exactly one action from `references/eval-check-routing.md`.

8. **Write the report.**
   Save inside the audited repo. Prefer an existing eval/report folder. If none exists, use `research/` or `reports/`. Use the report template in `references/eval-check-routing.md`.

## Report Template

Use `references/eval-check-routing.md`.

## Output Rules

- Be direct. Do not automate checks just because they exist.
- Prefer deterministic checks over LLM judges when the signal can be verified mechanically.
- Separate "valuable review question" from "worth automating."
- Include file paths and line references for important claims.
- End with a short summary: top promotions, auto-conversions, drops, and rough implementation effort.
- Provide a `computer://` link to the saved report.
