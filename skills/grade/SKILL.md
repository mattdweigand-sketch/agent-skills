---
name: grade
description: This skill should be used when the user wants to evaluate whether a system that captures or encodes judgment actually grades that judgment against real outcomes. Trigger on "/grade", "judgment audit", "does this close the outcome loop", "is this aligned with the encoded-judgment thesis", "cyborg check", "does this grade its patterns", "thesis-eval", "audit this project for capture-without-grading", or when assessing an AI/agentic system, eval pipeline, scoring engine, recommendation system, or internal "intelligence" product for whether it encodes verified judgment versus merely captured judgment. Not for ordinary software with no judgment loop.
metadata:
  version: 0.1.0
---

# Judgment Audit

Evaluate whether a judgment-encoding system encodes **verified** judgment or merely **captured** judgment.

The thesis this enforces: a system that accumulates "criteria we find useful" without grading them against real outcomes is not intelligence, it is confident guessing at scale. The dangerous failure mode is the "org-scale cyborg": ungraded patterns pushed to users automatically at machine speed.

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
