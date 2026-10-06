# Worked Example: sales-os as of 2026-06-03

A real run on an agent harness, showing the inventory, the sort applied to load-bearing judgment, and the verdict in the exact output template. Use it to pattern-match shape and depth. Do not copy the numbers or open/closed status. Re-inventory before trusting any of this.

Treat the project facts and numbers below as illustrative, not current.

*Owner: Matt Weigand. Snapshot date: 2026-06-03. Last verified still representative: 2026-07-19. Writer-exposure field back-filled 2026-07-29 and consequence/template fields aligned 2026-08-04. Placement and check-status wording corrected 2026-10-06 from recorded facts, not a re-run; the original numerical estimate is retained as historical. Refresh when `sales-os` composition changes materially or the snapshot becomes more than six months old.*

## Input

"$60-30-10 sales-os. It runs prep/debrief/close through an MCP harness backed by Open Brain, an off-repo record store."

## Inventory

- Prompt-model work: `harness-code/src/prompts/` per-step templates and interpretation or policy application driven by `_references/` documents loaded on demand. Loading a chosen policy does not change the policy itself from data into prompt-model work.
- Owned data: `harness-code/data/voice-constraints.json` with 16 governed records, chosen ICP and segment policies in `_references/icp.md` and `segments.md`, and off-repo Open Brain signals via `preamble.ts`. Markdown can hold maintained records. Off-repo weight has no repo line count, so do not undercount it from a file scan.
- Deterministic code: `src/lib/` validator suite and the fixed write in `close-stage-flip.ts`. `voice-constraints.ts` validates the record contract, `voice-gate.ts` runs a Tier-1 phrase scan, and `close-validate.ts` enforces required report sections. The snapshot names a 20-test `npm test` gate but does not retain results or establish the checks' timing on live writes.

## Sort Applied To Load-Bearing Judgment

- Banned vocabulary: chosen fact in data plus a code rail. Correctly placed; the named validator does not establish a passing result for a particular run.
- ICP boundaries, named lighthouse accounts, persona-to-stage map, trigger list, and segment vocabulary: chosen policy records in `_references/icp.md` and `segments.md` are owned data. Their application from loaded instructions depends on the model. Keep one maintained policy owner and add deterministic checks for machine-checkable uses whose consequence justifies them; changing the file format alone would not supply enforcement.
- Loss patterns and ICP trigger weights: predictive claims still stated as facts in prose. They belong in data only after an outcome grade. `close-validate.ts` checks that a Loss Patterns section exists; it does not grade the content.
- Stage advancement: `close-stage-flip.ts` writes the stage unconditionally. The required-field check is machine-checkable and a wrong advancement changes an authoritative deal state, so the consequence justifies pre-hoc enforcement in code.
- Output format, hypothesis-vs-observed marking, and deal-genome reasoning: steering. Correctly placed in prompts.

No unnecessary live decision was found in this snapshot; the model performs interpretation rather than merely sequencing a fixed pipeline. The file-splits-across-buckets case matters: `_references/icp.md` holds both chosen boundaries and predictive weights, so classify it rule by rule. The snapshot identifies checks but records no passing results for their named properties; the writer/check summaries below therefore render them as unchecked, with results unverified.

## Output

**Verdict:** mid-migration. The voice policy has a data owner and code checks, but consequential stage writes lack a gate and some chosen policies still depend on model application while predictive claims remain ungraded.

**Estimated shape:** ~15/30/55 (owned data/deterministic code/prompt-model work). Low confidence under the current definitions: this is the original snapshot estimate, retained for provenance rather than recomputed. The corrected rule basis counts chosen Markdown policies as data and fixed writes as code; a fresh audit must reweight those responsibilities and off-repo records before using a new split. This historical estimate is descriptive, not a score or a current allocation claim.

**Rule basis:**
- Banned vocabulary: current owned data + deterministic code → correct owned data + deterministic code; writer human — unchecked.
- ICP boundaries, accounts, stages, triggers, and segment vocabulary: current owned data + prompt-model work → correct owned data + deterministic code + prompt-model work; writer human — unchecked.
- Loss patterns and trigger weights: current prompt-model work → correct prompt-model work; writer human — unchecked.
- Stage advancement gate: current prompt-model work + deterministic code → correct deterministic code; writer model — unchecked.
- Output format, hypothesis marking, and deal-genome reasoning: current prompt-model work + deterministic code → correct prompt-model work + deterministic code; writer human — unchecked.

**Bucket findings:**
- Owned data (~15): holds `voice-constraints.json`, chosen policy records in Markdown, and off-repo signals. Predictive loss patterns and trigger weights are not authoritative without outcome grading.
- Deterministic code (~30): validates the voice contract, scans output, checks required report sections, and performs the fixed stage write. Check results and timing are unverified; the stage write lacks pre-write enforcement of the required fields.
- Prompt-model work (~55): applies ICP policy and interprets triggers and loss patterns. Format and hypothesis marking are genuine steering; consequential, machine-checkable policy application needs code protection.

**Unnecessary live judgment:** none found.

**Writer exposure:** Open Brain deal-stage field—model-written via `close-stage-flip.ts`, unchecked: no required-field check blocks the authoritative write, and no passing post-write check is recorded. The recorded mechanism writes unconditionally on upstream model output. `voice-constraints.json` is human-authored; its contract and phrase checks have unverified results and timing in this snapshot.

**Cross-target duplication:** not assessed—the dated snapshot covered `sales-os` only and recorded no directly connected target for inspection.

**Biggest misallocation:** The required-field rule does not gate `close-stage-flip.ts` before it changes authoritative deal state.

**Punch list (lowest risk first):**
1. Safe now: keep one governed owner for ICP chosen policies, including AUM tier boundaries, persona-to-stage map, trigger list, and named anti-ICP signals; make consuming prompts reference it. Maintained Markdown records can remain in place.
2. Safe now: add a deterministic required-field check before `close-stage-flip.ts` flips the stage.
3. Gated on evidence: keep loss patterns and ICP trigger weights non-authoritative until the outcome loop can grade them.
4. Leave: output format, hypothesis marking, and deal-genome reasoning scaffolds. They are genuine steering.
