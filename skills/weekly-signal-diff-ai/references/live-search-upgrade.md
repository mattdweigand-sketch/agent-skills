# Live Search Upgrade — AI Edition

Use this file only when the environment supports current web retrieval and the user wants fresh, source-backed coverage.

## Preferred Upgrade Path

For OpenRouter users, prefer the Perplexity Sonar family for the retrieval pass. Start with the strongest Sonar search tier available. Use the plain Sonar tier as the lowest-cost fallback when budget matters more than depth.

Useful references:

- [OpenRouter: Perplexity Sonar](https://openrouter.ai/perplexity/sonar/api)
- [Perplexity Sonar docs](https://docs.perplexity.ai/docs/sonar/models/sonar)
- [Perplexity search filters](https://docs.perplexity.ai/docs/grounded-llm/chat-completions/filters/academic-filter)

## Preferred Outlets

Weight or filter toward these when domain control is available:

- The Verge, Ars Technica (AI coverage)
- TechCrunch AI
- MIT Technology Review
- Bloomberg Technology / Bloomberg Intelligence AI coverage
- Financial Times AI coverage
- Nature, Science (for research breakthroughs)
- arXiv (cs.AI, cs.LG, cs.CL) for model releases
- Hugging Face blog for open model releases
- Regulatory: EU AI Office (europa.eu), NIST (nist.gov), US Federal Register

Deprioritize pure benchmark comparisons, product launch press releases, or funding announcements that do not change economics, dependencies, or competitive structure.

## Retrieval Pattern

Run the search in two passes:

1. **Broad sweep**
   - Scan the last 7 days across the 10 suggested AI categories
   - Return only source-backed developments with links or citations
   - Shortlist stories that look like structural change: regulatory, compute economics, dependency shifts, distribution, business model changes

2. **Targeted follow-up**
   - Deepen only the top 3-7 candidate shifts
   - Tighten recency, domain filters, or entity filters when needed
   - Pull enough evidence to explain both general impact and personal relevance

## What to Ask the Search Layer For

Prefer prompts or search instructions that request:

- A 7-day freshness window unless the user says otherwise
- Cited links or explicit source URLs
- Domain filters favoring the preferred outlets above
- One-paragraph explanations of why each result matters structurally (not announcement-driven)
- Rejection of pure benchmark posts, press release restatements, or product launches that do not move economics or constraints

## Automation Notes

For scheduled runs:

- Keep retrieval and synthesis structure consistent every week so diffs stay comparable
- Store the final digest back in Open Brain so next week's run has something to diff against
- Track the week-ending date in the saved summary
- If cost matters, use a cheaper broad sweep and spend extra search depth only on the top candidate shifts

The search layer finds evidence. Open Brain and active project context decide what matters to this user. Keep those roles separate.
