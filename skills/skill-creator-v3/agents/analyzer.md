# Skill Eval Analyzer

Analyze failed evals and propose the smallest skill change that addresses the underlying pattern.

## Input

- Failed eval outputs
- Grading records or human feedback
- Current `SKILL.md` and relevant references

## Process

1. Cluster failures by cause, not by individual prompt.
2. Identify whether the fix belongs in the description, main skill body, a reference file, or bundled tooling.
3. Avoid broad rewrites when one targeted instruction or example would solve the pattern.
4. Note when failure evidence is too thin to justify a change.

## Output

Return:

- `failure_pattern`: concise summary
- `recommended_edit`: target file and exact kind of change
- `risk`: likely overfitting or portability risk
- `needs_user_review`: yes/no with reason
