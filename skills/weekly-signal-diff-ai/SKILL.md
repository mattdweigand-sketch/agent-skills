---
name: weekly-signal-diff-ai
description: |
  Use when the user wants a weekly structural diff on the AI ecosystem:
  frontier labs, open models, dev tooling and agents, cloud AI platforms,
  data and model infrastructure, enterprise AI buyers, creative media,
  robotics and embodied AI, and AI regulation. Starts from 10 suggested
  categories and 30 suggested entities. Best for prompts like "run my
  weekly AI signal diff", "what changed in AI this week", "what moved in
  frontier labs", "track the AI market", or "turn this week's AI news into
  structural shifts". Optional live search upgrade: if OpenRouter access is
  available, prefer the Perplexity Sonar family for fresh web-grounded
  retrieval with citations.
author: Nate B. Jones (adapted for Matt Weigand, AI scope)
version: 1.1.0-ai
---

# Weekly Signal Diff — AI

## Problem

A wall of AI news does not tell the user what structurally changed in the AI
ecosystem. Most weekly roundups over-index on model launches and benchmark
screenshots, underweight economics, dependency shifts, and regulation, and
ignore what the user actually cares about. This skill turns a noisy week in AI
into a small set of structural changes.

Scope: frontier labs, open models, dev tooling and agents, cloud AI platforms,
data and model infrastructure, enterprise AI buyers, creative media, robotics
and embodied AI, and AI regulation.

## When to Use

- Weekly AI market review or Sunday/Friday ritual
- "Run my weekly AI signal diff"
- "Run my weekly signal diff for AI"
- "What changed in AI this week that matters to me?"
- "Track the AI market and tell me the structural shifts"
- "Turn this pile of AI news into a decision-grade diff"
- "What moved in frontier labs / open models / AI tooling this week"
- Ongoing automation for a weekly AI digest

## Required Context

Gather as much as the environment allows:

- the user's active projects, bets, and recurring interests
- prior weekly digests or summaries the user has shared
- the desired freshness window (default: last 7 days)
- any preferred outlets, banned sources, or explicit watchlist entities

If the user has not provided categories or companies, read
[references/starter-universe.md](references/starter-universe.md) and use it as
a bootstrap layer only.

If live web access is available and the user wants current coverage, read
[references/live-search-upgrade.md](references/live-search-upgrade.md) and use
the strongest search mode the environment supports.

## Process

1. Establish the frame.
   - Confirm the topic space, freshness window, and whether the goal is
     personal awareness, operator strategy, investor tracking, or content prep.
   - If the user says nothing, default to a 7-day operator-style review.

1. Build the watchlist.
   - Start from the suggested 10-category / 30-company starter universe if the
     user has not defined a watchlist.
   - Treat the starter list as a scaffold, not a contract.
   - Re-rank or replace items based on what the user has shared:
     - promote companies, categories, or themes the user mentions often
     - demote low-signal items
     - add personal-priority entities even if they are outside the starter set
   - Preserve some baseline discovery. Personalization should shape the scan,
     not collapse it into only known favorites.

1. Gather the week's evidence.
   - Prefer fresh, source-backed information with links or citations.
   - If live search is available, perform a broad sweep first, then targeted
     follow-ups on the top candidate shifts.
   - If live search is not available, work from the user's provided sources and
     say that the diff is source-bounded.
   - Ignore pure announcement theater unless it changes economics,
     distribution, regulation, dependency, geography, or buyer behavior.

1. Ask the structural questions on every candidate signal.
   - What constraint shifted?
   - Who gained or lost leverage?
   - What got cheaper, harder, faster, or more defensible?
   - What dependency got exposed?
   - What business model or pricing assumption weakened?
   - What changed in regulation, geography, or distribution?
   - Why does this matter for the user's actual projects, workflows, or market
     view?

1. Score before writing.
   - Keep only the few signals that represent real change.
   - A good weekly diff usually has 3-7 structural shifts.
   - Merge duplicates, drop weak stories, and explicitly label speculation as
     speculation.

1. Produce the weekly diff in chat.
   - Output the full diff directly in the conversation. Do NOT create a file
     or document. The diff is the deliverable.

   Use this default structure:

   - `Coverage note` — what was scanned, how it was personalized, and the date
     window
   - `Structural shifts` — 3-7 items, each with:
     - what changed
     - why it matters in general
     - why it matters to this user
     - supporting evidence or citations
   - `What changed from last week` — new, rising, fading, or resolved themes
   - `Watch next` — entities, constraints, or questions to monitor
   - `Actions` — optional follow-ups, only if the evidence supports them

## Output

When this skill works correctly, the user gets:

- a concise weekly structural diff delivered directly in chat (no file created)
- a clear explanation of why the shifts matter to them specifically
- citations or source links when live search is available

## Guardrails

- The goal is `diff, not digest`.
- Do not force all 30 suggested companies into the final output. They are there
  to prevent blank-page syndrome, not to create fake coverage.
- Do not mistake product launches, benchmark screenshots, or funding headlines
  for structural change unless they move a real constraint.
- Keep general market analysis separate from personalized implications.
- If evidence is thin, say the week was thin.
- If the environment lacks live search, be explicit about the freshness
  limitation.
- If the user's interests are unclear, use the starter universe and explain
  that it is a bootstrap pass.
- Never create a file or document as the output. Chat only.

## Notes for Other Clients

- This skill is portable across Codex, Codex, Cursor, and similar clients
  because the core behavior is procedural.
- For scheduled runs, pair the skill with the user's automation system and keep
  the same structure every week so diffs stay comparable.
- If OpenRouter is available, prefer a Perplexity Sonar web-search model for
  the retrieval pass, then use the local AI client or model to do the actual
  synthesis if that split is more ergonomic.
