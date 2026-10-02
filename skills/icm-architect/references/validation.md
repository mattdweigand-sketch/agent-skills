# ICM Validation

Checks adapted from the original workspace-builder validation stage, including the requested explicit file roles. Apply to the target workspace, using [conventions](conventions.md) and [templates](templates.md). Report pass, gap, requested adaptation, not applicable, or unverified with source and target evidence.

Check the three file roles against the templates: AGENTS.md maps jobs to their entry points; workspace CONTEXT.md lists each stage/contract, command or trigger, output artifact/location, and human check; stage CONTEXT.md defines the execution contract. Each overview output and human check must agree with its stage contract. The stage-contract shape in check 6 applies to stage routers. Preserve explicitly specified uppercase filenames such as `AGENTS.md` and `CONTEXT.md` when checking naming. Questionnaire mapping declarations are not unresolved configuration values. Note other source contradictions rather than inventing requirements.

Run each check below. Record pass/fail and any issues found.

1. **Cross-reference integrity.** Every file path mentioned in any CONTEXT.md Inputs table must point to a real file in the generated workspace. List any broken references.

2. **No circular dependencies.** Trace the reference graph. If Stage A references Stage B, Stage B must not reference Stage A (directly or through other stages). Draw the dependency graph and confirm it is a directed acyclic graph.

3. **Placeholder coverage.** Scan all markdown files for `{{PLACEHOLDER}}` patterns. Every placeholder found must have a corresponding question in the questionnaire. Every question must map to at least one file that contains its placeholder. List any orphaned placeholders or orphaned questions.

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
