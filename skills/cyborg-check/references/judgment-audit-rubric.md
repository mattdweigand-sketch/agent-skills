# Cyborg Check Rubric

Use this reference when `cyborg-check` applies. It owns the stable rubric and verdict taxonomy so `SKILL.md` can stay focused on routing and process.

## Applicability Gate

This thesis applies only to systems that **encode judgment**: they capture patterns, criteria, rules, scores, or recommendations that are meant to guide a future decision. Examples include a sales-intelligence system mining call transcripts for "what wins deals," an eval pipeline that scores model outputs, a recommendation or lead-scoring engine, or an internal tool that surfaces "best practices" or "playbooks."

If the project has no judgment loop, such as a CRUD app, static website, byte-moving data pipeline, or pure UI, say so plainly and stop. Do not force the rubric. The correct output is one sentence: "No judgment is being encoded here, so the encoded-judgment thesis does not apply." Offer to evaluate something else if useful.

If you are unsure whether it applies, ask what decision the system's outputs are meant to inform. If the answer is "none," it does not apply.

## Evidence Checklist

| Question | Evidence to find |
|---|---|
| Where is judgment captured? | The store of patterns, criteria, scores, rules, recommendations, schemas, agent specs, or prompt templates that emit structured claims. |
| Where are outcomes recorded? | Ground-truth labels such as won/lost, converted/churned, correct/incorrect, accepted/rejected; who writes them, when, and where. |
| Are capture and outcomes connected in code? | A shipped job, query, function, or workflow that scores captured criteria against outcome labels. Designed-but-unbuilt counts as unbuilt. |
| What reaches users, and how? | Any auto-commit or auto-surface path, cadence, and human or grading gate between capture and user-visible output. |
| Does each asserted pattern have provenance? | Traceability from surfaced pattern to outcome evidence, counts or correlation, and source records. Unsourced assertions fail this check. |
| How many outcome sources exist? | Whether the outcome label is single-sourced or copied into drift-prone stores. |
| Was the core assumption proven? | Manual small-N evidence that captured criteria separate good outcomes from bad before automation. |

## Scoring Axes

Mark each axis as **present / partial / absent / not-applicable**, with cited evidence.

| Axis | Category | What present means |
|---|---|---|
| Capture | Loop value | The system accumulates judgment in a structured, queryable form. |
| Outcome labels exist | Loop value | Ground-truth outcomes are recorded and queryable. |
| Grading loop is closed | Loop value | Captured criteria are scored against outcomes in shipped code. Correlation or lift per pattern is the signal of a real loop. |
| Proven, not assumed | Loop value | The load-bearing claim that criteria separate good from bad outcomes has been verified by hand at small N before automation. |
| No ungraded auto-commit | Guardrail | Nothing pushes ungraded patterns to users automatically at machine speed. Capture stays as candidates until graded or passes a human/grading gate. |
| Provenance | Guardrail | Every user-visible pattern carries outcome evidence and source records. No unsourced assertions. |
| Single source of truth for outcomes | Guardrail | The outcome label lives in one place. If missing fields make a second store tempting, extend the source of truth or defer the feature. |
| Verification frontier | Guardrail | High-stakes or low-confidence writes are human-reviewed before they land. |

## Verdict Taxonomy

| Verdict | Use when |
|---|---|
| **Aligned.** | Loop axes 1-4 are present and guardrails 5-8 hold. The system encodes verified judgment. Note any thin spots. |
| **Capture-without-grading (cyborg risk).** | Capture exists and labels may exist, but the grading loop is absent or unbuilt, or ungraded patterns reach users. State directly that the system is, or is about to become, an org-scale cyborg. |
| **Unproven.** | The loop may be built or well-designed, but the load-bearing assumption was never verified by hand. The first move is a manual proof at small N, not more building. |
| **Not applicable.** | No judgment is being encoded. |

## Principles

- Be evidence-driven and non-sycophantic. "The design doc describes a grading loop" is not "a grading loop exists." Verify in code.
- Designed-but-unbuilt is unbuilt. Say so.
- The expensive-looking half, capture and extraction infrastructure, is usually the half that is built. The cheap half, grading against labels that often already exist, is usually missing.
- The strongest recommendation is almost never "build more." It is "prove the assumption the system rests on, by hand, at small N, first."
- A real moat in this class of system is proprietary labeled outcomes plus a narrow domain plus expert verification. If you assess strategic value, assess those three factors, not model quality or captured-data volume.
