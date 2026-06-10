# Skill Creator — JSON Schemas

Data structures used across the eval and benchmark pipeline.

---

## evals.json

Stores test prompts for a skill. Lives at `evals/evals.json` in the skill folder.

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": [],
      "assertions": [
        {
          "type": "contains",
          "value": "expected phrase or pattern"
        },
        {
          "type": "not_contains",
          "value": "phrase that should not appear"
        },
        {
          "type": "format",
          "value": "markdown | json | plain"
        }
      ]
    }
  ]
}
```

**Assertion types:**
- `contains` — output must include this string
- `not_contains` — output must not include this string
- `format` — output must match this format (markdown, json, plain)
- `length_max` — output must be under N characters
- `length_min` — output must be at least N characters

---

## grading.json

Stores per-run grading results. Lives at `evals/grading.json`.

```json
{
  "skill_name": "example-skill",
  "run_id": "uuid",
  "timestamp": "2026-04-28T12:00:00Z",
  "results": [
    {
      "eval_id": 1,
      "prompt": "User's task prompt",
      "output": "Agent response",
      "assertions_passed": 2,
      "assertions_total": 3,
      "assertion_details": [
        { "type": "contains", "value": "expected phrase", "passed": true },
        { "type": "not_contains", "value": "bad phrase", "passed": true },
        { "type": "format", "value": "markdown", "passed": false }
      ],
      "human_score": null,
      "human_notes": null
    }
  ],
  "summary": {
    "total_evals": 1,
    "assertions_passed": 2,
    "assertions_total": 3,
    "pass_rate": 0.67
  }
}
```

---

## benchmark.json

Aggregates multiple grading runs for variance analysis. Lives at `evals/benchmark.json`.

```json
{
  "skill_name": "example-skill",
  "runs": [
    {
      "run_id": "uuid-1",
      "timestamp": "2026-04-20T12:00:00Z",
      "pass_rate": 0.75,
      "human_scores": [4, 3, 5]
    },
    {
      "run_id": "uuid-2",
      "timestamp": "2026-04-27T12:00:00Z",
      "pass_rate": 0.83,
      "human_scores": [4, 4, 5]
    }
  ],
  "aggregate": {
    "mean_pass_rate": 0.79,
    "pass_rate_variance": 0.02,
    "mean_human_score": 4.2,
    "trend": "improving"
  }
}
```
