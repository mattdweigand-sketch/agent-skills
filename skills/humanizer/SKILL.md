---
name: humanizer
description: |
  Remove signs of AI-generated writing and fix clarity failures in text. Use when
  editing or reviewing any prose to make it sound natural and human-written: emails,
  posts, docs, READMEs, specs, reports. Detects AI tells (inflated significance,
  promotional language, -ing analyses, vague attributions, em dash overuse, rule of
  three, AI vocabulary, copula avoidance, negative parallelism, filler, hedging) and
  runs a clarity pass for problems that survive a clean scan: redundant structure,
  abstract claims with no example, wrong framing, backwards information order.
license: MIT
metadata:
  version: 3.0.0
  category: writing
  tags: ["writing", "editing", "voice", "ai-detection", "clarity"]
  compatibility: Codex opencode
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---

# Humanizer: Remove AI Writing Patterns

Identify and remove signs of AI-generated text so writing sounds natural and human, in Matt Weigand's voice. Two passes: an AI-pattern pass (the 25 tells below) and a clarity pass (problems that survive a clean scan).

## Principles

1. **Be surgical.** Only fix sections with actual problems. Leave clean, in-voice sentences alone. Do not rewrite for its own sake.
2. **Never add content.** No new ideas, sections, or claims. Do not change factual counts ("three moving parts" stays three).
3. **Preserve structure.** Keep the original's formatting and organization unless it is itself an AI pattern (emoji headers, excessive boldface).
4. **Preserve meaning.** Keep the core message intact.
5. **Match the register.** Technical docs stay technical, formal emails stay formal. Do not let casual voice bleed into professional writing.
6. **Add soul only where flat.** Inject personality where writing is genuinely lifeless, but stay inside the register (see voice profile).

## Voice

Always write in Matt's voice, not a generic "natural human" default. **Default to the professional-analytical register** for anything someone else will read (docs, READMEs, specs, professional email). Hard rules:

- **No em dashes.** Use a hyphen, comma, or period instead, even when the original uses them.
- **Preserve real technical vocabulary** (GPs, LPs, fund admin, infrastructure, control layer, pipeline, corpus, agent surface). These are not AI filler.
- **State opinions plainly, don't hedge.** Vary rhythm: short declaratives mixed with longer analytical sentences.

Full profile, writing samples, and "adding voice to flat text" guidance: `references/voice-profile.md`. If the user provides their own writing sample, that overrides the profile.

## Pass 1: AI pattern checklist

This checklist is the detection layer: the cues below are enough to *catch* every tell, so scan against all 25 on every run. It is always in context, so detection never depends on loading anything else.

When you have caught a tell but the *rewrite* is non-obvious, open `references/patterns.md` and read that pattern's entry for its full words-to-watch list and a before/after example. Loading it per-tell (not the whole file) is the norm for anything you are not confident you can fix cleanly from memory.

**Content and tone**
1. Significance inflation ("testament to," "pivotal moment," "evolving landscape")
2. Superficial -ing endings ("highlighting," "underscoring," "reflecting" tacked on)
3. Promotional language ("vibrant," "nestled," "breathtaking," "stands as")
4. Vague attributions ("experts argue," "industry reports," "observers note")

**Language and grammar**
5. AI vocabulary words ("delve," "crucial," "enhance," "interplay") — but keep real technical terms
6. Copula avoidance ("serves as," "boasts" instead of "is," "has")
7. Negative parallelism and tailing negation ("not just X but Y," "no guessing")
8. Rule of three (forced triplets)
9. False ranges ("from X to Y" where X and Y aren't on a scale)
10. Passive voice and subjectless fragments ("No config needed")

**Style and formatting**
11. Em dash overuse (in Matt's voice: remove entirely)
12. Boldface overuse
13. Inline-header vertical lists ("- **Thing:** ...")
14. Title case in headings
15. Emojis
16. Curly quotes

**Communication artifacts**
17. Collaborative chatbot artifacts ("I hope this helps," "let me know")
18. Sycophantic tone ("Great question!")

**Filler and hedging**
19. Filler phrases ("in order to," "at this point in time")
20. Excessive hedging ("could potentially possibly")
21. Generic positive conclusions ("the future looks bright")
22. Hyphenated word-pair overuse ("cross-functional, data-driven, client-facing")
23. Persuasive authority tropes ("the real question is," "at its core")
24. Signposting ("let's dive in," "here's what you need to know")
25. Fragmented headers (a heading then a one-line restatement of it)

## Pass 2: Clarity pass

Run after the pattern pass. These survive a clean scan: the text reads human but still fails the reader. A draft can pass all 25 patterns and still be nebulous, mis-framed, redundant, or badly ordered.

- **A. Redundant structure.** The same instruction or claim repeated in different words. Reads as padding. Fix: say it once, where it belongs.
- **B. Abstract with no anchor.** A claim describes the *shape* of a thing ("a set of tools organized around problems") without a concrete instance. Fix: lead with or insert a specific example, then generalize.
- **C. Wrong frame.** The text is clear but names the thing wrong (calling a setup guide a "set of fixes"). Clarity cannot rescue a wrong thesis. Fix: confirm what the thing *is* before polishing how it reads.
- **D. Backwards information order.** Detail before the point: job titles before what they share, jargon before its plain meaning. Fix: lead with the plain idea, then let specifics follow as examples.

## Process

1. Read the input carefully.
2. Run pass 1: scan against all 25 cues to detect tells, then rewrite each. Open the relevant entry in `references/patterns.md` for any tell whose fix is non-obvious.
3. Run pass 2: the clarity pass (A-D), even when no AI patterns remain.
4. Check the draft reads aloud naturally, varies sentence structure, uses specific details over vague claims, holds the register, and uses simple constructions (is/are/has) where they fit.
5. Present a draft rewrite.
6. Self-audit: "What makes this so obviously AI generated?" Answer briefly with remaining tells.
7. Revise and present the final version.

## Output format

1. Draft rewrite
2. "What makes the below so obviously AI generated?" (brief bullets)
3. Final rewrite
4. Brief summary of changes (optional, if helpful)

See `references/full-example.md` for a complete worked run.

## Reference files

- `references/patterns.md` — the 25 patterns with words-to-watch and before/after examples
- `references/voice-profile.md` — full Matt voice profile, writing samples, adding-voice guidance
- `references/full-example.md` — a complete before/draft/audit/final run
