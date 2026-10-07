# ICM Conventions

Adapted from Jake Van Clief's supplied ICM repository and walkthroughs, using agent-neutral entry guidance and task-sized workspaces. Apply only the patterns the work needs. See the [source record](sources/provenance.md#source-record) and [examples](examples.md).

## Workspace shape and routing layers

A workspace groups a responsibility, client, or mode of work. A stage performs one step in a sequential workflow. One workspace can use `AGENTS.md`, local context, and its existing working folders. A collection can route directly to each workspace's `CONTEXT.md`.

The lessons' map, rooms, and tools model is a teaching simplification. The expanded model below adds stage contracts and separates reusable references from task inputs; it does not require five folder levels.

| Layer | Role | Contents |
|---|---|---|
| 0: `AGENTS.md` | Entry map | Purpose, actual folder map, task routes, shared conventions |
| 1: Workspace `CONTEXT.md` | Local guidance | Task inputs, process, outputs, quality criteria; pipeline table if needed |
| 2: Stage `CONTEXT.md` | Optional stage contract | Inputs, Process, Outputs, Checkpoints, and applicable Audit |
| 3: References | Reusable guidance | Voice rules, design systems, conventions, domain skills |
| 4: Working artifacts | Per-run material | Sources, drafts, code, previous-stage outputs |

References constrain the work; task artifacts are what the agent transforms. Keep short local rules in context and extract long, shared, or duplicated guidance. Read only the layers and sections the task needs. Preserve established code and artifact locations.

Determine an input's role from its use and authority for the current consumer, not its folder or layer label. Keep the original request distinct from a proposed interpretation; preserve observations, derived claims, assumptions, and chosen scope without turning one into another.

## Roles and separate agents

Start with one agent following task-specific instructions and tools. A role, folder, or stage does not require a separate agent. When delegation is authorized and supported, add a helper for independent work that benefits from parallel execution, a task whose context would overwhelm the main session, or continuous work that needs a separate supported runtime. Name the bounded job, inputs, output, and handoff; weigh the benefit against token use, waiting, and coordination costs. A monitoring role alone does not authorize scheduling or persistent execution.

## Loading and access

`AGENTS.md` is the template convention. Connect entry guidance through the active agent's supported instruction mechanism, or provide it explicitly. Preserve established entry-point ownership instead of creating competing instruction files.

Verify the named instructions were read and required skills are available and loaded using the environment's supported mechanism. A filename, routing-table entry, or skill folder alone proves neither. Folder separation and routing exclusions guide context selection; access isolation requires tool permissions and the execution environment.

Select sources for the intended audience and use. Internal notes may support a private task without being eligible for public reuse. Honor existing user authorization and resolve unclear sharing scope before including restricted material; an `approved-material/` label is not permission.

## Pattern 1: Stage contracts

Use the [stage template](templates.md#stage-contract) for actual sequential work. Inputs, Process, and Outputs express Input, Do, and Output. Checkpoints declares the Human check; Audit is the agent's quality check. A stage without human review states None and why, without adding a pause. One simple task does not need a separate stage contract.

## Pattern 2: Stage handoffs via output folders

For file-based pipelines, a stage's `output/` folder is the default handoff: Stage N writes `stages/0N-name/output/[topic]-[artifact].md`, and the next stage names that exact artifact as input. Preserve deliberate external handoffs by identifying the producer, consumer, location, and review point.

Distinguish sources, drafts, and reviewed outputs through locations, filenames, or existing status metadata. Keep uncertainty and approval status intact: an unconfirmed date or suggestion must not become a commitment. File presence or a `final` filename alone does not establish review.

For alternate versions or repeated runs, identify the exact artifact selected for the consumer and what review applies to it. When a load-bearing input changes, reconsider the affected output and downstream readiness before reuse. Check the handoff in the consumer's actual receiving surface. Existing filenames or status metadata are sufficient when unambiguous.

## Pattern 3: One-way dependencies

Keep execution dependencies acyclic. A stage can consume an earlier stage's output or shared reference; that producer must not depend on its consumer to perform its own work. Check the dependency graph when adding a handoff. Navigational backlinks are not execution dependencies.

## Pattern 4: Selective section routing

Name the needed files and sections, plus concrete exclusions where they help prevent irrelevant context from entering a task. Use the routing templates' **Do NOT load** column; write None when no exclusion is useful. Exclusions do not override required entry instructions.

| File | Section to load | Do NOT load | Why |
|---|---|---|---|
| `voice-rules.md` | Voice rules | Historical rationale | Drafting tone |
| `meeting-notes.md` | Full file | None | Follow-up evidence |

Compare required inputs with actual reads. Report unreadable, omitted, or partially read files and sections and the resulting output limits. Use manageable input groups when needed; file count alone does not establish that the material fits.

For extracted decisions, commitments, or consequential factual claims, retain a source identifier and short supporting passage or precise location, beside the item or in review notes, including through summaries. Preserve units and time periods with consequential values. Distinguish suggestions, decisions, actions, and contradictions where relevant. This requirement applies to source-derived work, not every line of a creative or code artifact.

## Pattern 5: Canonical sources

Give each fact or rule one authoritative home; replace duplicate directions with links. When a fact or decision changes, update its owner, date information whose currency matters, retire superseded directions, and retain consequential decision reasons. Preserve historical evidence separately from active guidance without adding a tracking system by default.

Keep chosen scope in one maintained home, or explicitly select a frozen reviewed copy for a run. A copied scope document does not become a second independently editable authority.

## Pattern 6: Concise local context

`CONTEXT.md` answers: what happens here, what to read, and how the task proceeds. Brief audience, voice, quality, or code conventions can stay inline. Aim for a useful page; extract material only when its length, reuse, or duplication justifies a separate reference.

## Pattern 7: Tool prerequisites

Name required tools and check their availability. For missing setup knowledge, link a guide describing installation, verification, and how the workspace uses the tool. Keep a guide with its stage or in shared references when several stages use it. Bundled scripts can still require external runtimes or dependencies; inspect them rather than assuming the bundle is self-sufficient.

## Execution allocation

For each task step, identify what existing tools or code can execute, what needs model interpretation, and what requires human judgment. Reuse available tools first. Prefer a supported export or API to repeated interface clicks when it fits the task and permissions. A repeatedly predictable step with fixed rules is a candidate for a narrow script; keep work requiring interpretation with the model and responsible person.

Give new automation clear inputs and outputs, preserve established code locations, and add its command and use condition to the task route. Compare it with a known manual result using representative inputs and task-appropriate failure cases before relying on it. Automate one demonstrated step at a time. Repeatable execution does not establish semantic correctness, and code invoking a learned model still needs its output checked. A scripts folder and a separate composition audit are optional, not prerequisites.

## Trigger keywords

Add triggers only when used:

- `setup`: collect unresolved system-level configuration through the [questionnaire](templates.md#questionnaire), using known values directly.
- `status`: inspect declared output locations and report progress against the stage's quality and review requirements. Distinguish an existing artifact from a completed, reviewed stage.

## Naming conventions

Use `lowercase-with-hyphens` for new workflow paths, preserve `AGENTS.md`, `CONTEXT.md`, and established codebase names, and number stage folders only where order matters. Use descriptive output names such as `[topic]-[artifact].md`. Do not rename existing paths merely to match an example.

## Pattern 8: Questionnaire design

Use onboarding only for unresolved persistent configuration. Present a flat list of missing questions in one pass, with useful defaults or examples. Derive values where justified, map answers to placeholders and target files, and reuse saved configuration until requirements change. Collect per-run details at task entry. For voice or style, request concrete examples when abstract descriptions are insufficient.

## Pattern 9: Bundled skills

Use existing available domain skills when suitable. Bundle a local copy only when portability requires it, preserving dependencies and notices. Apply [loading and access](#loading-and-access).

Look first in configured skill locations; search external repositories only when needed and within the task's scope. Offer candidates when the user has a meaningful choice. Stage Inputs can point to the selected entry file and the specific rules needed. Keep workspace-owned configuration beside the skill, not inside it.

Bundle skills that supply runtime domain knowledge, such as document formatting or data analysis. Platform setup helpers, such as account configuration or connector registration, ordinarily belong in the environment's setup rather than the workspace bundle.

## Pattern 10: Specs are contracts

A specification defines the intended outcome and acceptance criteria for its consumer. In video production, it may define beats, approximate timing, visual meaning, audio cues, and color flow, leaving frames, component implementation, and pixel placement to the build stage. Other domains may need architecture and implementation constraints in the spec; use criteria appropriate to the work.

## Pattern 11: Checkpoints

For creative stages, identify a review point after a complete unit of work: who reviews which artifact, what they check, and the decision before continuing. Place it between process steps. Linear stages can declare None with a reason. Use supplied decisions and existing authorization rather than asking again for settled choices.

## Pattern 12: Stage audits

Creative and build stages need specific quality checks before an output is treated as ready. Extraction also needs source-fidelity checks when consequential claims are involved. Revise failed work before handing it on. A simple workspace can state the relevant check locally without a separate stage or audit file.

For an actual iterative stage, set an appropriate attempt, time, or cost limit. At that limit, return the best attempt with unresolved failures and its readiness stated. Do not introduce retries into every task.

## Pattern 13: Value validation

For content work, define what the output should accomplish, such as teaching a concept or enabling a practical action. Reuse one workspace-owned framework if useful; do not introduce a new taxonomy or review gate for a settled task.

## Pattern 14: Docs over outputs

Canonical guidance defines how to build. Prior outputs do not automatically become authority. Explicitly selected writing samples or approved examples may guide a task; keep their facts scoped to their original context. Keep a one-off creative adjustment with its artifact. Promote useful lessons and recurring corrections into their canonical owner after checking another relevant case.

## Pattern 15: Shared constants

Keep reusable code configuration, such as colors, fonts, or timing, in shared files imported by consumers. Configure known values directly; use onboarding only for unresolved choices. Non-code workspaces keep shared values in canonical references.

## Quality guardrails

Review context files over 80 lines and maintained workspace references over 200 lines for repetition or useful section routing. These are review signals, not automatic splitting rules for sources or template collections. Use plain language, valid Markdown, and `.gitkeep` only for required empty folders that must persist in Git.
