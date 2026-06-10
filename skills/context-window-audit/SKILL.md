---
name: context-window-audit
description: "Audit an agent setup for token waste, context-window bloat, stale instructions, and dead command wrappers. Use when the user says context-window audit, context audit, audit my context, check my settings, why is Codex so slow, token optimization, or asks why startup context is too large."
---

# Context Window Audit

Use this skill when the user asks for a context-window audit, context audit,
token optimization, settings cleanup, or an explanation of why an agent session
is loading too much context.

## Scope

Audit prompt and context surfaces that load automatically or are likely to be
pulled into many sessions:

- global and repo instruction files such as `AGENTS.md`, `CLAUDE.md`, command
  wrappers, settings, and skill descriptions
- enabled skills, plugins, and connectors when visible
- memory summaries or routed context files when they affect startup behavior
- repeated references that cause large files to be read by default

Do not audit private content for substance unless it is relevant to context
loading. The goal is smaller, clearer context, not content cleanup.

Load `references/context-surface-taxonomy.md` when classifying issues or
formatting the final audit. That file owns the stable action taxonomy and output
template.

## Process

1. Identify the startup path.
   - List the files, skills, commands, memories, or settings that are loaded or
     strongly routed at session start.
   - Separate automatic context from on-demand references.

2. Find bloat and dead routes.
   - Look for duplicated rules, stale model-specific instructions, wrappers that
     invoke missing skills or commands, broad "read everything" guidance, and
     large reference files that should be loaded only on demand.

3. Classify each issue.
   Use the action taxonomy in `references/context-surface-taxonomy.md`.

4. Report findings before edits.
   - Prioritize issues by token impact and failure risk.
   - Name the canonical owner for every duplicated rule.
   - Call out any command wrapper that points to a missing target.

5. Apply changes only if asked.
   - Keep edits narrow.
   - Preserve repo-specific authority boundaries.
   - Validate any edited skill frontmatter or command wrapper if a validator is
     available.

## Output

Use the output template in `references/context-surface-taxonomy.md`.

If no meaningful bloat is found, say that directly and list the remaining
context surfaces that still deserve periodic review.
