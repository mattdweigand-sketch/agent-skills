# Composition Model

The buckets, routing sort, counting traps, and healthy or unhealthy shapes that back the 60/30/10 audit. Load this when running an audit; `SKILL.md` keeps only the invocation boundary, thesis, and procedure.

## The Three Buckets

**Data = the facts you chose, held as owned data.** The durable layer: ICP rules, banned phrases, stage gates, win stories, deal genomes, operating records, schemas, ledgers, and other facts that compound and survive model upgrades.

**Code = deterministic code and checks.** The rails, validators, orchestration, gates, scanners, test suites, and scripts that fetch the right records and enforce machine-checkable rules. A rule that must hold every time belongs outside the nondeterministic model.

**Prompt = prompt and model doing genuine interpretation.** Keep it small, steering-heavy, and concrete-fact-light. This is the perishable layer that needs retuning as models and harnesses change.

The numbers express a preferred direction and relative shape, not a target to optimize mechanically. Do not penalize a project merely because its estimated shape is not 60/30/10. Judge whether each rule is in the right home and whether live-model dependence is limited to work that genuinely requires interpretation. A different shape is healthy when the system's needs justify it; a superficially exact ratio is unhealthy when judgment is misrouted.

## Measurement Discipline

Measure by load-bearing judgment, not raw line count. A 2,000-line prose file of durable teaching is not automatically 2,000 lines of debt, and a 16-row JSON file can carry the policy that actually decides outputs. Weight each bucket by how much the system relies on what it holds.

Two counting traps:

- Owned data often lives off-repo. Database rows, memory stores, retrieved records, and vector stores carry real weight but may have no repo line count.
- Prompt surface is whatever loads into model context per run, not just files named like prompts. Always-on instructions and frequently injected reference documents count toward prompt load.

## Routing Sort

For every piece of judgment, ask in sequence:

1. **Steering or fact?** Output format, reasoning scaffolds, and hypothesis-vs-observed marking are steering. Steering stays in the prompt.
2. **If a fact: chosen or predictive?** A chosen fact is policy set by fiat, such as a banned phrase, boundary, or required field. Chosen facts become data. A predictive fact claims a correlation with an outcome and needs an outcome grade before becoming authoritative.
3. **Machine-checkable?** If a rule is mechanically verifiable, it also gets a deterministic check in code.
4. **Who writes it, and is the write checked?** Name the writer for each data store. Where the model writes, require a deterministic check on the way in or mark the store as model-authored and ungraded.

The unit of the sort is the rule, not the file. One document can split across buckets.

The fourth question is a direction constraint, not a placement rule. A human-chosen fact and a model-generated fact can look identical after both land in a data store. The strongest design has the model emit a reference to a governed value rather than author the value itself. Verifiable strings, numbers, and identifiers can carry deterministic checks. Paraphrase, summary, and inference usually cannot, which is a reason to keep them out of load-bearing positions.

## What Healthy And Unhealthy Look Like

Healthy: a thin prompt for format and genuine interpretation, an owned-data layer of chosen facts and graded rules, and deterministic code enforcing everything machine-checkable. New rules land as data records or code checks when those are their correct homes.

Unhealthy: prompt files are the largest load-bearing surface, policy is duplicated across prose files, reliability-critical rules are phrased as requests to the model, or the model writes authoritative records without a check.

---

*Owner: Matt Weigand. Last reviewed: 2026-07-30. Re-review when the routing sort or writer-exposure model changes materially.*
