# Skill Creator — Eval Methodology

Complete workflow for running, grading, and iterating on skill evals.

---

## Overview

The eval loop: draft prompts → run in parallel → grade assertions → human review → iterate.
Always generate the viewer before grading yourself. Human review comes first.

---

## Step 1: Prepare Eval Prompts

Load `evals/evals.json`. If it doesn't exist, create 2–3 realistic test prompts covering:
- Happy path (clear trigger, expected format)
- Edge case (ambiguous input, boundary condition)
- Negative case (should NOT trigger, or should produce minimal output)

Share prompts with the user for approval before running.

---

## Step 2: Run Evals in Parallel

Spawn one agent per eval prompt. Each agent:
1. Receives the prompt plus the SKILL.md (and referenced files)
2. Produces output as if the skill is active
3. Returns raw output to the grading step

Do not evaluate the output yourself before the human sees it.

---

## Step 3: Generate the Viewer

Run before grading:

```bash
python eval-viewer/generate_review.py evals/grading.json
```

This produces a static HTML file the user can open locally. Present the path and ask the user to review it. Wait for feedback.

If in Claude.ai (no browser): present a formatted markdown summary of outputs for each eval instead.

---

## Step 4: Draft and Apply Assertions

After the user reviews:
1. Ask which outputs passed and which failed
2. Generalize the failure patterns into assertion rules (see `schemas.md` for assertion types)
3. Add assertions to `evals/evals.json`
4. Update `evals/grading.json` with pass/fail per assertion

**Assertion quality bar:** assertions should catch systematic failures, not be so narrow they only catch this one bad output. If an assertion only fires for the specific failure case, generalize it.

---

## Step 5: Grade and Aggregate

Run scoring:

```python
# Pseudo-code — implement per-environment
for eval in evals:
    for assertion in eval.assertions:
        result = check_assertion(assertion, output)
        record(result)

pass_rate = passed / total
```

Write results to `evals/grading.json`. Append summary to `evals/benchmark.json` (see `schemas.md`).

---

## Step 6: Iterate

Based on grading:
- Pass rate > 80%: skill is performing well. Show user summary, offer to finalize.
- Pass rate 60–80%: identify the failing pattern. Improve the specific section of SKILL.md (or a reference file) that causes the failure. Rerun from Step 2.
- Pass rate < 60%: fundamental issue with skill structure. Review the core process and rewrite before rerunning.

**Variance check:** If pass rate varies > 15% across runs in benchmark.json, the skill is unstable. Tighten constraints in the relevant SKILL.md section.

---

## Step 7: Human Score (Optional)

For subjective skills (writing quality, reasoning quality), add human scores after the user reviews:

```json
"human_score": 4,
"human_notes": "Good structure but missing the risk section"
```

Aggregate in benchmark.json under `human_scores`.

---

## Cowork Environment

Static HTML viewer works normally. Feedback is downloaded as a JSON file from the viewer. Load it back: `python eval-viewer/load_feedback.py <path-to-feedback.json>`.
