---
name: skill-tune
description: "Audit or refactor a skill or prompt artifact for prompt technical debt. Use when explicitly asked to review SKILL.md, AGENTS.md, CLAUDE.md, system prompts, command wrappers, or tool instructions for prompt debt, over-steering, context bloat, stale model-specific instructions, duplicated canonical rules, misplaced executable checks, or missing authority boundaries. Use as a debt review pass before or after skill creation; use skill-creator for net-new skill scaffolding."
---

# Skill Tune

Audit prompt artifacts for debt. Default to findings only; edit only when the user asks to apply, update, or fix the artifact.

## Thesis

When available, audit against the user-supplied canonical prompt-debt thesis. Compact fallback: own as little prompt as possible. Keep durable knowledge in canonical context, put checkable behavior in code or tests, and delete or isolate perishable steering.

Classify each meaningful instruction by format, fate, and verification:

| Bucket | Meaning | Preferred home |
|---|---|---|
| Durable | Stable facts, principles, reusable workflow contracts | Workflow contracts in `SKILL.md`; repo facts in canonical project docs; bulky context in references; factual claims need provenance or freshness |
| Perishable | Model-specific steering, tone hacks, brittle behavioral nudges | Stay stock, delete, shorten, isolate, or put on an audit clock |
| Executable | Anything a machine can check or perform reliably | Scripts, tests, schemas, hooks |
| Reference | Bulky examples, API details, domain docs, templates | `references/` or `assets/` |
| Duplicate | Rule already owned by a canonical file or platform default | Replace with a pointer or remove |

Fate test: if it breaks on the next model, rent it and keep it minimal; if the next model can regenerate it, treat it as commodity infrastructure; if it depends on owned outcome context, preserve its provenance.

Verification test: Tier 1 machine-checkable rules need rails; Tier 2 expert-checkable rules need review or eval evidence; Tier 3 genuine judgment may stay as prompt steering.

Repo facts and conventions belong in the repo's canonical docs, not in a global skill. Command wrappers are prompt surface unless they merely invoke canonical workflows or deterministic checks.

## Workflow

1. For non-trivial or editable audits, scope the target path, canonical owner, and mode: audit-only or apply.
2. Read the target file, nearby metadata, and only the canonical docs needed to prove ownership or duplication.
3. Check trigger breadth, stale/model-specific steering, duplicated rules, context bloat, executable checks left in prose, missing provenance or freshness, and missing audit/apply boundaries.
4. For artifacts that grant tool use, writes, external actions, memory, credentials, or approvals, also check identity, tools, denials, approvals, logs, retention, and failure behavior.
5. Return concrete findings with one action each: keep, stay stock, shorten, move to reference, move to script/test/schema/hook, add provenance, delete, retune, or needs owner decision.
6. If applying edits, make the smallest patch that reduces debt, then validate frontmatter/YAML, expected files, absence of extra prompt artifacts, and any available skill validator.

Do not rewrite for style alone, add generic model coaching, create generic docs, or move debt into another prompt artifact.
