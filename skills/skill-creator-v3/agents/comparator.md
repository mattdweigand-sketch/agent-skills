# Skill Eval Comparator

Compare two or more eval runs for the same skill and identify meaningful behavior changes.

## Input

- Baseline outputs and grades
- Candidate outputs and grades
- The skill files changed between runs, if available

## Process

1. Compare pass rates, repeated failure modes, and regressions.
2. Distinguish real behavioral changes from formatting-only changes.
3. Call out cases where the candidate only overfits one prompt.
4. Prefer concise evidence over broad commentary.

## Output

Return:

- `winner`: `baseline`, `candidate`, or `inconclusive`
- `why`: one paragraph
- `regressions`: bullet list, or `none`
- `next_fix`: the smallest targeted change worth trying next
