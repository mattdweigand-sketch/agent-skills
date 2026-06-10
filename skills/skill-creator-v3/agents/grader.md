# Skill Eval Grader

Grade one eval output against the assertions in `evals/evals.json`.

## Input

- Eval prompt and expected output
- Actual output
- Assertion list, if available

## Process

1. Check each assertion independently.
2. Record `pass`, `fail`, or `not_applicable` with one concise reason.
3. Do not invent hidden criteria. If the assertion is ambiguous, mark it as a concern.
4. Separate deterministic failures from subjective quality notes.

## Output

Return a compact grading record:

```json
{
  "eval_id": "id",
  "assertions": [
    {
      "id": "assertion-id",
      "result": "pass",
      "reason": "Short evidence-based reason."
    }
  ],
  "concerns": []
}
```
