---
name: cyborg-check
description: Audit whether a judgment-encoding system closes the loop between captured patterns and real outcomes, or is becoming an org-scale cyborg that spreads unverified judgment at machine speed. Trigger on "/cyborg-check", "cyborg check", "does this close the outcome loop", "is this just captured judgment", "capture without grading", "judgment audit", "are these patterns verified", or when assessing an AI/agentic system, eval pipeline, scoring engine, recommendation system, sales-intelligence system, or internal "best practice" tool. Do not use for ordinary grading, document review, rubric scoring, or software with no judgment loop.
metadata:
  version: 0.1.0
---

# Cyborg Check

Evaluate whether a judgment-encoding system encodes **verified** judgment or merely **captured** judgment.

Capturing judgment is not the same as proving it. This skill checks whether the system connects its captured criteria, patterns, recommendations, or scores to real outcome labels before those patterns become trusted or user-visible.

The dangerous failure mode is the org-scale cyborg: ungraded patterns pushed to users automatically at machine speed.

This skill produces an **inline verdict** with evidence and a punch list. It does not write a file.

Load `references/judgment-audit-rubric.md` when the skill applies. That file owns the stable applicability rules, evidence checklist, scoring axes, verdict taxonomy, and principles.

## Step 0 — Applicability gate (refuse cleanly when it does not apply)

Use the applicability gate in `references/judgment-audit-rubric.md`. If no judgment is being encoded, stop cleanly instead of forcing the rubric.

## Step 1 — Gather evidence (read, do not assume)

Inspect the actual code and docs. Do not score from the README's claims. For each axis below, find the concrete artifact or confirm its absence. Cite file paths and line numbers in the verdict.

Use the evidence checklist in `references/judgment-audit-rubric.md`. Designed-but-unbuilt counts as unbuilt.

## Step 2 — Score the axes

Mark each rubric axis from `references/judgment-audit-rubric.md` as **present / partial / absent / not-applicable**, with cited evidence.

## Step 3 — Render the verdict inline

Open with one verdict from `references/judgment-audit-rubric.md`, then the evidence and the punch list.

Then give:
- **Evidence**, per axis, with file:line citations. Report what is present as well as what is missing, so the user can see the system's real shape, not just its gaps.
- **Punch list**, ordered by leverage. Lead with the one move that most changes alignment. For most capture-without-grading systems that is: prove the assumption by hand before building, then build capture and grading together, never capture alone.

## Principles

Use the principles in `references/judgment-audit-rubric.md` when weighing recommendations.
