# Autoresearch Experiment Schema

Use this structure for each run. A TSV is still the default artifact, but these
fields keep the experiment log machine-checkable and comparable.

## Run Header

| Field | Meaning |
|---|---|
| `run_tag` | Stable identifier, such as `routing-june10` |
| `target` | The exact editable surface |
| `live_path_check` | Evidence that production uses the edited surface |
| `test_set` | Path or description of the frozen cases |
| `scorer` | Exact metric and scoring command or rubric |
| `primary_metric` | Main score to optimize |
| `secondary_metric` | Trade-off to watch, such as false positives, recall, cost, or latency |

## Experiment Row

| Field | Meaning |
|---|---|
| `exp` | `b0`, `e1`, `e2`, etc. |
| `hypothesis` | One-line reason the change should improve the metric |
| `change` | The single edited parameter, prompt, config, or file |
| `primary_score` | Primary metric result |
| `secondary_score` | Trade-off metric result |
| `status` | `keep`, `discard`, `stop-label-bug`, or `stop-structural` |
| `note` | One-line residual miss or reason |

## Stop Record

| Field | Meaning |
|---|---|
| `baseline` | Starting score |
| `best` | Best kept score |
| `delta` | Baseline to best change |
| `kept_change` | Winning config or patch |
| `residual_misses` | Remaining failures grouped by cause |
| `next_action` | Stop, fix labels, add data, or structural redesign |
