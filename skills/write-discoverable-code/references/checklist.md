# Pre-Commit / Pre-PR Checklist

Run this before committing new code or opening a PR. Resolve enforced failures and explicitly review the judgment-based items.

**Automated subset:** run `scripts/check-discoverable-code.sh <target-dir>` first — it enforces `@deprecated` markers for paths with whole legacy-name components and reports TypeScript/Python type signals for public-API review. The type signals are advisory because a text search cannot reliably determine an API boundary. The items below are judgment-based checks.

## Names

- [ ] Every new function, type, file, and directory name is distinctive enough that grepping it in this repo returns only real usages of that thing (not hundreds of unrelated hits).
- [ ] Every new name is distinctive enough in this repository's actual search results. Use `references/banned-names.json` as advisory examples, not a deny list.
- [ ] Consistent spelling for every concept across the diff (no `orgId` in one file and `organizationId` in another).
- [ ] When a test exists, it is named after the source it covers (`foo.test.ts` ↔ `foo.ts`, `test_foo.py` ↔ `foo.py`).

## Types

- [ ] Every exported / public function has fully typed parameters and return value.
- [ ] Public TypeScript and Python APIs avoid opaque annotations (`any`, `Object`, `Any`, untyped variadics); the script reports broad advisory signals, so confirm the public-API boundary manually.
- [ ] For Go, Java, Rust, Ruby, or any other language: no `interface{}`, `Object`, `Box<dyn Any>`, or untyped signatures on public APIs.
- [ ] Consider branded types / newtypes when primitive-shaped IDs or quantities could be swapped (see SKILL.md §2 for examples).

## Comments

- [ ] The one-line "why" comment sits directly above each new public definition.
- [ ] No decorative header banners or in-body README-style prose added.

## Legacy

- [ ] Any legacy paths this PR keeps around are marked `@deprecated` (or language equivalent) — enforced by the script when `legacy`, `deprecated`, or `old` appears as a whole filename or directory component.

## Repo Conventions

- [ ] `AGENTS.md` / `CLAUDE.md` updated if this PR changes naming conventions, source layout, or script entry points.
