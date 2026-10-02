# ICM Validation

Checks adapted from the original workspace-builder validation stage, including the requested explicit file roles. Apply to the target workspace, using [conventions](conventions.md) and [templates](templates.md). Report pass, gap, requested adaptation, not applicable, or unverified with source and target evidence.

Check the three file roles against the templates: AGENTS.md maps jobs to their entry points; workspace CONTEXT.md lists each stage/contract, command or trigger, output artifact/location, and human check; stage CONTEXT.md defines the execution contract. Each overview output and human check must agree with its stage contract. The stage-contract shape in check 6 applies to stage routers. Preserve explicitly specified uppercase filenames such as `AGENTS.md` and `CONTEXT.md` when checking naming. Questionnaire mapping declarations are not unresolved configuration values. Note other source contradictions rather than inventing requirements.

Run each check below. Record pass/fail and any issues found.

1. **Cross-reference integrity.** Every file path mentioned in any CONTEXT.md Inputs table must point to a real file in the generated workspace. List any broken references.

2. **No circular dependencies.** Trace the reference graph. If Stage A references Stage B, Stage B must not reference Stage A (directly or through other stages). Draw the dependency graph and confirm it is a directed acyclic graph.

3. **Placeholder coverage.** Check the discovery map identifies system-level variables, optional stages and their conditions, and required or optional tools per stage. Scan all markdown files for `{{PLACEHOLDER}}` patterns. Each system-level placeholder must map to a setup question or derived value and its target files; each per-run value must be collected by its entry contract. List orphaned variables, placeholders, or questions.

4. **Conditional section validity.** Every `{{?SECTION}}...{{/SECTION}}` block must wrap a complete section (a heading and all content below it). No inline conditional wrapping. Flag any violations.

5. **Stage handoff chain.** Verify the chain is unbroken: Stage N's output location must match what Stage N+1's Inputs table references. List the chain and flag any gaps.

6. **CONTEXT.md purity.** Verify no CONTEXT.md file contains actual reference content (definitions, extended rules, examples, guidelines). They should contain only: title, description, Inputs table, Process steps, Checkpoints table or explicit None with a reason, Audit table (optional), Outputs table.

7. **Checkpoints in creative stages.** Verify that stages doing creative work (writing, design, ideation) have at least one checkpoint. Verify checkpoint tables reference valid process step numbers. Each checkpoint identifies the reviewer, artifact, review criteria, and decision before continuing. Linear stages (extract, render, validate) may declare None with a reason; this declaration does not add an approval pause.

8. **Audits in creative/build stages.** Verify that stages doing creative or build work have an Audit section with specific, unambiguous pass conditions. Verify the audit runs after the process steps and before output is written.

9. **Contract purity in spec stages.** If the workspace has a specification stage, verify its output format defines WHAT and WHEN, not HOW. Check for component names, frame numbers, prop definitions, or spring configs in spec reference files. These are implementation details that belong to the build stage.

10. **Line count check.** Flag any CONTEXT.md over 80 lines. Flag any reference file over 200 lines.

11. **Naming conventions.** All folder and file names are lowercase-with-hyphens. Stage folders use zero-padded numbers (01-, 02-). Empty output/ folders have .gitkeep files.

12. **Tool prerequisites.** If the workspace has a prerequisites/ folder or tool setup guides: verify prerequisites/CONTEXT.md lists every tool, verify each listed tool has a setup guide, verify setup guides include install steps and verification commands, and verify the questionnaire asks whether optional tools are needed (so conditional stages can be removed).

13. **Quality scan.** Check for em dashes (replace with --), jargon without explanation, and markdown formatting issues.

For a build or authorized repair, fix issues and re-run the failed checks. For an audit, report them without editing.


Finish by tracing a representative task from a fresh context through its entry, scoped inputs, output, human check, and consumer. Say whether this was a static trace or an executed run.

## Safe migration

Use before moving or replacing existing workspace files. Establish the durable destination and a usable backup or Git recovery point. Temporary storage is staging, not the final workspace.

1. Map each source to its destination and identify internal links, relative paths, symlinks, and known external consumers. Record unknown coverage. A live consumer must keep working or receive an authorized update in the same migration. Check planned destinations against each other for overlaps and case-insensitive name collisions.
2. Run the read-only checker below for each source/destination pair. It requires an absent destination; resolve conflicts before copying. Copy without overwriting existing paths. Keep the source and copied bytes unchanged until verification passes.
3. Run `--verify`. It compares relative file/directory inventories and whole-file SHA-256 hashes, including binary files and empty directories. Only after parity passes may an authorized removal occur. On failure, retain the source, report the partial destination, and resolve the failure before retrying.
4. Apply authorized content and reference updates after copy verification. Recheck the affected consumers and task navigation from the new location. Use existing authorization; passing checks does not authorize deletion or publication.

From the skill directory, using Python 3.9 or newer:

```sh
python3 scripts/migration_preflight.py /absolute/source /absolute/destination
python3 scripts/migration_preflight.py /absolute/source /absolute/destination --verify
```

The checker rejects overlapping trees, existing destinations in preflight mode, case/Unicode-normalization collisions, symlinks, and special files. Reports are JSON; exit 0 means passed, 1 means a check or filesystem failure, and 2 means invalid command syntax. It reads only. It does not find consumers, compare multiple planned moves, verify permissions or extended attributes, or stop concurrent writers. Use quiescent inputs and recheck if they change; symlinks need a separately planned move that preserves their meaning.
