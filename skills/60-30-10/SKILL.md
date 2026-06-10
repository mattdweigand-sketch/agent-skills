---
name: 60-30-10
description: >
  Evaluate how a project allocates its judgment across owned data, deterministic
  code, and live model. Use when the user says "60/30/10", "composition audit",
  "audit this project's structure", "is this allocated right", "what's the
  60/30/10 here", "is too much in the prompt", "where does the judgment live",
  "budget check", or runs /60-30-10, or when reviewing an agent/harness/AI system for
  whether durable value sits in data and code versus trapped in perishable prose.
  Pairs with `cyborg-check`, which checks whether judgment is graded against
  outcomes, but this skill checks where judgment lives, not whether it is verified.
metadata:
  version: 0.3.0
  user-invocable: true
---

# Composition Audit

Evaluate where a project keeps its judgment, and whether the allocation matches
the durable shape: mostly owned data, partly deterministic code, only a thin
layer of live model.

The thesis this enforces: every piece of judgment has a right home, and the
default, prose in a prompt, is usually the wrong one. A healthy system routes
each piece to the bucket that fits, and the result is roughly 60% database, 30%
code, 10% model. The naive build inverts that ratio, traps load-bearing judgment
in prompt text, and decays silently on every model upgrade. This skill estimates
the current ratio, names the biggest misallocation, and gives a punch list of
moves. It produces an inline verdict. It does not write a file unless asked.

## Step 0: Applicability Gate

This applies to any system that encodes judgment as prompts, data, or code: an
agent harness, a sales/intelligence tool, an eval pipeline, a scoring or
recommendation engine, a RAG app, or a workflow built on `AGENTS.md`, `CLAUDE.md`,
skills, MCP, or similar agent context.

If the project has no model and no encoded judgment, such as a plain CRUD app, a
static site, or a byte-moving pipeline, say so in one sentence and stop. Do not
force the rubric.

## The Three Buckets

**60% database = the facts you chose, held as owned data.** This is the durable
layer: ICP rules, banned phrases, stage gates, win stories, deal genomes. It is
the biggest bucket because most of what feels like "the system's intelligence"
is accumulated fact, not live reasoning.

**30% automation = deterministic code and checks.** The rails, validators,
scanners, gates, and orchestration that fetch the right records and enforce
machine-checkable rules. This is the only bucket that crosses the reliability
ceiling, so anything that has to be reliable belongs here, not in the 10.

**10% LLM/AI = the prompt and model doing genuine interpretation.** Keep it
small, concrete, and perishable. It should steer the task and interpret what
cannot be reduced to data or code.

The percentages are a target shape, not a precise quota. The point is the order
of magnitude: data should dwarf code, and code should dwarf prompt. If prompt is
the biggest bucket, the build is inverted.

Measure by load-bearing judgment, not raw line count. A 2,000-line prose file of
durable teaching is not automatically 2,000 lines of debt, and a 16-row JSON
file can carry the policy that actually decides outputs. Weight each bucket by
how much the system relies on what it holds.

Two counting traps:

- Owned data often lives off-repo. Database rows, memory stores, retrieved
  records, and vector stores carry real weight in the 60 but may have no repo
  line count.
- Prompt surface is whatever loads into model context per run, not just files
  named like prompts. Always-on system prompts and frequently injected reference
  docs count toward the 10.

## Routing Sort

For every piece of judgment, ask in sequence:

1. **Steering or fact?** Output format, reasoning scaffolds, and
   hypothesis-vs-observed marking are steering. Steering stays in the prompt.
2. **If a fact: chosen or predictive?** A chosen fact is policy set by fiat, such
   as a banned phrase, ICP boundary, or required field. Chosen facts become data.
   A predictive fact claims a correlation with outcome. Predictive facts need an
   outcome grade before they become authoritative.
3. **Machine-checkable?** If a rule is mechanically verifiable, it also gets a
   deterministic check in code.

The unit of the sort is the rule, not the file. One document can split across
buckets.

## Procedure

1. **Inventory.** Find where judgment physically lives. List prompt surface,
   owned data, and deterministic code. Correct for off-repo data and
   actually-loaded reference docs.
2. **Classify the load-bearing judgment.** Name the top eight to twelve rules
   that decide outputs. Record where each currently lives and where it belongs.
3. **Estimate the ratio.** Anchor the estimate in that rule set, not a vibe. Give
   an approximate current split against 60/30/10 and state confidence.
4. **Name the biggest misallocation.** Identify the single highest-leverage move.
5. **Punch list.** Give concrete moves ordered by leverage and lowest risk first.
   Separate safe moves from changes gated on evidence.

Use `references/audit-worksheet.md` as the internal worksheet when the system is
large enough that the ratio could otherwise become a vibe.

## What Good And Bad Look Like

Good: a thin prompt for format and genuine interpretation, a fat owned-data
layer of chosen facts and graded rules, and deterministic code enforcing
everything machine-checkable. New rules land as data rows or code checks, not
prompt edits.

Bad: `AGENTS.md` and prompt templates are the biggest surface, the same policy is
duplicated across prose files, reliability-critical rules are phrased as polite
requests to the model, and a model upgrade can degrade behavior silently.

## Output Format

Use this exact template:

```text
**Verdict:** [inverted / prose-heavy / mid-migration / roughly balanced / healthy]. One line on why. Use mid-migration when some layers are routed right and others are not.

**Estimated ratio:** ~[X/Y/Z] against the 60/30/10 target. [One line on confidence and what drove the estimate.]

**Bucket findings:**
- Data (should be ~60, is ~[X]): [what is held; what durable fact is missing from here]
- Code (should be ~30, is ~[Y]): [what is enforced; what reliability-critical rule is not]
- Prompt (should be ~10, is ~[Z]): [what is steering and correct; what is relocatable]

**Biggest misallocation:** [the single highest-leverage move, named concretely.]

**Punch list (lowest risk first):**
1. Safe now: [chosen policy to data, or machine-checkable rule to code]
2. Safe now: [...]
3. Gated on evidence: [predictive rule that needs an outcome grade before it moves]
4. Leave: [genuine steering, correctly placed]
```

Read `references/worked-example.md` before a first run to calibrate depth.
Use `references/audit-worksheet.md` for repeatable inventory and rule sorting.

## Source

This skill operationalizes four ideas: judgment routing, prompt technical debt,
storage versus enforcement, and context as a durable advantage. The skill body is
self-contained; external notes can deepen the concepts but are not required.
