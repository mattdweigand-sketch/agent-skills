---
name: skill-tune
description: "Audit or refactor a skill or prompt artifact for prompt technical debt. Use when explicitly asked to review SKILL.md, AGENTS.md, CLAUDE.md, system prompts, command wrappers, or tool instructions for prompt debt, over-steering, context bloat, stale model-specific instructions, duplicated canonical rules, misplaced executable checks, or missing authority boundaries. Use as a debt review pass before or after skill creation; use skill-creator for net-new skill scaffolding."
---

# Skill Tune

Audit prompt artifacts for debt. Default to findings only; edit only when the user asks to apply, update, or fix the artifact.

## Thesis

Prompt artifacts are technical debt because model-specific steering decays silently as models and harnesses change. Own as little prompt as possible: keep durable knowledge in canonical context, put checkable behavior in code or tests, delete or isolate perishable steering, and leave generic behavior to stock platform defaults.

Load `references/prompt-debt-taxonomy.md` when classifying instructions. That file owns the stable bucket taxonomy, fate test, verification tiers, and action set.

Repo facts and conventions belong in the repo's canonical docs, not in a global skill. Command wrappers are prompt surface unless they merely invoke canonical workflows or deterministic checks.

## Workflow

1. For non-trivial or editable audits, scope the target path, canonical owner, and mode: audit-only or apply.
2. Read the target file, nearby metadata, and only the canonical docs needed to prove ownership or duplication.
3. Check trigger breadth, stale/model-specific steering, duplicated rules, context bloat, executable checks left in prose, missing provenance or freshness, and missing audit/apply boundaries.
4. For artifacts that grant tool use, writes, external actions, memory, credentials, or approvals, also check identity, tools, denials, approvals, logs, retention, and failure behavior.
5. Return concrete findings with one action each from `references/prompt-debt-taxonomy.md`.
6. If applying edits, make the smallest patch that reduces debt, then validate frontmatter/YAML, expected files, absence of extra prompt artifacts, and any available skill validator.

Do not rewrite for style alone, add generic model coaching, create generic docs, or move debt into another prompt artifact.
