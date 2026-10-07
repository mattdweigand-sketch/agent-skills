# Composition Model

The buckets, routing sort, counting traps, and healthy or unhealthy shapes that back the 60/30/10 audit. In this skill the order is always **owned data / deterministic code / prompt-model work**. Load this when running an audit; `SKILL.md` keeps only the invocation boundary, thesis, and procedure.

## Source framings

Jake Van Clief's [How I'd Learn AI From Zero in 2026, 28:34-29:25](https://www.youtube.com/watch?v=6AzLk2-kWyY&t=1714s) revises the teaching heuristic to 60% data, questions, and thinking / 30% existing tools / 10% AI, and describes his older version as code, routing, and AI calls. The code/rules/AI heuristic previously cited by this package is also a separate framing.

This skill retains an operational adaptation: classify each load-bearing rule by its durable owner, execution, and checking mechanism. Thinking is not automatically owned data, an existing tool is not automatically deterministic, and AI activity does not map one-to-one to prompt-model judgment. The course and this skill both use rough directional numbers; neither supplies a numerical compliance target.

The 2026-10-07 comparison used all 1,456 English auto-generated caption segments, ending at a caption window of 54:05.520; timestamps are approximate and the endpoint is not a verified video duration. JSON capture SHA-256: `62e1a6b911c4274905c20416e22e2e41a4b31fdf3e5590b8a9884144367f5b87`. Captions are not bundled, and audiovisual content and linked materials were not independently verified.

## The Three Buckets

**Owned data = the facts and policies you chose.** The durable layer: ICP rules, banned phrases, stage gates, win stories, deal genomes, operating records, schemas, ledgers, and other governed facts that compound and survive model upgrades.

**Deterministic code = fixed execution and consequence-worthy checks.** The pipelines, rails, validators, orchestration, gates, scanners, test suites, detectors, alerts, and scripts that fetch the right records and handle machine-checkable rules. A rule that must hold every time belongs outside the nondeterministic model. Code may prevent a failure before action or observe and alert on it afterward; that is a mechanism distinction inside this bucket, not a fourth bucket.

Evals measure behavior; deterministic controls enforce machine-checkable rules. You cannot eval your way to deterministic behavior, and deterministic execution alone does not establish semantic correctness.

**Prompt-model work = prompt and model doing genuine interpretation.** Keep it small, steering-heavy, and concrete-fact-light. This is the perishable layer that needs retuning as models and harnesses change.

The numbers express a preferred direction and relative shape, not a target to optimize mechanically. Do not penalize a project merely because its estimated shape is not 60/30/10. Judge whether each rule is in the right home and whether prompt-model dependence is limited to work that genuinely requires interpretation. A different shape is healthy when the system's needs justify it; a superficially exact ratio is unhealthy when judgment is misrouted.

## Measurement Discipline

Measure by load-bearing judgment, not raw line count. A 2,000-line prose file of durable teaching is not automatically 2,000 lines of debt, and a 16-row JSON file can carry the policy that actually decides outputs. Weight each bucket by how much the system relies on what it holds.

Two counting traps:

- Owned data often lives off-repo. Database rows, memory stores, retrieved records, and vector stores carry real weight but may have no repo line count.
- Prompt-model surface is whatever loads into model context per run, not just files named like prompts. Always-on instructions and frequently injected reference documents count toward prompt-model load.

For each load-bearing rule, distinguish its canonical owner and location, its delivery into model context, and its execution or checking mechanism. Human-owned policy stored in Markdown can be durable data while compliance still depends on the model. Count those responsibilities, not the file extension; avoid counting the same policy twice merely because it is loaded.

Verify delivery and required tool availability from observed reads and use. Tie access claims to actual permissions and data-residency claims to actual processing and network flows. A folder label or local storage location alone does not establish either.

## Routing Sort

For every apparent piece of judgment, ask in sequence:

0. **Does this need live judgment at all?** If the inputs, order, and outcome rule are fixed, the "decision" is an over-specified pipeline. Delete the live judgment and implement the sequence deterministically. This finding does not relocate to a bucket.
1. **Steering or fact?** Output format, reasoning scaffolds, and hypothesis-vs-observed marking are steering. Genuine steering stays in prompt-model work.
2. **If a fact: chosen or predictive?** A chosen fact is policy set by fiat, such as a banned phrase, boundary, or required field. Chosen facts become owned data. A predictive fact claims a correlation with an outcome and needs an outcome grade before becoming authoritative.
3. **Machine-checkable, and consequential if wrong once?** Mechanical verifiability makes a code check possible. High-consequence misses get deterministic protection. Low-consequence checkable preferences may remain prompt-model steering without becoming a finding when a code path would cost more than the failure. Choose pre-hoc enforcement when the action must be blocked; choose post-hoc detection or alerting when observation plus recovery is sufficient.
4. **Who writes it, and is the write checked?** Name the writer for each owned-data store. Where the model writes, require a deterministic check before an authoritative, consequence-bearing write or promotion; otherwise mark the value as model-authored and ungraded. A passing check after that authoritative write does not satisfy this requirement.
5. **Where else does the same chosen policy live?** Inspect directly connected targets that consume, generate, or restate it. If the policy has multiple independent homes, name one owner and make the other surfaces reference or retrieve it.

The unit of the sort is the rule, not the file. One document can split across buckets.

The fourth question is a direction constraint, not a placement rule. A human-chosen fact and a model-generated fact can look identical after both land in an owned-data store. The strongest design has the model emit a reference to a governed value rather than author the value itself. Verifiable strings, numbers, and identifiers can carry deterministic checks when their consequence justifies one. Paraphrase, summary, and inference usually cannot, which is a reason to keep them out of load-bearing positions.

Preserve source observations separately from model-derived proposals and chosen policy. Keep units, time periods, and provenance with consequential values. A schema-valid claim remains a proposal until appropriately checked: arithmetic can pass while the selected period is wrong. Code that invokes a learned model does not make its semantic output a deterministic check.

Record passed, failed, skipped, and unverified checks for the property each check actually examines. Wrapper success, file creation, or a required section's presence does not grade its meaning. Name the human decision the workflow supports and the consequence of an incorrect result before recommending additional machinery.

Render `checked` only when a relevant deterministic check has evidence of passing for the named property and scope. The check may run before or after a write. Render a missing, failed, skipped, or unverified check as `unchecked`, and name that state. Observed runs, tests, or logs can supply evidence; identify their scope rather than treating tests as proof that a live write path invokes the check. Writer exposure names the property, evidence, timing, and whether failure blocks the authoritative write or promotion. A passing post-write check can render as `checked` while missing pre-write protection remains a finding under question 4.

The fifth question crosses target boundaries but stays bounded. Search only connected surfaces named by dependencies, generators, workflow routes, deployment config, or user-provided scope. Do not turn a composition audit into an organization-wide architecture review.

## What Healthy And Unhealthy Look Like

Healthy: thin prompt-model work for format and genuine interpretation, an owned-data layer of chosen facts and graded rules, and deterministic code handling fixed sequences plus consequence-worthy checks. New rules land in their correct homes, unnecessary model decisions disappear, and shared policy has one owner across connected targets.

Unhealthy: prompt-model files are the largest load-bearing surface, policy is duplicated across prose files or connected targets, fixed pipelines are modeled as live decisions, reliability-critical rules are phrased as requests to the model, or the model writes authoritative records without a consequence-appropriate check.

---

Provenance: the 2026-10-06 source-fidelity, delivery-evidence, and review refinements are local synthesis from the review of Jake Van Clief's [Augmenting Human Intellect](https://jakevanclief.substack.com/p/augmenting-human-intellect), the [ICM paper v2, section 6.1](https://arxiv.org/html/2603.16021v2), and the supplied `workspace-blueprint.zip` and `files.zip` (nested Eduba `vault-toolkit`, client-delivery discovery, review, and handoff contracts). The 2026-10-07 course comparison is recorded under [source framings](#source-framings). The buckets and directional use of the ratio remain this skill's model.

*Owner: Matt Weigand. Last reviewed: 2026-10-07. Re-review when the routing sort, consequence model, cross-target boundary, or writer-exposure model changes materially.*
