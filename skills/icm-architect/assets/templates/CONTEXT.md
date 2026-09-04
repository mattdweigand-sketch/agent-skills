# {Workspace name} — the pipeline

The flow in one line: {plan it, make it, check it, ship it — in your workspace's words}.

| Stage | Job | Input | Output | Human check |
|---|---|---|---|---|
| `01_{name}` | {five words} | {what it reads} | `output/{run-id}/{file}` | {what a person verifies} |
| `02_{name}` | {five words} | 01's output | `output/{run-id}/{file}` | {what a person verifies} |
| `03_{name}` | {five words} | 02's output | `output/{run-id}/{file}` | {what a person verifies} |

Factory (stable, every run): `_shared/{voice.md, rules.md, …}`
Product (new each run): each stage's `output/{run-id}/`. The task supplies the run ID; never reuse a previous run's ID for new work.

A stage is output-ready only when all declared artifacts for the active run exist and pass its contract checks. Placeholders and prior-run artifacts do not count. Report human approval separately from output readiness using the review record declared by the stage contract.
