# RALF Loop Skill

Reusable Codex skill for running local smoke/eval improvement loops.

The loop is:

```text
Run -> Analyze -> Learn -> Fix -> Rerun
```

Use it when a repo has a local command or workflow that can be scored against frozen gates.

## Install

Copy the skill folder into your personal skills directory:

```bash
cp -R ralf-loop ~/.agents/skills/ralf-loop
```

## Trigger

Ask Codex:

```text
run a RALF loop on this repo
```

or:

```text
run the smoke test until it converges
```

## Safety Defaults

- Local-first. No cloud deploys unless explicitly authorized.
- Frozen gates before edits.
- Negative controls required for retrieval, AI, parser, and workflow tests.
- One bounded fix per iteration.
- Terminal state is `pass`, `needs-human`, or `blocked`.
