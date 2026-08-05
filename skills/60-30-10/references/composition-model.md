# Composition Model

The buckets, routing sort, counting traps, and healthy or unhealthy shapes that back the 60/30/10 audit. In this skill the order is always **owned data / deterministic code / prompt-model work**; code/rules/AI is a different heuristic. Load this when running an audit; `SKILL.md` keeps only the invocation boundary, thesis, and procedure.

## The Three Buckets

**Owned data = the facts and policies you chose.** The durable layer: ICP rules, banned phrases, stage gates, win stories, deal genomes, operating records, schemas, ledgers, and other governed facts that compound and survive model upgrades.

**Deterministic code = fixed execution and consequence-worthy checks.** The pipelines, rails, validators, orchestration, gates, scanners, test suites, detectors, alerts, and scripts that fetch the right records and handle machine-checkable rules. A rule that must hold every time belongs outside the nondeterministic model. Code may prevent a failure before action or observe and alert on it afterward; that is a mechanism distinction inside this bucket, not a fourth bucket.

**Prompt-model work = prompt and model doing genuine interpretation.** Keep it small, steering-heavy, and concrete-fact-light. This is the perishable layer that needs retuning as models and harnesses change.

The numbers express a preferred direction and relative shape, not a target to optimize mechanically. Do not penalize a project merely because its estimated shape is not 60/30/10. Judge whether each rule is in the right home and whether prompt-model dependence is limited to work that genuinely requires interpretation. A different shape is healthy when the system's needs justify it; a superficially exact ratio is unhealthy when judgment is misrouted.

## Measurement Discipline

Measure by load-bearing judgment, not raw line count. A 2,000-line prose file of durable teaching is not automatically 2,000 lines of debt, and a 16-row JSON file can carry the policy that actually decides outputs. Weight each bucket by how much the system relies on what it holds.

Two counting traps:

- Owned data often lives off-repo. Database rows, memory stores, retrieved records, and vector stores carry real weight but may have no repo line count.
- Prompt-model surface is whatever loads into model context per run, not just files named like prompts. Always-on instructions and frequently injected reference documents count toward prompt-model load.

## Routing Sort

For every apparent piece of judgment, ask in sequence:

0. **Does this need live judgment at all?** If the inputs, order, and outcome rule are fixed, the "decision" is an over-specified pipeline. Delete the live judgment and implement the sequence deterministically. This finding does not relocate to a bucket.
1. **Steering or fact?** Output format, reasoning scaffolds, and hypothesis-vs-observed marking are steering. Genuine steering stays in prompt-model work.
2. **If a fact: chosen or predictive?** A chosen fact is policy set by fiat, such as a banned phrase, boundary, or required field. Chosen facts become owned data. A predictive fact claims a correlation with an outcome and needs an outcome grade before becoming authoritative.
3. **Machine-checkable, and consequential if wrong once?** Mechanical verifiability makes a code check possible. High-consequence misses get deterministic protection. Low-consequence checkable preferences may remain prompt-model steering without becoming a finding when a code path would cost more than the failure. Choose pre-hoc enforcement when the action must be blocked; choose post-hoc detection or alerting when observation plus recovery is sufficient.
4. **Who writes it, and is the write checked?** Name the writer for each owned-data store. Where the model writes, require a deterministic check on the way in for authoritative, consequence-bearing values or mark the store as model-authored and ungraded.
5. **Where else does the same chosen policy live?** Inspect directly connected targets that consume, generate, or restate it. If the policy has multiple independent homes, name one owner and make the other surfaces reference or retrieve it.

The unit of the sort is the rule, not the file. One document can split across buckets.

The fourth question is a direction constraint, not a placement rule. A human-chosen fact and a model-generated fact can look identical after both land in an owned-data store. The strongest design has the model emit a reference to a governed value rather than author the value itself. Verifiable strings, numbers, and identifiers can carry deterministic checks when their consequence justifies one. Paraphrase, summary, and inference usually cannot, which is a reason to keep them out of load-bearing positions.

The fifth question crosses target boundaries but stays bounded. Search only connected surfaces named by dependencies, generators, workflow routes, deployment config, or user-provided scope. Do not turn a composition audit into an organization-wide architecture review.

## What Healthy And Unhealthy Look Like

Healthy: thin prompt-model work for format and genuine interpretation, an owned-data layer of chosen facts and graded rules, and deterministic code handling fixed sequences plus consequence-worthy checks. New rules land in their correct homes, unnecessary model decisions disappear, and shared policy has one owner across connected targets.

Unhealthy: prompt-model files are the largest load-bearing surface, policy is duplicated across prose files or connected targets, fixed pipelines are modeled as live decisions, reliability-critical rules are phrased as requests to the model, or the model writes authoritative records without a consequence-appropriate check.

---

*Owner: Matt Weigand. Last reviewed: 2026-08-04. Re-review when the routing sort, consequence model, cross-target boundary, or writer-exposure model changes materially.*
