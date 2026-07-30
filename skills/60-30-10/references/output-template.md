# Output Template

Every 60/30/10 audit renders its verdict in this exact shape. Load when writing the final output.

## Template

```text
**Verdict:** [inverted / prose-heavy / mid-migration / roughly balanced / healthy]. One line on why. Use mid-migration when some layers are routed right and others are not.

**Estimated shape:** ~[X/Y/Z]. [One line on confidence and what drove the estimate.] This is descriptive, not a score; explain whether the underlying judgment is routed well regardless of numerical proximity to 60/30/10.

**Bucket findings:**
- Data (~[X]): [what is held; what durable fact is missing from here]
- Code (~[Y]): [what is enforced; what reliability-critical rule is not]
- Prompt (~[Z]): [what is steering and correct; what is relocatable]

**Writer exposure:** [each data store the model writes into and whether a deterministic check sits between the writer and the store; `none` when every store is human- or code-authored]

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
| Estimated shape | Three integers summing to approximately 100, formatted `~X/Y/Z` in Data/Code/Prompt order. Anchor them in the eight to twelve load-bearing rules and include low, medium, or high confidence. |
| Bucket findings | Three bullets, one per bucket. Each names what is currently held and what belongs there but is missing. |
| Writer exposure | Each model-written data store, named by path when available, with `checked` or `unchecked`. Write `none` when no store is model-written; never omit the field. |
| Biggest misallocation | One concrete move, identified by a file path or rule name rather than a broad category. |
| Punch list | Ordered by leverage and lowest risk first. Each item is `Safe now`, `Gated on evidence`, or `Leave`. Include at least one `Leave` entry so genuine steering is acknowledged. |

Outputs that skip fields, reverse the Data/Code/Prompt order, invent verdict values, or state a shape without confidence are incomplete.

---

*Owner: Matt Weigand. Last reviewed: 2026-07-30. Re-review when an audit surfaces a rule that does not fit the template.*
