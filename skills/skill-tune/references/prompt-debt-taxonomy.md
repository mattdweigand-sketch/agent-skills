# Prompt Debt Taxonomy

Use this reference with `skill-tune` when classifying instructions and choosing actions.

## Instruction Buckets

Classify each meaningful instruction by format, fate, and verification.

| Bucket | Meaning | Preferred home |
|---|---|---|
| Durable | Stable facts, principles, reusable workflow contracts | Workflow contracts in `SKILL.md`; repo facts in canonical project docs; bulky context in references; factual claims need provenance or freshness. |
| Perishable | Model-specific steering, tone hacks, brittle behavioral nudges | Stay stock, delete, shorten, isolate, or put on an audit clock. |
| Executable | Anything a machine can check or perform reliably | Scripts, tests, schemas, hooks. |
| Reference | Bulky examples, API details, domain docs, templates | `references/` or `assets/`. |
| Duplicate | Rule already owned by a canonical file or platform default | Replace with a pointer or remove. |

## Fate Test

- If it breaks on the next model, rent it and keep it minimal.
- If the next model can regenerate it, treat it as commodity infrastructure.
- If it depends on owned outcome context, preserve its provenance.

## Verification Tiers

| Tier | Meaning | Preferred treatment |
|---|---|---|
| Tier 1 | Machine-checkable rules | Move into scripts, tests, schemas, hooks, or deterministic validators when practical. |
| Tier 2 | Expert-checkable rules | Keep as review criteria or eval evidence; do not pretend they are deterministic. |
| Tier 3 | Genuine judgment | May stay as prompt steering when no better owner exists. |

## Actions

Use one action per finding.

| Action | Use when |
|---|---|
| keep | The instruction has a justified owner and load path. |
| stay stock | The platform default is enough; remove local steering. |
| shorten | The rule is useful but bloated. |
| move to reference | The material is stable, bulky, and only needed after routing. |
| move to script/test/schema/hook | The rule is machine-checkable. |
| add provenance | The claim is factual, current-state-dependent, or derived from an owner document. |
| delete | The rule is stale, duplicated, or unnecessary. |
| retune | Triggering, routing, or boundaries need narrower wording. |
| needs owner decision | The artifact cannot be safely changed without a source-of-authority decision. |
