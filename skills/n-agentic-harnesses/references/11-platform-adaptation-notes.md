# Platform Adaptation Notes

## Table Of Contents

- What this file is for
- Baseline rule
- Platform-specific additions
- What should stay the same
- Migration approach

## What This File Is For

Read this only when adapting the skill to a specific agent runtime, plugin
format, command surface, or packaging system.

## Baseline Rule

Keep `SKILL.md` and the referenced files as the canonical skill.

Treat runtime-specific files as adaptation layers, not the canonical design.

## Platform-Specific Additions

Possible additions in a platform-specific version:

- runtime-specific metadata
- command wrappers that point back to `SKILL.md`
- `agents/openai.yaml` metadata
- path or prompt trigger metadata
- validation scripts
- repo- or plugin-specific routing hints
- additional instructions for developer tools and MCP usage

Those additions should not rewrite the core skill logic. They should only help a
runtime discover, render, package, or route the same skill more effectively.

## What Should Stay The Same

Preserve:

- the skill slug and identity
- progressive disclosure design
- router behavior in `SKILL.md`
- reference file boundaries
- design plus evaluation as equal first-class jobs
- solo-dev default posture

## Migration Approach

When building a platform-specific version:

1. copy the canonical skill directory
2. add runtime metadata and only the minimum extra files needed
3. validate that the router still points to the same reference files
4. avoid turning the skill into a runtime-only internal document

If the platform version starts changing the actual architectural guidance, you
are no longer adapting it. You are forking it.
