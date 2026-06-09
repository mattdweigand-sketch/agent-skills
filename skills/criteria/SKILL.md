---
name: criteria
description: "Audit judge-style criteria, rubrics, or manual evaluation checks to decide which should become automated LLM judges, deterministic checks, manual reviews, or be dropped. Use when the user runs /criteria or asks for a criteria audit, judge criteria audit, rubric promotion review, eval coverage audit, or wants to decide whether subjective criteria are worth automating. Not for checking whether a system grades encoded judgment against outcomes (that's the grade skill)."
version: "2.0"
category: "analysis"
tags: ["evals", "judgment", "rubrics", "quality"]
---

# Rubric Promotion Audit

Audit subjective evaluation criteria and recommend which ones deserve automation.

## Use This When

Use this skill when the user asks to:
- audit `type: judge`, manual, rubric, or subjective success criteria
- decide whether to build an LLM-judge runner
- review skipped eval coverage
- rank criteria by frequency, stakes, and automation value
- convert subjective checks into deterministic checks where possible

## Contract

**Produces:** a markdown audit report in the current repo, plus a short chat summary.

**Does not produce:** runner implementation, schema migration, scheduler changes, or production writes unless the user explicitly asks after the audit.

## Assumptions To State

Before acting, state:
- which repo/worktree you are auditing
- where criteria live
- where eval logs or recent artifacts live
- what report path you will write

If any of these are unclear and not discoverable from local files, ask one concise question.

## Audit Workflow

1. **Find criteria.**
   Use `rg` and local file inspection. Look for terms such as `type: judge`, `type: manual`, `success_criteria`, `rubric`, `judge`, `manual`, `criteria`, and `eval`.

2. **Catalog criteria.**
   Build a table with: criterion id, parent job/file, type, rubric/check text, expected evidence, and current evaluator path if any.

3. **Scan execution signal.**
   Read eval logs, run reports, or recent output artifacts. Count how often each criterion is skipped, manually reviewed, failed, or would have been relevant. Prefer actual logs over speculation.

4. **Check deterministic alternatives.**
   For each criterion, ask whether it can become a deterministic check:
   - file exists / section exists
   - regex or structured parse
   - JSON/schema validation
   - count or threshold
   - local command/test result
   - retrieval or metadata query through approved tools

5. **Spot-check real artifacts.**
   Inspect 2 to 5 recent representative outputs. Ask whether each criterion would have caught a real quality issue. If it would not have fired, call that out.

6. **Score each criterion.**
   Use:
   - Frequency: high / medium / low
   - Stakes: high / medium / low
   - Auto-convertibility: yes / partial / no
   - Evidence quality: strong / mixed / weak

7. **Recommend one action.**
   For each criterion, choose exactly one:
   - `PROMOTE` — build an LLM judge
   - `AUTO-CONVERT` — replace with deterministic check
   - `KEEP-MANUAL` — judgment matters, but automation is not worth it yet
   - `DROP` — low signal, unclear rubric, or no observed value

8. **Write the report.**
   Save inside the audited repo. Prefer an existing eval/report folder. If none exists, use `research/` or `reports/`.

## Report Template

```markdown
# Rubric Promotion Audit: <scope>

## Scope
- Repo:
- Criteria source:
- Eval/log source:
- Artifact sample:

## Criteria Catalog
| Criterion | Parent | Type | Rubric | Current status |
|---|---|---|---|---|

## Execution Signal
| Criterion | Observed skips/reviews/failures | Artifact evidence | Notes |
|---|---:|---|---|

## Recommendations
| Criterion | Frequency | Stakes | Auto-convertibility | Evidence | Recommendation |
|---|---|---|---|---|---|

## V2 Judge Scope
List the 3 to 5 best LLM-judge candidates. For each, include:
- why deterministic checks are insufficient
- judgment prompt sketch
- required evidence/context
- expected output shape

## Auto-Conversion Candidates
List criteria that should become deterministic checks instead of LLM judges.

## Drop / Keep Manual
Explain briefly.
```

## Output Rules

- Be direct. Do not promote criteria just because they exist.
- Prefer deterministic checks over LLM judges when the signal can be verified mechanically.
- Separate "valuable criterion" from "worth automating."
- Include file paths and line references for important claims.
- End with a short summary: top promotions, auto-conversions, drops, and rough implementation effort.
- Provide a `computer://` link to the saved report.
