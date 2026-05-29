---
name: linkedin-post
description: "Write LinkedIn posts for Matt Weigand's personal feed. Produces a 150 to 300 word post formatted for LinkedIn with a hook opening, one idea per paragraph, no bullet points, and a concrete closing. Content types: thought leadership on fund admin and alternative investments, JSQ product news, industry trend commentary, personal takes on AI and PE. Trigger on '/linkedin-post [topic]', 'write a LinkedIn post about', 'LinkedIn post on', 'post about [topic]', 'draft a post on', 'create a LinkedIn post'. Do NOT trigger for LinkedIn DMs or connection request messages, email outreach, or multi-post campaigns."
allowed-tools: Read Write Edit Glob Grep mcp__open-brain__search_thoughts
---

# LinkedIn Post

Generate LinkedIn posts for Matt's personal feed. Voice and structure rules layer on top of writing-style.

## Contract

**Produces:** A single LinkedIn post (150-300 words) formatted for copy-paste into LinkedIn. Presented in chat with an iteration offer.

**Does NOT produce:** LinkedIn DMs, connection request messages, email outreach, multi-post campaigns, or files written to disk.

## Context Needs

| Source | Load level | Purpose |
|---|---|---|
| [_references/writing-style.md](../_references/writing-style.md) | full | Voice, tone, formatting (Tier 2: 20-word sentence limit) |
| Open Brain `search_thoughts` | targeted | `REJECTION linkedin`, `[topic] ICP`, `[topic] competitive intel` when topic is fund-admin or JSQ-related |
| `~/Code/jsq-wiki/wiki/<entity>` | targeted | Load only when the post needs a specific JSQ product/customer/competitor reference |

## Step 0: Open Brain Pre-Flight

1. **Rejection enforcement.** `search_thoughts` for `REJECTION linkedin`, `REJECTION post`, `REJECTION social`. Silently apply.
2. **Topic context.** If topic is fund-admin / alternatives / JSQ, search Open Brain for relevant ICP and competitive intel.

If Open Brain is unreachable: flag `[rejection enforcement skipped]` as the first line of chat output and proceed.

## Process

1. **Clarify if needed.** If topic or angle is unclear, ask once: what topic, what angle, what type (thought leadership / product news / industry commentary / AI-PE take).
2. **Research.** Open Brain search per Step 0 plus targeted wiki reads.
3. **Draft.** Write per Structure Rules below. Aim for 150-300 words.
4. **Present.** Output formatted exactly as it would appear on LinkedIn. Ask: "Any changes, or is this ready to post?"

## Structure Rules

These layer on writing-style. Writing-style owns voice, tone, hard rules. This section owns LinkedIn-specific structure.

- **Hook first.** Opening 1-2 lines must hook the reader. This is what shows before "see more."
- **One idea per paragraph.** If two points feel similar, consolidate.
- **No bullet points.** Use line breaks and short standalone paragraphs.
- **No motivational closing.** End on something concrete.
- **Whitespace.** Use line breaks strategically so ideas breathe and scan easily.

## Content Guidance

- **Thought leadership (fund admin / alternatives):** Practical insights, not generic advice. Authenticate with specific examples when possible.
- **JSQ product news:** Lead with customer impact, not the feature. Accessible to non-technical readers.
- **Industry trend commentary:** React to market moves, regulation, or shifts. Offer a perspective, not just observation.
- **AI / PE takes:** Reflective, can take a stance. Ground in concrete examples. Avoid hype.

## Edge Cases

- **Off-domain topic.** Anchor to Matt's professional perspective (enterprise sales, building teams). If no natural anchor exists, flag it: "This is outside your usual lane. Want to angle it toward [suggested connection]?"
- **JSQ feature without inside knowledge.** Ask for specifics. Do not invent capabilities.
- **No relevant Open Brain context.** Proceed with web research and Matt's general domain expertise. Do not pad with generic industry observations.

## Boundaries

I write to:
- Chat only — post formatted for copy-paste.

I do not write to:
- Any `deal-management/` file.
- Open Brain (search-only; no `capture_thought` or other writes).

## Examples of Style in Action

**Good (hooks immediately):** "Fund managers are drowning in paperwork that could be automated. Here's why most still handle cap tables manually."

**Avoid (filler):** "I've been thinking a lot about automation lately, and there's something interesting I want to share."

**Good (concrete ending):** "The fund managers winning today aren't the ones with the smartest investment thesis. They're the ones who've automated everything that isn't strategic."

**Avoid (motivational platitude):** "So remember: always embrace change and stay ahead of the curve."

## Fallback

If Open Brain is unreachable, flag `[rejection enforcement skipped]` as the first line of chat output and proceed. Rejection enforcement is the only OB dependency.
