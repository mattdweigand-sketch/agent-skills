# autoresearch — target playbooks

The loop in `SKILL.md` is identical for every target. Only the **edit surface**, **test set**, and
**scorer** change. Pick the closest playbook; for anything not listed, follow the same three-part shape.

## Open Brain retrieval

- **Edit surface:** `search_thoughts` params (`min_similarity`, `limit`, `type`/`subtype`/`account`
  filters, `min_confidence`) and query phrasing.
- **Test set:** `{query, expected_id(s) | expected_substring, should_be_empty?}`. Server-side
  embeddings are fixed, so results are reproducible.
- **Metric:** top-k hit rate on positives + clean-refusal rate on negatives (a no-answer query that
  returns junk above threshold is a miss). Report both — raising `min_similarity` trades one for the other.
- **Watch for:** `min_confidence` / `subtype` filters silently empty a slot when the corpus lacks
  those tags. Ablate one filter at a time to prove which one is fatal.

## Skill routing

- **Edit surface:** the `description:` block of one or more `SKILL.md` files.
- **Test set:** `{prompt, expected_skill}`. Route using ONLY the descriptions, mirroring the live harness.
- **Metric:** routing accuracy = correct / total.
- **Orchestrate, don't reinvent:** `skill-eval` runs the measurement, `skill-creator` makes the edit.
  This skill owns only the keep/discard loop around them.

## A prompt / talk-track / email template

- **Edit surface:** the wording.
- **Test set:** a set of inputs + a rubric. Freeze the rubric before looping.
- **Metric:** rubric score. Define each criterion and its weight up front so scoring is repeatable.

## A config / threshold / ranking weight

- **Edit surface:** the value(s).
- **Test set:** labeled cases the config is meant to get right.
- **Metric:** whatever the config optimizes (precision/recall, latency, cost, accuracy).

---

## results.tsv format

Tab-separated (commas break descriptions). Header + one row per experiment. Columns flex to the
target; always keep a primary score, a secondary trade-off axis, status, and a one-line note.

```
exp	score	secondary	status	change
b0	8/14	neg_clean:1/4	keep	baseline — default params
e1	11/14	neg_clean:3/4	keep	raise threshold to 0.55 — cuts false matches, holds hits
e2	10/14	neg_clean:4/4	discard	threshold 0.6 — over-tight, drops a real hit
```

- `exp` — short id (`b0`, `e1`, …)
- `score` — primary metric
- `secondary` — the trade-off axis you're watching (false positives, recall, cost)
- `status` — `keep` / `discard`
- `change` — hypothesis + outcome, one line

---

## Worked example (Open Brain retrieval, May 2026)

Baseline **9/14** (8/10 positives, 1/4 negatives clean) at `min_similarity 0.3`.

1. Swept `min_similarity` → best **11/14** at 0.55. Hit a ceiling: a false match (sim 0.585) sat
   *above* a real hit (sim 0.582) — interleaved, so no threshold could separate them.
2. Added uniform domain-vocab query expansion → lifted every true hit's similarity, opening a clean
   gap, and re-tuned the threshold up to 0.6 → **14/14**.
3. Honesty check caught a leak: one expanded query echoed the target's own wording. Re-ran it
   neutrally → that case reverted to a real miss. **Honest floor: 13/14.**

Lessons baked back into `SKILL.md`: freeze the test, no answer leaks, and confirm the surface is on
the live path (here it wasn't — the production retrieval used canned queries, so the win wasn't directly
shippable).
