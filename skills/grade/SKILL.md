---
name: grade
description: This skill should be used when the user wants to evaluate whether a system that captures or encodes judgment actually grades that judgment against real outcomes. Trigger on "/grade", "judgment audit", "does this close the outcome loop", "is this aligned with the encoded-judgment thesis", "cyborg check", "does this grade its patterns", "thesis-eval", "audit this project for capture-without-grading", or when assessing an AI/agentic system, eval pipeline, scoring engine, recommendation system, or internal "intelligence" product for whether it encodes verified judgment versus merely captured judgment. Not for ordinary software with no judgment loop.
metadata:
  version: 0.1.0
---

# Judgment Audit

Evaluate whether a judgment-encoding system encodes **verified** judgment or merely **captured** judgment.

The thesis this enforces: a system that accumulates "criteria we find useful" without grading them against real outcomes is not intelligence, it is confident guessing at scale. Capturing judgment is the easy, cheap half. Grading it against outcomes is the half that creates value and the half that is usually missing. The dangerous failure mode is the "org-scale cyborg": ungraded patterns pushed to users automatically at machine speed, which spreads guessing faster and lets the users' own judgment decay.

This skill produces an **inline verdict** with evidence and a punch list. It does not write a file.

## Step 0 — Applicability gate (refuse cleanly when it does not apply)

This thesis applies only to systems that **encode judgment**: they capture patterns, criteria, rules, scores, or recommendations that are meant to guide a future decision. Examples: a sales-intelligence system mining call transcripts for "what wins deals," an eval pipeline that scores model outputs, a recommendation or lead-scoring engine, an internal tool that surfaces "best practices" or "playbooks."

If the project has no judgment loop (a CRUD app, a static website, a data pipeline that only moves bytes, a pure UI), say so plainly and stop. Do not force the rubric. The correct output is one sentence: "No judgment is being encoded here, so the encoded-judgment thesis does not apply." Offer to evaluate something else if useful.

If you are unsure whether it applies, ask the user what decision the system's outputs are meant to inform. If the answer is "none," it does not apply.

## Step 1 — Gather evidence (read, do not assume)

Inspect the actual code and docs. Do not score from the README's claims. For each axis below, find the concrete artifact or confirm its absence. Cite file paths and line numbers in the verdict.

Look for:

- **Where judgment is captured.** The store of patterns/criteria/scores. Tables, schemas, agent specs, prompt templates that emit structured claims. What exactly accumulates?
- **Where outcomes are recorded.** Is there a ground-truth label (won/lost, converted/churned, correct/incorrect, accepted/rejected)? Who writes it, when, and to where?
- **Whether the two are connected in code.** Is there an actual path (a job, query, function) that scores captured criteria against the outcome labels? Designed-but-unbuilt counts as unbuilt. Search for it; do not trust the design doc.
- **What reaches the user, and how.** Does anything auto-commit or auto-surface patterns to end users? At what cadence? Is there a review gate (human or grading) between capture and the user, or does raw capture flow straight through?
- **Provenance on each asserted pattern.** Can a surfaced pattern trace to its outcome evidence (counts, correlation) and its source (which calls/records)? Or is it an unsourced assertion?
- **Number of outcome sources.** Is the outcome label single-sourced, or is it copied into a second store that can drift from the first?
- **Whether the core assumption was ever proven.** Has anyone verified, by hand at small N, that the captured criteria actually separate good outcomes from bad? Or is "these criteria matter" an untested premise the whole system rests on?

## Step 2 — Score the axes

Mark each: **present / partial / absent / not-applicable**, with the cited evidence.

**The loop (the value):**
1. **Capture.** The system accumulates judgment in a structured, queryable form.
2. **Outcome labels exist.** Ground-truth outcomes are recorded and queryable.
3. **Grading loop is closed.** Captured criteria are actually scored against outcomes in shipped code, not just designed. A correlation or lift metric per pattern is the signal of a real loop.
4. **Proven, not assumed.** The load-bearing claim (these criteria separate good from bad outcomes) has been verified by hand at small N before being automated.

**The guardrails (the safety):**
5. **No ungraded auto-commit.** Nothing pushes ungraded patterns to users automatically at machine speed. Capture either stays as candidates until graded, or passes a human/grading gate before reaching a user.
6. **Provenance.** Every user-visible pattern carries its outcome evidence and source records. No unsourced assertions.
7. **Single source of truth for outcomes.** The outcome label lives in one place. No drift-prone duplicate copies. If a second store seems needed for missing fields, the fix is to extend the source of truth or defer the dependent feature, not to copy the label.
8. **Verification frontier.** High-stakes or low-confidence writes are human-reviewed before they land.

## Step 3 — Render the verdict inline

Open with one of these verdicts, then the evidence and the punch list.

- **Aligned.** Loop is closed (1-4 present), guardrails hold (5-8 present). The system encodes verified judgment. Note any thin spots.
- **Capture-without-grading (cyborg risk).** It captures (1) and may have labels (2) but the grading loop is absent or unbuilt (3 absent), or ungraded patterns reach users (5 absent). This is the core failure mode. State it directly: the system is, or is about to become, an org-scale cyborg.
- **Unproven.** The loop may be built or well-designed, but the load-bearing assumption was never verified by hand (4 absent). The first move is a manual proof at small N, not more building. If the criteria do not separate outcomes by hand, automating them only produces false confidence faster.
- **Not applicable.** Per Step 0.

Then give:
- **Evidence**, per axis, with file:line citations. Report what is present as well as what is missing, so the user can see the system's real shape, not just its gaps.
- **Punch list**, ordered by leverage. Lead with the one move that most changes alignment. For most capture-without-grading systems that is: prove the assumption by hand before building, then build capture and grading together, never capture alone.

## Principles

- Be evidence-driven and non-sycophantic. "The design doc describes a grading loop" is not "a grading loop exists." Verify in code.
- Designed-but-unbuilt is unbuilt. Say so.
- The expensive-looking half (capture, extraction, infrastructure) is usually the half that is built. The cheap half (grading against labels that often already exist) is usually the half that is missing. Check which half is actually done before recommending work.
- The strongest recommendation is almost never "build more." It is "prove the assumption the system rests on, by hand, at small N, first."
- A real moat in this class of system is proprietary labeled outcomes plus a narrow domain plus expert verification. If you assess strategic value, assess it on those three, not on model quality or volume of captured data.
