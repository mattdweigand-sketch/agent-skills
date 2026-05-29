---
name: linkedin-post
description: "Write LinkedIn posts for your personal feed. Produces a 150 to 300 word post formatted for LinkedIn with a hook opening, one idea per paragraph, no bullet points, and a concrete closing. Content types: thought leadership, product or company news, industry trend commentary, and personal takes. Trigger on '/linkedin-post [topic]', 'write a LinkedIn post about', 'LinkedIn post on', 'post about [topic]', 'draft a post on', 'create a LinkedIn post'. Do NOT trigger for LinkedIn DMs or connection request messages, email outreach, or multi-post campaigns."
allowed-tools: Read Write Edit Glob Grep WebSearch
---

# LinkedIn Post

Generate LinkedIn posts for your personal feed. Voice and structure rules layer on top of your writing-style guide if you keep one.

## Contract

**Produces:** A single LinkedIn post (150-300 words) formatted for copy-paste into LinkedIn. Presented in chat with an iteration offer.

**Does NOT produce:** LinkedIn DMs, connection request messages, email outreach, multi-post campaigns, or files written to disk.

## Context Needs

| Source | Load level | Purpose |
|---|---|---|
| Your writing-style guide, if you have one | full | Voice, tone, formatting |
| A knowledge base or notes store, if connected | targeted | Past feedback on your posts, plus topic-specific context |
| Domain reference docs, if available | targeted | Load only when the post needs a specific product, customer, or competitor reference |

## Step 0: Pre-Flight

1. **Past feedback.** If you keep a feedback or rejection log, search it for prior notes on LinkedIn posts and apply them silently.
2. **Topic context.** Pull any available context on the topic before drafting.

This step is optional. If no knowledge base is connected, proceed straight to the process.

## Process

1. **Clarify if needed.** If topic or angle is unclear, ask once: what topic, what angle, what type (thought leadership / product news / industry commentary / personal take).
2. **Research.** Pull context per Step 0, plus targeted reads or web search as needed.
3. **Draft.** Write per Structure Rules below. Aim for 150-300 words.
4. **Present.** Output formatted exactly as it would appear on LinkedIn. Ask: "Any changes, or is this ready to post?"

## Structure Rules

These layer on your writing-style guide. The guide owns voice, tone, and hard rules. This section owns LinkedIn-specific structure.

- **Hook first.** Opening 1-2 lines must hook the reader. This is what shows before "see more."
- **One idea per paragraph.** If two points feel similar, consolidate.
- **No bullet points.** Use line breaks and short standalone paragraphs.
- **No motivational closing.** End on something concrete.
- **Whitespace.** Use line breaks strategically so ideas breathe and scan easily.

## Content Guidance

- **Thought leadership:** Practical insights, not generic advice. Authenticate with specific examples when possible.
- **Product or company news:** Lead with customer impact, not the feature. Accessible to non-technical readers.
- **Industry trend commentary:** React to market moves, regulation, or shifts. Offer a perspective, not just observation.
- **Personal takes:** Reflective, can take a stance. Ground in concrete examples. Avoid hype.

## Edge Cases

- **Off-domain topic.** Anchor to your professional perspective. If no natural anchor exists, flag it: "This is outside your usual lane. Want to angle it toward [suggested connection]?"
- **Product feature without inside knowledge.** Ask for specifics. Do not invent capabilities.
- **No relevant stored context.** Proceed with web research and your general domain expertise. Do not pad with generic industry observations.

## Boundaries

I write to:
- Chat only. The post is formatted for copy-paste.

I do not write files or external systems. This skill is read and draft only.

## Examples of Style in Action

**Good (hooks immediately):** "Fund managers are drowning in paperwork that could be automated. Here's why most still handle cap tables manually."

**Avoid (filler):** "I've been thinking a lot about automation lately, and there's something interesting I want to share."

**Good (concrete ending):** "The fund managers winning today aren't the ones with the smartest investment thesis. They're the ones who've automated everything that isn't strategic."

**Avoid (motivational platitude):** "So remember: always embrace change and stay ahead of the curve."
