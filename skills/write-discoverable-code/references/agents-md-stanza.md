# AGENTS.md — Drop-in Stanza for New Code Repos

Paste the following into the root `AGENTS.md` (or `CLAUDE.md`) of any new code repository. Edit the bracketed sections to match the repo.

---

## Code Conventions for Agents

This repository is written to be navigated by coding agents (Perplexity, Claude Code, Codex, Cursor, OpenCode, etc.). Agents find code by running `rg` (ripgrep) over the source, so the words in this repo are search terms. Follow these rules on every change.

### Naming

- **Distinctive names, always.** Every function, type, file, and directory name should be specific enough that grepping it returns only real usages. Prefer `createStripeClient` over `createClient` over `create`. Prefer `hmac-payload-signer.ts` over `signer.ts` over `client.ts`.
- **One spelling per concept.** [List the canonical spellings this repo uses, e.g. `orgId` not `organizationId`, `userId` not `uid`.]
- **Test files mirror their source.** `foo.test.ts` covers `foo.ts`. `test_foo.py` covers `foo.py`.
- **No generic module names.** `helpers.*`, `utils.*`, `common.*`, `misc.*` are banned. Split them into concept-named modules.

### Types

- Every exported function and public method has fully typed parameters and return value.
- No `any` (TS), `interface{}` (Go), `Object` (Java), or untyped `**kwargs` (Python) on public APIs.
- IDs and other primitive-shaped values that could be accidentally swapped use branded types / newtypes (e.g. `OrgId` and `UserId`, not two `string`s).

### Comments

- Put the one-line "why" comment directly above the definition it explains. That is the one line the agent is guaranteed to read.
- Skip decorative header banners and inline README-style prose.

### Legacy Code

- Mark legacy paths with `@deprecated` (or the language equivalent) so agents avoid them. Prefer deleting.

### Repo Layout

- **Source lives in:** [`src/` or equivalent]
- **Tests live in:** [`tests/` or colocated `*.test.ts`]
- **Scripts live in:** [`scripts/`, and each script is named after what it does — `bootstrap_remote_workspace.py`, not `bootstrap.py`]
- **Package manager:** [npm / uv / etc.]
- **Build / lint / test commands:** [list them]

### Reference

The reasoning behind these rules: [Modem — How coding agents read your code](https://modem.dev/blog/how-coding-agents-read-your-code).

---
