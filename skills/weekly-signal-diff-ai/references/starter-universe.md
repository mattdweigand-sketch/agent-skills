# Starter Universe — AI Edition

Use this file only when the user has not already defined a watchlist. The list below is a bootstrap scaffold, not a hard requirement.

Rules for using it:

- Start here only if the user has not provided categories, entities, or a source packet.
- Treat the categories and entities as suggested defaults.
- Re-rank, replace, or expand the list using Open Brain memory and active projects before writing the final diff.
- Preserve some baseline discovery. Do not personalize so aggressively that the scan stops surfacing new signal (new entrants, regulation shifts, and dependency changes matter even when they aren't tied to a current project).

## Suggested Categories and Entities

| Category | Suggested Entities |
| -------- | ------------------ |
| Frontier labs | OpenAI, Anthropic, Google DeepMind, xAI, Meta AI |
| Open models | Meta Llama, Mistral, Qwen, DeepSeek |
| Dev tooling & agents | Cursor, GitHub Copilot, LangChain, Vercel AI, Replit |
| Cloud AI platforms | AWS Bedrock, Azure OpenAI, Google Vertex AI |
| Data & model infrastructure | Hugging Face, Weights & Biases, Together AI, Replicate |
| Enterprise AI buyers | Salesforce, ServiceNow, SAP, Workday (AI layer moves) |
| Creative media AI | Midjourney, Adobe Firefly, ElevenLabs, RunwayML |
| Robotics & embodied AI | Figure, Boston Dynamics, Physical Intelligence |
| AI regulation | EU AI Act, NIST AI RMF, US executive orders, state-level bills |
| AI economics & compute | NVIDIA, TSMC, AMD; inference cost trends |

## Re-Ranking Heuristics

Promote an entity or category when:

- it shows up in active projects or recent Open Brain captures
- it directly competes with or enables tools the user currently uses
- a regulation or compute shift affects the user's stack or market view
- it appeared in the last digest and has unresolved momentum
- it represents a dependency shift (new model API, new pricing tier, new OSS release)

Demote or replace an entity or category when:

- it has low connection to current projects or recurring interests
- it generates plenty of headlines but little structural change (e.g., a benchmark screenshot without economic implications)
- the coverage is so broad it dilutes signal

## Coverage Note Template

Use wording like this at the top of the weekly diff:

`This week's scan started from 10 suggested AI categories and 30 suggested entities, then reweighted coverage using Open Brain context around [focus areas — e.g., frontier lab pricing moves, EU AI Act implementation, agentic tooling shifts].`
