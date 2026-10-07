# ICM Validation

Inspect the exact target and version. Use the [conventions](conventions.md) and relevant [templates](templates.md); report pass, gap, requested adaptation, not applicable, or unverified with file evidence. First identify whether the target is one workspace, a collection, or a staged pipeline. Do not require unused stages, questionnaires, or reference folders.

## Checks

1. **Routing and coverage.** Resolve task routes and declared inputs, identify producers of generated inputs, and check actual reads against [selective routing](conventions.md#pattern-4-selective-section-routing). Inspect useful exclusions as well as inclusions. Apply [loading and access](conventions.md#loading-and-access).
2. **Dependencies.** Check execution dependencies for cycles or broken producer/consumer relationships; distinguish them from navigational backlinks.
3. **Configuration.** For reusable templates, map unresolved persistent values to questions or justified derived values and target files. Use known values directly. Exclude mapping declarations and illustrative examples from unresolved-value scans.
4. **Conditional sections.** Every `{{?SECTION}}...{{/SECTION}}` block wraps a complete section. Flag inline wrapping.
5. **Handoffs.** Match producer outputs to consumer inputs, including deliberate external systems. Check source/draft/review status and preservation of uncertainty against [handoff rules](conventions.md#pattern-2-stage-handoffs-via-output-folders). A standalone task needs an output destination, not an invented consumer.
6. **Ownership and freshness.** Flag duplicate authority, stale active directions, missing dates where currency matters, and unexplained consequential decisions. Allow short local context. Report unknown currency instead of assuming freshness.
7. **Contracts and review.** When stages exist, their overview outputs and human checks agree with contracts. Checkpoint step numbers resolve, with reviewer, artifact, criteria, and decision; None has a reason. Apply [checkpoint guidance](conventions.md#pattern-11-checkpoints) without reopening settled decisions.
8. **Quality and evidence.** Assess observable acceptance criteria. For source-derived items, inspect supporting references and certainty under [selective routing](conventions.md#pattern-4-selective-section-routing); report contradictions. Keep workspace checks proportional to the task.
9. **Specifications.** Match outcome and acceptance criteria to the consumer. The video-production WHAT/WHEN versus HOW split is not a universal rule for software architecture.
10. **Size and naming.** Apply the conventions' review signals and naming rules. Do not split sources automatically or scaffold unused empty folders.
11. **Prerequisites and execution.** Verify required tools or report the unverified prerequisite. Check added helpers against [agent criteria](conventions.md#roles-and-separate-agents) and automation against [execution allocation](conventions.md#execution-allocation), including comparison with a known manual result. Check authored Markdown, local references, and unclear terminology.

For an audit, report findings without editing. For an authorized repair, fix failed checks and rerun them.

## Representative task and repair

Follow one task from fresh entry context through scoped inputs, output, relevant review, and an actual consumer if present. For builds or authorized repairs, run it when feasible before expanding. If execution is unavailable or outside the audit's scope, use a static trace and mark behavior unverified. Do not authorize an external action merely to complete the check.

Use populated inputs and task-appropriate acceptance and rejection criteria. Observe required reads, applicable tool use, and output placement. When another person receives the work, check whether they can find the selected current input, understand the result, and make the intended next decision without the builder's explanation. Record confusion and repair its owner before expanding the workspace.

For fresh-session orientation, ask what the workspace is, what is in progress, and what comes next; compare the answers with the selected current artifacts and review status. Unknown status should remain unknown. For a human handoff, also check whether the receiver can follow the map, locate inputs and tools, and carry out the intended work or next decision without AI assistance. A static inspection or builder walkthrough leaves independent human usability unverified. If the task itself requires AI, test the human's navigation and next decision rather than requiring replacement of that capability.

Report passed, failed, skipped, and unverified checks separately. A structural check establishes only the property checked; it does not establish semantic correctness or usefulness to the receiver.

Recheck a representative task after model, tool, or instruction changes before calling the workflow validated under the new conditions. Record the relevant configuration.

For one demonstrated failure:

1. Find the source, route, or rule that should have prevented it. Fix missing or stale context at its owner.
2. Make one targeted change. Compare the same request and inputs in separate fresh sessions and clean copies, keeping model/tools constant when possible. Exclude earlier drafts and corrections. Declare source or environment differences and any limits on the comparison.
3. Compare the result with the original failure and source evidence. Use accepted, usable output, correction effort, and maintenance burden where relevant to the intended improvement. Keep an improvement, revise an ineffective change, and remove noise.
4. Check another relevant example before generalizing. One successful run is evidence for that case, not a reliability guarantee.

See the [fictional repair example](examples.md#repair-and-source-fidelity).

## Safe migration

Before moving or replacing existing files, establish the durable destination and a usable backup or Git recovery point. Stage replacements from the current working copy; reconcile differences with the maintained source and recheck that baseline before applying the update so local fixes survive.

1. Map source/destination paths and known consumers, including relative links and symlinks. Record unknown coverage. Plan authorized consumer updates and check all proposed moves for overlap and case-insensitive collisions.
2. Run the read-only checker for each pair. It requires an absent destination. Copy without overwriting, keeping source and copied bytes unchanged until verification passes.
3. Run `--verify` to compare relative file/directory inventories and whole-file SHA-256 hashes, including binaries and empty directories. On failure, retain the source, report the partial destination, and resolve the problem before retrying. Only verified copies may proceed to already-authorized removals.
4. Apply approved content/reference updates and recheck affected consumers from the new location. Passing checks does not authorize deletion or publication.

From the skill directory, with Python 3.9 or newer:

```sh
python3 scripts/migration_preflight.py /absolute/source /absolute/destination
python3 scripts/migration_preflight.py /absolute/source /absolute/destination --verify
```

The checker rejects overlaps, existing preflight destinations, case/Unicode-normalization collisions, symlinks, and special files. It reads only and returns JSON: exit 0 passes, 1 indicates check/filesystem failure, and 2 indicates invalid syntax. It does not discover consumers, compare multiple planned moves, verify permissions/extended attributes, or stop concurrent writers. Use quiescent inputs and separately plan symlink moves.

**macOS temporary paths:** `/tmp` commonly aliases `/private/tmp`, so the checker's symlink-ancestor rejection can reject an otherwise ordinary staging path. Inspect the trusted temporary-root alias, then use its explicit `/private/tmp/...` path. Do not blindly resolve untrusted paths or disable symlink checks to make a migration pass.
