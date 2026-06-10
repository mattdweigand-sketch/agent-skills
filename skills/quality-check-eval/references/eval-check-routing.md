# Eval Check Routing

Use this reference with `quality-check-eval`. It owns the stable action taxonomy, scoring fields, deterministic alternatives, and report template.

## Recommendation Actions

Choose exactly one action per check.

| Action | Meaning |
|---|---|
| `PROMOTE` | Build an LLM judge because deterministic checks are insufficient and the check is frequent, important, and evidence-backed. |
| `AUTO-CONVERT` | Replace with a deterministic check such as a parser, schema, regex, count, threshold, local command, or metadata query. |
| `KEEP-MANUAL` | Keep human review because judgment matters but automation is not worth it yet. |
| `DROP` | Remove from the active quality gate because it is low signal, unclear, duplicative, or has no observed value. |

## Scoring Fields

| Field | Values | Use |
|---|---|---|
| Frequency | high / medium / low | How often the check is relevant in real or representative runs. |
| Stakes | high / medium / low | Impact if the failure slips through. |
| Auto-convertibility | yes / partial / no | Whether a deterministic check can verify the signal. |
| Evidence quality | strong / mixed / weak | Whether logs, artifacts, or examples prove the check catches real issues. |

## Deterministic Alternatives

Prefer deterministic checks over LLM judges when the signal can be verified mechanically. Common alternatives:

| Alternative | Examples |
|---|---|
| File or section existence | Required artifact exists; required heading appears once. |
| Regex or structured parse | Required marker, ID, citation shape, or frontmatter field. |
| JSON or schema validation | Valid output shape; required keys; enum values. |
| Count or threshold | Minimum examples; maximum length; minimum cited sources. |
| Local command or test result | Unit test, lint, validator, smoke command, render check. |
| Retrieval or metadata query | Approved tool confirms link target, document metadata, or source status. |

## Report Template

```markdown
# Quality Check Eval: <scope>

## Scope
- Repo:
- Check source:
- Eval/log source:
- Artifact sample:

## Eval Check Catalog
| Check | Parent | Type | Rubric | Current status |
|---|---|---|---|---|

## Execution Signal
| Check | Observed skips/reviews/failures | Artifact evidence | Notes |
|---|---:|---|---|

## Recommendations
| Check | Frequency | Stakes | Auto-convertibility | Evidence | Recommendation |
|---|---|---|---|---|---|

## V2 Judge Scope
List the 3 to 5 best LLM-judge candidates. For each, include:
- why deterministic checks are insufficient
- judgment prompt sketch
- required evidence/context
- expected output shape

## Auto-Conversion Candidates
List eval checks that should become deterministic checks instead of LLM judges.

## Drop / Keep Manual
Explain briefly.
```
