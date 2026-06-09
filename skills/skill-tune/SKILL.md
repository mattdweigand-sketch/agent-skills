---
name: skill-tune
description: "Audit or refactor a skill or prompt artifact for prompt technical debt. Use when explicitly asked to review SKILL.md, AGENTS.md, CLAUDE.md, system prompts, command wrappers, or tool instructions for prompt debt, over-steering, context bloat, stale model-specific instructions, duplicated canonical rules, or misplaced executable checks. Use as a debt review pass before or after skill creation; use skill-creator for net-new skill scaffolding."
---

# Skill Tune

Audit prompt artifacts for debt. Default to findings only; edit only when the user asks to apply, update, or fix the artifact.

## Thesis

When available, audit against the user-supplied canonical prompt-debt thesis. Compact fallback: own as little prompt as possible. Keep durable knowledge in canonical context, put checkable behavior in code or tests, and delete or isolate perishable steering.

Classify each meaningful instruction:

| Bucket | Meaning | Preferred home |
|---|---|---|
| Durable | Stable facts, principles, reusable workflow contracts | Workflow contracts in `SKILL.md`; repo facts in canonical project docs; bulky context in references |
| Perishable | Model-specific steering, tone hacks, brittle behavioral nudges | Delete, shorten, isolate, or put on an audit clock |
| Executable | Anything a machine can check or perform reliably | Scripts, tests, schemas, hooks |
| Reference | Bulky examples, API details, domain docs, templates | `references/` or `assets/` |
| Duplicate | Rule already owned by a canonical file or platform default | Replace with a pointer or remove |

Repo facts and conventions belong in the repo's canonical docs, not in a global skill. Command wrappers are prompt surface unless they merely invoke canonical workflows or deterministic checks.

## Workflow

1. For non-trivial or editable audits, scope the target path, canonical owner, and mode: audit-only or apply.
2. Read the target file, nearby metadata, and only the canonical docs needed to prove ownership or duplication.
3. Check trigger breadth, stale/model-specific steering, duplicated rules, context bloat, executable checks left in prose, and missing audit/apply boundaries.
4. Return concrete findings with one action each: keep, shorten, move to reference, move to script/test/schema/hook, delete, retune, or needs owner decision.
5. If applying edits, make the smallest patch that reduces debt, then validate frontmatter/YAML, expected files, absence of extra prompt artifacts, and any available skill validator.

Do not rewrite for style alone, add generic model coaching, create generic docs, or move debt into another prompt artifact.
