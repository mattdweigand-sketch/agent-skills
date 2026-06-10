---
name: parallel-refactor
description: >
  Orchestrate multi-agent parallel code refactoring using isolated git worktrees.
  Trigger on /parallel-refactor [goal], "parallel refactor", "multi-agent refactor",
  "refactor using agents", or when the user wants to split a refactor across multiple
  agents or worktrees. Works on any codebase — no harness-specific knowledge required.
metadata:
  version: "2.0"
  category: agentic-systems
  tags: [refactor, multi-agent, worktrees, parallel, harness]
---

# /parallel-refactor [goal]

Thin coordinator pattern: specialist agents work on isolated worktrees simultaneously.
The main coordinator routes — it does not implement. A reviewer checks cross-partition consistency
before any merge guidance is given.

The [karpathy-guidelines](../karpathy-guidelines/SKILL.md) (simplicity-first, surgical changes,
goal-driven verification) are baked directly into the builder, plan, and reviewer prompts —
subagents do not inherit the parent's skills, so the principles must travel in the prompt text.
The plan assigns each partition a `Verify:` criterion; builders satisfy it; the reviewer checks it.

## Phases

| Phase | Agent | Gate |
|-------|-------|------|
| 0: Intake | — | Collect goal + root |
| 1: Scout | Explore | Maps codebase, identifies partitions |
| 2: Plan | Plan | Assigns files to waves and partitions |
| 3: Confirm | — | **Human gate** — Proceed / Edit / Abort |
| 4: Build | N builders in worktrees | Parallel per wave |
| 5: Review | 1 reviewer | Checks cross-partition consistency |
| 6: Merge | — | Git commands only — never auto-merge |

## Phase 0 — Intake

Collect:
- `goal` — from trigger args. If omitted, run Phase 1 in **suggest mode**.
- `root` — current working directory (cwd).
- `scope` — optional. Ask if codebase looks large (> ~30 files at root level).

**Clean-tree pre-flight (mandatory).** Worktrees branch from the committed HEAD — they do NOT
see uncommitted changes in the main working tree. If the user has in-progress edits to files a
builder will also touch, a later merge can clobber that work. Run `git status --short` in `root`.
If it shows modified/staged files:

```
⚠ Working tree has uncommitted changes. Worktrees branch from HEAD, so these edits
  won't be in any builder's copy — and merging a builder branch could overwrite them.

  [list the modified files]

  Recommend: commit or stash before launching. (commit / stash / proceed anyway / abort)
```

- `commit`/`stash` → tell the user to do it (or do it on request), then re-check.
- `proceed anyway` → continue, but in Phase 6 you MUST reconcile by hand any file that appears
  in both the working tree and a builder's CHANGED list (apply the builder's change on top of the
  user's work — never blind-merge over it).
- `abort` → stop.

Optional deterministic support: if this repo includes `scripts/parallel_refactor_preflight.py`,
run it from the skill repo against the target root as a read-only helper:

```bash
python3 scripts/parallel_refactor_preflight.py <root>
```

After Phase 2, pass planned builder files to check for dirty-tree collisions:

```bash
python3 scripts/parallel_refactor_preflight.py <root> --planned-files-from <newline-file-list>
```

If the helper is unavailable, use the prose checks above. Do not make the target repo depend on
this script.

## Phase 1 — Scout

Spawn one **Explore** agent. Full prompt: `references/scout-prompt.md`.
Substitute `{{goal}}`, `{{root}}`, `{{scope}}`, `{{suggest_mode}}` before sending.

On return:
- **Suggest mode**: present the 3 SUGGEST options to the user. Wait for selection.
  Set `goal` to chosen option. Proceed to Phase 2 (reuse scout's matching partition candidates).
- **1 viable partition only**: note to user, set `single_builder_mode = true`.
  Skip wave logic in Phase 4 — spawn one builder in a worktree.
- **No viable partitions**: surface RISKS section. Ask user to narrow scope or refine goal.

## Phase 2 — Plan

Spawn one **Plan** agent with the full scout output + `goal`.
Full prompt: `references/plan-prompt.md`. Substitute `{{scout_output}}` and `{{goal}}`.

Extract from output: partition specs (name, files, new files, goal, owns, must-not-touch,
contracts, wave), MERGE ORDER, RISKS.

## Phase 3 — Confirm (mandatory — never skip)

Print this panel verbatim and wait for `yes / edit / abort`:

```
Parallel Refactor Plan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Goal:   [goal]
Root:   [root]

Wave A  (parallel — N agents):
  [partition]: N files — [one-line goal]
  [partition]: N files — [one-line goal]

Wave B  (after Wave A — M agents):    [omit section if empty]
  [partition]: N files — [one-line goal]

Interface contracts at risk:
  [list from plan, or "none"]

Risks:
  [list from plan, or "none"]

Worktrees: N  |  Reviewer: 1

Proceed? (yes / edit / abort)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

- `yes`   → Phase 4
- `edit`  → ask which partition or goal to adjust → re-run Phase 2 → re-print panel
- `abort` → stop cleanly

## Phase 4 — Build

Builder prompt template: `references/builder-prompt.md`.
Fill in per-partition values before sending each agent.

**Wave A** — spawn all Wave A agents together when the runtime supports parallel worker calls:
- worker type: use the local coding agent or repo-capable worker
- isolation: use a separate git worktree per worker
- background execution: enabled when available

Wait for all Wave A notifications. Collect each agent's summary block
(`CHANGED / CREATED / CONCERNS / COMMIT / BRANCH / STATUS`). Record each branch + commit SHA.

Each builder commits its own work to its branch (staging only its files). If any builder reports
`COMMIT: NOT COMMITTED`, its changes are uncommitted in the worktree — Phase 6's `git merge` will
not pick them up. Either re-dispatch the builder to commit, or in Phase 6 apply that worktree's
diff by hand.

If any builder returns `STATUS: NEEDS REVIEW`:
→ Surface the concern. Ask: *"[Partition] flagged: [concern]. Proceed to Wave B? (yes / inspect first)"*

**Wave B** (if any) — same spawn pattern. Inject Wave A summaries as context for dependent
partitions (see `{{wave_b_context}}` in builder-prompt.md). Repeat for Wave C if present.

## Phase 5 — Review

Spawn one reviewer agent (no worktree isolation, no background).
Full prompt: `references/reviewer-prompt.md`.
Pass all builder summaries + worktree branch names.

Present reviewer output to the user verbatim. Do not filter or summarize it.

## Phase 6 — Merge guidance

Print exact git commands derived from reviewer's MERGE ORDER and CLEAN/FLAG results:

```bash
# Clean partitions — merge in dependency order:
git merge [branch]   # Partition 1: [name]
git merge [branch]   # Partition 2: [name]

# Flagged partitions — inspect before merging:
git diff main..[branch]   # Partition N: [concern]
```

Do not auto-merge. For flagged partitions: describe the conflict and suggest resolution.

**If Phase 0 was "proceed anyway" on a dirty tree:** for any file in both the user's working tree
and a builder's CHANGED list, do NOT `git merge` that branch blindly — it would overwrite the user's
work. Instead apply the builder's change on top of the user's version by hand (the builder's branch
was cut from HEAD and is missing the user's uncommitted edits). Flag each such file explicitly.

**Worktree cleanup:** after the user merges, offer to remove the worktrees:
`git worktree remove [path]` per branch. Agent-managed worktrees may be locked by the harness;
if `remove` reports a lock, leave them — the harness cleans them up. Do not force-unlock.

## Graceful degradation

| Situation | Behavior |
|---|---|
| No goal given | Suggest mode — user picks from 3 scout-surfaced options |
| 1 viable partition | Single worktree builder, still runs reviewer |
| No viable partitions | Surface RISKS, ask user to narrow scope |
| Builder NEEDS REVIEW | Pause before next wave, user decides |
| Reviewer flags conflict | No merge command for flagged partition; describe resolution |
| No test suite found | Reviewer notes it; user assumes merge risk |

## Reference files

- `references/scout-prompt.md` — Explore agent prompt
- `references/plan-prompt.md` — Plan agent prompt
- `references/builder-prompt.md` — Builder agent prompt template
- `references/reviewer-prompt.md` — Reviewer agent prompt
