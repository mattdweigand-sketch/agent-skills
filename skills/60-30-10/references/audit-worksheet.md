# 60-30-10 Audit Worksheet

Use this as an internal worksheet before writing the final verdict. Render a compact `Rule basis` in the final verdict; do not paste the whole worksheet unless the user asks for supporting detail.

## Inventory

| Bucket | Artifacts found | Loaded by default? | Notes |
|---|---|---:|---|
| Owned data |  | yes/no | Governed records, reference tables, schemas, eval sets, stored examples |
| Deterministic code |  | yes/no | Pipelines, tests, validators, gates, detectors, alerts, typed parsers |
| Prompt-model work |  | yes/no | System prompts, `SKILL.md` bodies, command wrappers, templates, injected references |

Use Notes for observed context delivery, required tool availability, and relevant permissions or processing flows. Mark unobserved behavior unverified; stored files alone do not prove runtime use.

## Rule Sort

| Rule or apparent judgment | Current home | Correct home or delete | Consequence if wrong once | Writer and check | Reason | Safe move? |
|---|---|---|---|---|---|---|
|  | owner/location; owned data/code/prompt-model | owned data/code/prompt-model/delete | low/medium/high; reversible/irreversible | human/code/model; mechanism and result | fixed sequence/steering/chosen fact/predictive/checkable | yes/no/evidence needed |

For each load-bearing rule, record its canonical owner in Current home, the observed delivery route in Reason, and the actual enforcement or checking mechanism in Writer and check. State the checked property, evidence scope, result, timing before/after the write, and whether failure blocks the authoritative write or promotion. Apply the [composition model's check-status rules](composition-model.md#routing-sort) to the final verdict's checked/unchecked summary. Classify maintained records by their actual use, including records held in Markdown, and keep current placement separate from recommended placement.

## Connected-target policy check

| Chosen policy | Homes found | Canonical owner | Reference or retrieval path | Finding |
|---|---|---|---|---|
|  |  |  |  | duplicate / single-owned / not assessed |

Record the bounded connected-target scope inspected:

## Shape Estimate

Anchor the estimate in the eight to twelve load-bearing rules, not raw line count.

| Bucket | Estimated share | Evidence |
|---|---:|---|
| Owned data |  |  |
| Deterministic code |  |  |
| Prompt-model work |  |  |

## Misallocation

Name one highest-leverage move:

- Move:
- From:
- To:
- Why it matters:
- Risk:

## Punch List

1.
2.
3.

---

*Owner: Matt Weigand. Last reviewed: 2026-10-06. Re-review when the output template, routing sort, or cross-target check changes.*
