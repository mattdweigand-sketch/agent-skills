# Worked Example: sales-os as of 2026-06-03

A real run on an agent harness, showing the inventory, the sort applied to
load-bearing judgment, and the verdict in the exact output template. Use it to
pattern-match shape and depth. Do not copy the numbers or the open/closed
status. Re-inventory before trusting any of this.

## Input

"Audit sales-os composition. It runs prep/debrief/close through an MCP harness
backed by Open Brain, an off-repo record store."

## Inventory

- Prompt surface: `harness-code/src/prompts/` with per-step templates plus
  `_references/` with ICP, voice, positioning, and segments docs that load on
  demand. Large. Most load-bearing interpretation is here.
- Owned data: `harness-code/data/voice-constraints.json` with 16 governed
  records plus off-repo Open Brain signals pulled via `preamble.ts`. The off-repo
  records carry real weight but have no repo line count, so do not undercount
  this bucket from a file scan.
- Deterministic code: `src/lib/` carries a validator suite.
  `voice-constraints.ts` validates the record contract, `voice-gate.ts` runs a
  deterministic Tier-1 phrase scan, and `close-validate.ts` enforces required
  report sections. A 20-test `npm test` gates it.

## Sort Applied To Load-Bearing Judgment

- Banned vocabulary: chosen fact, already migrated to data plus a code rail.
  Correctly placed.
- ICP boundaries, named lighthouse accounts, persona-to-stage map, trigger list,
  segment vocab: chosen facts, still prose in `_references/icp.md` and
  `segments.md`. Belong in data. Safe to move now.
- Loss patterns and ICP trigger weights: predictive, still prose stated as fact.
  Belong in data only after an outcome grade. `close-validate.ts` checks that a
  Loss Patterns section exists; it does not grade the content.
- Stage advancement: `close-stage-flip.ts` writes the stage unconditionally. The
  required-field check is machine-checkable but not enforced in code, so
  advancement rests on upstream model output.
- Output format, hypothesis-vs-observed marking, deal-genome reasoning:
  steering. Correctly in the prompts.

Note the file-splits-across-buckets case: `_references/icp.md` holds both chosen
boundaries and predictive weights, so classify rule by rule.

## Output

**Verdict:** Mid-migration. The voice layer is correctly routed to data plus
code, but the largest body of load-bearing judgment, ICP fit, triggers,
segments, and loss patterns, is still prose.

**Estimated ratio:** ~55/15/30 against the 60/30/10 target. Medium confidence.
Anchored on the load-bearing rule set: voice rules sit in data/code, but ICP,
trigger, segment, and loss-pattern rules still live in prose, so data is thin
and prompt is heavy. The number would shift if the off-repo records are weighted
up.

**Bucket findings:**
- Data (should be ~60, is ~15): holds `voice-constraints.json` and off-repo
  signals. Missing the chosen interpretation layer: ICP boundaries, persona
  weights, trigger list, segment vocab.
- Code (should be ~30, is ~30): strong. Validates the voice contract, scans
  output, enforces required report sections.
- Prompt (should be ~10, is ~55): carries ICP scoring, trigger interpretation,
  and loss-pattern reasoning. Format and hypothesis marking are correct steering;
  the ICP and loss content is relocatable.

**Biggest misallocation:** ICP definitions, triggers, and segment vocab trapped
as prose in `_references/icp.md`. Chosen facts tuned to nothing, read by the
model every run. This is the largest decay exposure now that voice is migrated.

**Punch list (lowest risk first):**
1. Safe now: migrate ICP chosen facts, AUM tier boundaries, persona-to-stage map,
   trigger list, and named anti-ICP signals to governed records.
2. Safe now: add a deterministic required-field check before
   `close-stage-flip.ts` flips the stage, so advancement stops resting on model
   output.
3. Gated on evidence: loss patterns and ICP trigger weights stay prose until the
   outcome loop can grade them. Moving ungraded patterns to authoritative data
   just relocates opinion.
4. Leave: output format, hypothesis marking, and deal-genome reasoning
   scaffolds. Genuine steering, correctly placed.

