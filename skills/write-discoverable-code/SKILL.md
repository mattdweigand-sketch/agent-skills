---
name: write-discoverable-code
description: "Write and review source code with distinctive names and precise public APIs so coding agents can find it efficiently across text search, repo maps, and semantic retrieval. Do NOT load for Markdown corpora, wikis, or docs sites that navigate via explicit indexes and wikilinks. Do NOT load for prompt/skill authoring — use `create-skill` or `skill-tune`. Use when writing, reviewing, or refactoring code in a repository; picking names for functions/files/types/directories; tightening type annotations; or drafting an AGENTS.md/CLAUDE.md for a code repo. Triggers: 'write this code', 'review this code', 'refactor this file', 'name this function/file/type', 'is this agent-navigable', 'grep-friendly', 'discoverable code'."
metadata:
  author: matthew-weigand
  version: '1.3'
---

# Write Discoverable Code

## When to Use This Skill

Load when writing, generating, reviewing, or refactoring source code — new files, PR review, renames, type tightening, monolith refactors, or AGENTS.md authoring for a code repo.

Do NOT load for Markdown wikis, documentation sites, or prose corpora whose navigation is explicit (index files, wikilinks, routed AGENTS.md); they solve discoverability without grep. Do NOT load for prompt/skill authoring — use `create-skill` or `skill-tune`.

## The Core Mental Model

Many coding-agent workflows lean on **plain-text search** (grep/ripgrep) as a first pass. Others supplement it with repo maps, language servers, or semantic retrieval. Names that are useful search terms remain useful across these retrieval methods.

A common navigation loop:

1. **Search** the repo with `rg` for a symbol or filename
2. **Read** a window around the best hit
3. **Decide** if that's enough context; if not, search again with a better query
4. **Edit**

Every input you as the code author control feeds step 1: the names on your files, functions, types, and directories. Filenames are search terms too (`rg --files`), so a `session-broker/` directory is a hit before the agent opens anything.

**The single lever:** make the words in your code good search terms.

## The Rules (in order of payoff)

### 1. Names must be distinctive

Generic names return hundreds of unrelated hits and burn thousands of tokens as the agent reads windows to disambiguate. Distinctive names resolve in one hop.

Evaluate names against the target repository: a name is too generic when searching it produces many unrelated hits. Do not use a fixed hit count or global deny list in place of that judgment.

**Examples of generic names and worked bad→good alternatives live in `references/banned-names.json`.** Treat them as review prompts, not an automatic deny list: inspect the target repository's actual search results and conventions.

This is the highest-leverage rule. Everything else in this skill is a distant second.

### 2. Types tell the agent how to use code without opening it

A precise signature often answers the agent's first question without a file read:

```ts
// Good — agent may never need to open the body
function enrich(user: User): EnrichedUser

// Bad — agent must read the implementation to learn what `data` is
function enrich(data)
```

On public APIs, avoid `any` / `as any` / `Object` / `Function` (TypeScript); bare `Any`, untyped `**kwargs`, untyped `*args` (Python); and `interface{}` (Go). These often conceal the same usage information as an untyped signature. Judge local implementation trade-offs separately from public interfaces.

**Branded types / newtypes** for identifiers that share a primitive shape (`OrgId` and `UserId` instead of two `string`s) can turn argument swaps into compile errors. Consider them when a function takes:

- two parameters of type `string` that represent different identifiers
- two parameters of type `number` that represent different quantities (retry count, timeout ms)
- a token, key, secret, or URL as bare `string`
- a currency amount as bare `number`

Type names are search terms too. `OrgId` grep-resolves cleanly; `Result`, `Data`, `Config` do not. Compiler errors are the fastest feedback loop the agent has — a typed API is worth more than any comment.

### 3. Put the comment on the definition

Search often lands on the definition. Put the one-line comment that explains the *why* the code cannot say itself directly above that definition. Skip decorative headers and README-style prose; keep critical context close to the definition.

### 4. Small rules that add up

- **One spelling per concept.** `orgId` and `organizationId` split searches. Pick one and use it everywhere. Same for import aliases.
- **Unique names pierce barrel files.** `export *` re-exports erase names, so a call site importing from `@modem/common` gives the agent no path to the definition — but a distinctive symbol name lands there directly.
- **Name tests after the source they cover.** `stripe.test.ts` ↔ `stripe.ts`. `test_stripe.py` ↔ `stripe.py`.
- **Mark legacy paths `@deprecated`** (or the language equivalent). Better yet, delete them.
- **Write an `AGENTS.md` / `CLAUDE.md`** in the repo root. Record naming conventions, source layout, script entry points. Template in `references/agents-md-stanza.md`.

## Why This Matters (the evidence)

The cited experiments found large retrieval and cost gains from more discoverable code in many configurations, especially where names were less distinctive. Results varied by model and harness; treat them as directional evidence, not a universal benchmark.

## Workflow: Writing New Code

1. Say in one specific sentence what the file/function/type does.
2. Turn the nouns in that sentence into the name. `hmac-payload-signer.ts` came from "signs notification payloads with HMAC."
3. Type every public signature. Consider a branded type / newtype when a bare `string` or `number` could be confused with another primitive-shaped value.
4. Write the one-line "why" comment on the definition.

## Workflow: Reviewing Existing Code

1. Run the automated checks first: `scripts/check-discoverable-code.sh <target-dir>`. It enforces unmarked legacy paths whose names contain a whole legacy component and surfaces TypeScript/Python type signals for public-API review.
2. Then run the checklist in `references/checklist.md` against the file or PR for the expert-checkable items (name distinctiveness, one-spelling-per-concept, test naming, comment-on-definition, branded-type opportunities, and public-API scope).
3. For each failing item, propose the specific rename or annotation — do not just flag it.

## Workflow: Refactoring a Monolith

When a module is unusually large or search-hostile—for example, it contains many nested definitions under one wrapper—review it for independently named concepts. Do not make architectural changes unless the task asks for them:

1. Identify the distinct concepts inside (Odysseus's `email_routes.py` contained SMTP settings, message rendering, folder fallbacks, delivery history).
2. Split into concept-named modules, one file per concept. Filenames become search terms.
3. Preserve behavior mechanically — run existing tests before and after.
4. Update `AGENTS.md` to point at the new layout.

## What This Skill Does NOT Cover

- **Retrieval strategy** (embeddings, repo maps, LSP-backed tools). This skill keeps source text useful to the retrieval methods a repository already uses.
- **Architecture** (module boundaries, service splits, framework choice). Upstream of naming.

## References and Scripts

- `references/banned-names.json` — advisory examples of generic file and symbol names, with bad→good alternatives.
- `references/checklist.md` — the pre-commit / pre-PR checklist for expert-checkable items.
- `references/agents-md-stanza.md` — drop-in AGENTS.md template for new code repos.
- `scripts/check-discoverable-code.sh` — ripgrep-backed legacy-marker enforcement plus advisory TypeScript/Python public-API review signals. Requires `rg`.

---

*Owner: Matt Weigand. Last reviewed: 2026-08-10. Source: [Modem — How coding agents read your code](https://modem.dev/blog/how-coding-agents-read-your-code) (2026-07-20). Re-review when coding-agent retrieval strategies materially shift, when Modem publishes Part 2 with new evidence, or when the advisory name examples need a language-specific refresh.*
