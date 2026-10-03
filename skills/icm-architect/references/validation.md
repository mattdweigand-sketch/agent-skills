# ICM Validation

Checks adapted from the original workspace-builder validation stage, including the requested explicit file roles. Apply to the target workspace, using [conventions](conventions.md) and [templates](templates.md). Report pass, gap, requested adaptation, not applicable, or unverified with source and target evidence.

First identify the actual shape: a simple workspace, a collection of responsibility or client workspaces, or a staged pipeline. AGENTS.md maps jobs to their entry points. Workspace CONTEXT.md provides concise local guidance and task routes; use the pipeline overview and stage contracts only where sequential handoffs need them. If stages exist, each overview output and human check must agree with its contract. Do not require missing stage folders, separate references, questionnaires, or extra entry files without a task-specific need. Questionnaire mapping declarations are not unresolved configuration values. Note other source contradictions rather than inventing requirements.

Assess each check below for applicability. Record findings without treating not-applicable checks as failures.

1. **Cross-reference integrity and loading.** Task routes and declared inputs must resolve to actual files or identified external sources available at the relevant step. For a generated input, identify its producer. Verify permitted source scope and required skill availability; a link or skill name alone does not prove loading or access isolation. Report observed reads separately from planned routes.

2. **No circular dependencies.** Trace the reference graph. If Stage A references Stage B, Stage B must not reference Stage A (directly or through other stages). Draw the dependency graph and confirm it is a directed acyclic graph.

3. **Configuration coverage, when needed.** For a reusable template, map unresolved system-level variables to questions or derived values and target files, including applicable optional stages and tools. Scan template configuration for `{{PLACEHOLDER}}` patterns. Use known values directly and collect per-run inputs at task entry. Do not require a questionnaire for an already configured workspace or treat placeholders in preserved source examples as active configuration.

4. **Conditional section validity.** Every `{{?SECTION}}...{{/SECTION}}` block must wrap a complete section (a heading and all content below it). No inline conditional wrapping. Flag any violations.

5. **Handoffs, when present.** A producer's output location must match its consumer's declared input, whether a stage folder, existing code or deliverable path, or intentional external system. List actual handoffs and flag gaps. For a standalone task, verify its output destination without inventing a downstream stage.

6. **Concise context and canonical ownership.** Allow short, locally owned guidance in CONTEXT.md. Flag long, shared, or duplicated material that should have a canonical reference. Stage contracts retain Inputs, Process, Outputs, and Checkpoints, with Audit where applicable; simple workspaces need only the guidance their tasks require.

7. **Checkpoints in creative stages.** Verify that stages doing creative work (writing, design, ideation) have at least one checkpoint. Verify checkpoint tables reference valid process step numbers. Each checkpoint identifies the reviewer, artifact, review criteria, and decision before continuing. Linear stages (extract, render, validate) may declare None with a reason; this declaration does not add an approval pause.

8. **Task quality checks.** Creative/build stages need specific, unambiguous audit conditions before output is finalized. A simple workspace can express the same relevant check in its local guidance without adding a stage or separate audit file.

9. **Specification scope, when applicable.** Check that a spec defines the intended outcome and acceptance criteria at the level needed by its consumer. Apply the video-production WHAT/WHEN versus HOW split only to that workflow; do not reject software architecture details because they differ from a video example.

10. **Context size.** Review CONTEXT.md over 80 lines and maintained workspace references over 200 lines for avoidable detail, duplication, or useful section routing. Length is a review signal; do not automatically split preserved sources or template collections.

11. **Naming conventions.** Use lowercase-with-hyphens for new workflow files, preserve `AGENTS.md` and `CONTEXT.md`, and respect established codebase naming. Number stage folders where sequence matters. Add .gitkeep only to required empty folders that must persist in Git; do not scaffold unused folders.

12. **Tool prerequisites.** Identify required tools and verify availability, or report unverified prerequisites. Link setup guidance where needed. If optional tool choices remain unresolved in a reusable template, include them in onboarding; a prerequisite does not itself require a new folder or questionnaire.

13. **Quality scan.** Check authored guidance for unexplained jargon and Markdown formatting issues. Preserve source examples verbatim; do not normalize their punctuation, filenames, or original platform terminology.

For a build or authorized repair, fix issues and re-run the failed checks. For an audit, report them without editing.


Finish with the existing representative-task check: start from fresh context and follow its entry, scoped inputs, actual output, relevant human check, and consumer if one exists. For builds or authorized repairs, run one task when feasible before expanding the structure; revise from demonstrated problems, re-run the affected task, and remove instructions that add noise. For read-only audits or unavailable execution, use a static trace and mark behavior unverified. Do not invent a downstream consumer or authorize an external action to complete this check.

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
