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

## Companion example: client follow-up

Authored on 2026-10-06. This fictional routing exercise complements the dated audit above; it is not another recorded run or a measured composition estimate.

Request: "Draft a client follow-up from the planning notes." Chosen scope: produce a draft for the account owner to review. A model's proposed interpretation that the client needs a delivery commitment remains an assumption. The human decision is what to communicate next; an unsupported promise could mislead the client.

Source observation: `inputs/planning-note-01-v1.md`, Next steps, says, "Iris will prepare a demo. The delivery date is still open." A suitable draft says, "Iris will prepare the demo; the delivery date remains open." Keep that source location in review notes. The filenames below are illustrative, not bundled fixtures.

| Load-bearing item | Owner and delivery | Mechanism and limit |
|---|---|---|
| Chosen draft scope | Account owner; existing local context is the maintained home and the task route delivers it | Human-owned policy is data; applying it from prose remains model-dependent. A source note cannot authorize sending. |
| Action, owner, and open date | Original note is evidence; the task route names the exact input and the draft retains its source location | Model extracts a proposal. Review checks it against the passage; field presence or a schema check cannot establish faithful meaning. |
| Format and source selection | Existing context defines the required fields and selected input | If a miss has sufficient consequence, code can check field presence or exact source-version equality. Without an implemented and observed check, enforcement remains model-dependent and unverified. |
| Client-ready wording | Model drafts; account owner reviews the selected `drafts/follow-up-v1.md` in the actual receiving preview | Acceptance includes the action and owner, visible date uncertainty, and usable next steps. Reject an invented Tuesday commitment. Code calling a model judge still supplies a learned judgment. |
| Changed evidence | Selected `inputs/planning-note-01-v2.md` changes the owner to Morgan; the date stays open | Reconsider the owner claim and affected draft readiness. Review of v1 does not establish readiness for a revised draft. |

Use the existing review record to identify the exact source and reviewed output. Observe the required reads and tool use in a real run before calling the route verified. Keep one scope owner; select a frozen copy explicitly if a run needs one. A wrapper that completes while a source check is skipped cannot claim that check passed.

For this reversible draft, repair the unsupported claim and check another relevant case before adding machinery. A consequential automated action may justify a fixed check before execution, but semantic fidelity still needs appropriate review. The [composition model](composition-model.md) owns these distinctions; the [worksheet](audit-worksheet.md) records the rule-level evidence.

Provenance: local synthesis from the 2026-10-06 review of Jake Van Clief's [Augmenting Human Intellect](https://jakevanclief.substack.com/p/augmenting-human-intellect), the [ICM paper v2, section 6.1](https://arxiv.org/html/2603.16021v2), and the supplied `workspace-blueprint.zip` and `files.zip` (nested Eduba `vault-toolkit`, client-delivery discovery, review, and handoff contracts). The buckets and directional use of the ratio remain this skill's model; the sources' code/rules/AI heuristic is a different framing.
