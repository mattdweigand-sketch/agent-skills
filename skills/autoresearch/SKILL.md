---
name: autoresearch
description: "Eval-driven keep/discard optimization loop for any laptop-runnable target — Open Brain retrieval, a skill's routing/description, a prompt or talk-track, an email template, a deck outline, a config, any editable surface you can score against a frozen labeled test set. Measure a baseline, make ONE change, re-measure, keep if the metric improved, revert if not, log every experiment, repeat until it converges. Use whenever the user says '/autoresearch', 'optimize my target', 'tune this against a test set', 'improve this accuracy/quality', 'find the best params/wording/config', or 'is this change actually better' — even when phrased loosely as wanting something to work better and there's a way to score it. Do NOT use to merely diagnose a skill (use skill-eval) or merely edit one (use skill-creator); this skill owns the measure→edit→re-measure loop that ties them together."
metadata:
  version: "2.0"
  category: "meta"
  tags: ["optimization", "eval", "autoresearch", "keep-discard", "retrieval"]
---

# autoresearch

An eval-driven optimization loop for any target you can run on a laptop and score. Karpathy's
`autoresearch` pattern pointed at your own tooling: you are the researcher, an "experiment" is ONE
change to an editable surface, and the "metric" is a score against a frozen labeled test set.

## The mapping

| autoresearch (GPU) | here (anything) |
|---|---|
| `val_bpb` — fixed metric | **your metric** — accuracy, top-k hit rate, MRR, rubric score |
| `train.py` — the file you edit | **the edit surface** — params, a description, a query, a prompt, a template, a config |
| `prepare.py` — frozen harness | **the test set + scorer** — labeled cases you do NOT touch mid-run |
| keep / discard / `git reset` | keep if the metric rose, else revert |

## Does this apply? (gate before starting)

Run the loop only if all three hold. If any fails, this is the wrong tool — say so and stop.

1. **Editable surface** — a specific thing you can change and re-run.
2. **Scorable** — you can write down a right answer and *count* (or rubric-score) hits. No countable
   metric → don't use this.
3. **On the live path** — confirm production actually uses the surface you're about to tune. We once
   tuned a search path the real system never called; the win was unshippable. Check first.

## Setup

Pin down before any experiment:

1. **Target** — name the edit surface and confirm gate #3 (it's live).
2. **Lock the test set** — existing or built. Include **negatives** (cases that should return
   nothing / a refusal); without them you optimize into noise. Split into an *easy* sanity set and a
   *hard* set — only the hard set has a gradient.
3. **Define the scorer** — exact metric and what counts as a hit. Write it down.
4. **Run tag** — e.g. `ob-retrieval-may24`. Results go to a fresh `results-<tag>.tsv`.
5. **Confirm and go.**

Use `references/experiment-schema.md` when the run needs a more explicit record
than the TSV row alone.

## Two rules that keep it honest

- **Freeze the test.** The test set and scorer do not change mid-run. Editing the test to make a
  change "win" deletes the gradient.
- **No answer leaks.** When the edit surface IS wording (a query, a prompt), don't slip the target's
  own answer-words into it — that inflates the score. Phrase it the way a real user would, then measure.

## Baseline

First experiment is always the unmodified surface. Measure, record, and state it to the user before
looping. Every later number is read relative to this.

## The loop

LOOP until it converges (this is NOT run-forever):

1. Note current state (what's live).
2. Make **one** change with a stated hypothesis.
3. Re-run the FROZEN test set through the scorer.
4. Read the metric.
5. **Keep** if it improved; **revert** if equal or worse. (A flat-metric change that simplifies is a keep.)
6. Log the row to `results-<tag>.tsv`.
7. If a change reveals a *label error* (system returned a better answer than your label), STOP and fix
   the label — that's a harness bug, not an experiment. Note it.

## Stop conditions

The edit surface is small and discrete, so the loop converges (unlike the GPU version). Stop when:
- you've swept the obvious changes and the metric plateaus for ~3–4 experiments, OR
- remaining misses are test-set/label problems, not tunable, OR
- the fix is structural (one-shot edit, not a loop).

On stop, hand the user: the winning config, the baseline→best delta, the `results-<tag>.tsv`, and the
residual misses *with why* (content gap, label issue, true ceiling).

## Reference

- `references/targets.md` — per-target playbooks (retrieval, skill-routing, prompt/template, config),
  the `results.tsv` format, and a worked example.
- `references/experiment-schema.md` — run header, experiment row, and stop-record fields for
  repeatable logs.
