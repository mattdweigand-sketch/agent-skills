# Worked Example: sales-os as of 2026-06-03

A real run on an agent harness, showing the inventory, the sort applied to load-bearing judgment, and the verdict in the exact output template. Use it to pattern-match shape and depth. Do not copy the numbers or open/closed status. Re-inventory before trusting any of this.

Treat the project facts and numbers below as illustrative, not current.

*Owner: Matt Weigand. Snapshot date: 2026-06-03. Last verified still representative: 2026-07-19. Writer-exposure field back-filled 2026-07-29 and consequence/template fields aligned 2026-08-04 from facts already recorded in this snapshot, not from a re-run. Refresh when `sales-os` composition changes materially or the snapshot becomes more than six months old.*

## Input

"$60-30-10 sales-os. It runs prep/debrief/close through an MCP harness backed by Open Brain, an off-repo record store."

## Inventory

- Prompt-model work: `harness-code/src/prompts/` per-step templates plus `_references/` ICP, voice, positioning, and segments documents that load on demand. Most load-bearing interpretation lives here.
- Owned data: `harness-code/data/voice-constraints.json` with 16 governed records plus off-repo Open Brain signals via `preamble.ts`. Off-repo weight has no repo line count, so do not undercount it from a file scan.
- Deterministic code: `src/lib/` validator suite. `voice-constraints.ts` validates the record contract, `voice-gate.ts` runs a Tier-1 phrase scan, and `close-validate.ts` enforces required report sections. A 20-test `npm test` gates it.

## Sort Applied To Load-Bearing Judgment

- Banned vocabulary: chosen fact, already migrated to data plus a code rail. Correctly placed.
- ICP boundaries, named lighthouse accounts, persona-to-stage map, trigger list, and segment vocabulary: chosen facts still in `_references/icp.md` and `segments.md`. They belong in data and are safe to move.
- Loss patterns and ICP trigger weights: predictive claims still stated as facts in prose. They belong in data only after an outcome grade. `close-validate.ts` checks that a Loss Patterns section exists; it does not grade the content.
- Stage advancement: `close-stage-flip.ts` writes the stage unconditionally. The required-field check is machine-checkable and a wrong advancement changes an authoritative deal state, so the consequence justifies pre-hoc enforcement in code.
- Output format, hypothesis-vs-observed marking, and deal-genome reasoning: steering. Correctly placed in prompts.

No unnecessary live decision was found in this snapshot; the model performs interpretation rather than merely sequencing a fixed pipeline. The file-splits-across-buckets case matters: `_references/icp.md` holds both chosen boundaries and predictive weights, so classify it rule by rule.

## Output

**Verdict:** mid-migration. The voice layer is correctly routed to data plus code, but the largest body of load-bearing judgment—ICP fit, triggers, segments, and loss patterns—is still prose.

**Estimated shape:** ~15/30/55 (owned data/deterministic code/prompt-model work). Medium confidence. Voice rules sit in owned data and deterministic code, but ICP, trigger, segment, and loss-pattern rules still live in prompt-model work, so data is thin and prompt is heavy. The estimate would shift if the off-repo records were weighted more heavily. This is descriptive, not a score.

**Rule basis:**
- Banned vocabulary: current owned data + deterministic code → correct owned data + deterministic code; writer human — checked.
- ICP boundaries, accounts, stages, triggers, and segment vocabulary: current prompt-model work → correct owned data; writer human — unchecked.
- Loss patterns and trigger weights: current prompt-model work → correct prompt-model work; writer human — unchecked.
- Stage advancement: current prompt-model work → correct deterministic code; writer model — unchecked.
- Output format, hypothesis marking, and deal-genome reasoning: current prompt-model work → correct prompt-model work; writer human — checked.

**Bucket findings:**
- Owned data (~15): holds `voice-constraints.json` and off-repo signals. Missing the chosen interpretation layer: ICP boundaries, persona weights, trigger list, and segment vocabulary.
- Deterministic code (~30): validates the voice contract, scans output, and enforces required report sections. It does not gate stage advancement on the required fields.
- Prompt-model work (~55): carries ICP scoring, trigger interpretation, and loss-pattern reasoning. Format and hypothesis marking are correct steering; the ICP and loss content is relocatable.

**Unnecessary live judgment:** none found.

**Writer exposure:** Open Brain deal-stage field—model-written via `close-stage-flip.ts`, unchecked because the flip runs unconditionally on upstream model output. `voice-constraints.json` is human-authored and governed.

**Cross-target duplication:** not assessed—the dated snapshot covered `sales-os` only and recorded no directly connected target for inspection.

**Biggest misallocation:** ICP definitions, triggers, and segment vocabulary trapped as prose in `_references/icp.md`. These chosen facts are the largest remaining source of decay exposure.

**Punch list (lowest risk first):**
1. Safe now: migrate ICP chosen facts, including AUM tier boundaries, persona-to-stage map, trigger list, and named anti-ICP signals, to governed records.
2. Safe now: add a deterministic required-field check before `close-stage-flip.ts` flips the stage.
3. Gated on evidence: keep loss patterns and ICP trigger weights non-authoritative until the outcome loop can grade them.
4. Leave: output format, hypothesis marking, and deal-genome reasoning scaffolds. They are genuine steering.
