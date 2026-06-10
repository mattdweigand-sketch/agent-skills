# Context Surface Taxonomy

Use this reference with `context-window-audit` when classifying context bloat or formatting an audit report.

## Actions

| Action | Meaning |
|---|---|
| `delete` | No longer useful or duplicated by a canonical owner. |
| `shorten` | Useful at startup, but too verbose for always-loaded context. |
| `route` | Move behind a task router, command wrapper, or skill trigger. |
| `reference` | Keep as an on-demand reference file, not startup context. |
| `code` | Replace prompt instructions with scripts, tests, schemas, or hooks. |
| `keep` | Justified startup context. |

## Output Template

Return:

- `Startup map`: what appears to load by default
- `Findings`: prioritized issues with file paths and concrete actions
- `Suggested removals`: prompt surface that can be deleted or parked
- `Suggested routing`: context that should become on-demand
- `Validation`: checks run and anything not verified

If no meaningful bloat is found, say that directly and list the remaining context surfaces that still deserve periodic review.
