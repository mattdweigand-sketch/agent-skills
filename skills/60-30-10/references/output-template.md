# Output Template

Every 60/30/10 audit renders its verdict in this exact shape. Load when writing the final output.

## Template

```text
**Verdict:** [inverted / prose-heavy / mid-migration / roughly balanced / healthy]. One line on why. Use mid-migration when some layers are routed right and others are not.

**Estimated shape:** ~[X/Y/Z]. [One line on confidence and what drove the estimate.] This is descriptive, not a score; explain whether the underlying judgment is routed well regardless of numerical proximity to 60/30/10.

**Bucket findings:**
- Owned data (~[X]): [what is held; what durable fact or policy is missing from here]
- Deterministic code (~[Y]): [what fixed execution, pre-hoc enforcement, or post-hoc detection exists; what consequence-worthy rule is missing]
- Prompt-model work (~[Z]): [what genuine interpretation or steering is correct; what is relocatable]

**Unnecessary live judgment:** [the model decision that should become a fixed pipeline, or `none found`]

**Writer exposure:** [each data store the model writes into and whether a deterministic check sits between the writer and the store; `none` when every store is human- or code-authored]

**Cross-target duplication:** [duplicated chosen policy, its current homes, and one canonical owner; `none found within [bounded scope]`; or `not assessed—[why no connected target was inspectable]`]

**Biggest misallocation:** [the single highest-leverage move, named concretely.]

**Punch list (lowest risk first):**
1. Safe now: [chosen policy to data, or machine-checkable rule to code]
2. Safe now: [...]
3. Gated on evidence: [predictive rule that needs an outcome grade before it moves; include only when the audit surfaces one]
4. Leave: [genuine steering, correctly placed]
```

## Field Specification

| Field | Content |
|---|---|
| Verdict | Exactly one of `inverted`, `prose-heavy`, `mid-migration`, `roughly balanced`, or `healthy`, plus one sentence explaining why. |
| Estimated shape | Three integers summing to approximately 100, formatted `~X/Y/Z` in owned-data / deterministic-code / prompt-model order. Anchor them in the eight to twelve load-bearing rules and include low, medium, or high confidence. |
| Bucket findings | Three bullets in owned-data / deterministic-code / prompt-model order. Each names what is currently held and what belongs there but is missing. The code bullet distinguishes pre-hoc enforcement from post-hoc detection when relevant. |
| Unnecessary live judgment | Name the highest-leverage model decision that is really a fixed sequence and should be deleted, or write `none found`. |
| Writer exposure | Each model-written data store, named by path when available, with `checked` or `unchecked`. Write `none` when no store is model-written; never omit the field. |
| Cross-target duplication | Name a duplicated chosen policy, its homes, and canonical owner. If none was found, state the bounded connected-target scope. If no connected target was inspectable, say `not assessed` and why. |
| Biggest misallocation | One concrete move, identified by a file path or rule name rather than a broad category. |
| Punch list | Ordered by leverage and lowest risk first. Each item is `Safe now`, `Gated on evidence`, or `Leave`. Include at least one `Leave` entry so genuine steering is acknowledged. |

Outputs that skip fields, reverse the owned-data / deterministic-code / prompt-model order, invent verdict values, or state a shape without confidence are incomplete.

---

*Owner: Matt Weigand. Last reviewed: 2026-08-04. Re-review when an audit surfaces a rule that does not fit the template.*
