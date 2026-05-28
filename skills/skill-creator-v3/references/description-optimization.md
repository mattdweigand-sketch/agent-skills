---
# Skill Creator — Description Optimization

Complete process for improving skill triggering accuracy via eval queries.

---

## Overview

A skill description does two things: tells Claude what the skill is for, and determines when it fires. Optimization focuses on the second: ensuring the description triggers on the right prompts and stays silent on the wrong ones.

The process: generate test queries → user reviews and edits → run trigger simulation → score → rewrite description → rerun.

---

## Step 1: Generate Trigger Eval Queries

Produce 10–15 test queries across three categories:

**Should trigger (5–7 queries):**
- The clearest, most direct invocations of the skill's purpose
- Rephrased or indirect formulations ("turn this into a skill" vs. "create a SKILL.md for this")
- Edge cases that are still within scope

**Should not trigger (3–5 queries):**
- Related but out-of-scope requests (e.g., "help me organize my notes" for a skill-creation skill)
- Overlapping skills — queries where another skill should fire instead
- Requests that sound similar but have different intent

**Ambiguous (2–3 queries):**
- Prompts where triggering would be reasonable but not guaranteed
- Use these to explore where the threshold should sit

Present these as a numbered list. Ask the user to mark each: `Y` (should trigger), `N` (should not), `M` (marginal — ok either way).

---

## Step 2: Simulate Triggering

For each query, simulate how Claude's skill selection behaves:

1. Show the current description.
2. For each query, reason aloud: "Based on this description, would I activate this skill?"
3. Record: `fired` or `did not fire`.
4. Compare against the user's expected labels.

Compute:
- **True positive rate** — correct fires / expected fires
- **False positive rate** — incorrect fires / expected non-fires
- **Miss rate** — expected fires that didn't fire

---

## Step 3: Identify Failure Patterns

Cluster mismatches:

| Pattern | Fix |
|---|---|
| Skill fires on too many things | Description too broad. Narrow the trigger context. Add specificity. |
| Skill doesn't fire on key phrases | Description missing those phrases. Add trigger vocabulary. |
| Skill fires instead of another skill | Add explicit "use [other-skill] instead" redirect in the description. |
| Skill misses indirect phrasings | Add paraphrased trigger examples to the description. |

---

## Step 4: Rewrite the Description

Apply targeted fixes based on the failure pattern:

**Too broad:** Add exclusions. "Use when X. Does not apply to Y or Z — use [other-skill] for those."

**Undertriggering:** Expand the trigger vocabulary. List additional user phrases and contexts explicitly.

**Competing with another skill:** Add a mutual exclusion clause. Both skills should name the split.

**Description format principles:**
- Lead with what the skill *does*, not what it's called
- Enumerate trigger phrases explicitly, especially non-obvious ones
- Make it "pushy" — Claude tends to undertrigger by default
- Keep it under ~80 words; longer descriptions degrade scannability
- Do not bury the trigger — put the clearest phrase in the first sentence

---

## Step 5: Rerun and Confirm

Repeat Steps 2–3 with the new description. Confirm:
- True positive rate ≥ 90%
- False positive rate ≤ 10%
- Zero misses on the user-labeled `Y` queries

If the rates don't meet bar: iterate once more before finalizing. If after 2 rewrites the description still misses — the skill may need restructuring (scope too broad, overlaps with another skill not yet guarded against).

---

## Step 6: Apply to SKILL.md

Update the `description` field in the frontmatter. Do not change any other frontmatter field. Present the diff.

Offer to run the same optimization on any competing skills identified during Step 3.
