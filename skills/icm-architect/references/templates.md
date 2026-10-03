# ICM Templates

Copy only the templates needed for the task. Bracketed fields are authoring notation; complete them before delivering a configured workspace. These templates follow the [conventions](conventions.md); see [examples](examples.md) for compact adaptations.

## Workspace entry

Use for `AGENTS.md`. Route a collection to its workspaces; for one workspace, place local context beside the entry file without adding an extra directory.

````markdown
# [Project or Workspace]

[Purpose and audience.]

## Folder map

```
[project]/
├── AGENTS.md
└── [area]/
    ├── CONTEXT.md
    └── [working-folder]/
```

## Routing

| Task | Go to | Read | Do NOT load |
|---|---|---|---|
| [Task] | `[area]/` | `[area]/CONTEXT.md` | [Excluded files or sections and why; or None] |

## Shared conventions

[Brief locally owned rules or links to canonical guidance.]
````

Include only actual responsibilities and useful exclusions. Add `setup`, `status`, or skill routes only when used.

## Workspace context

Use for a responsibility, client, or mode of work without separate stages. Keep short local guidance inline and omit unused sections.

````markdown
# [Workspace]

[Purpose, audience, scope, and source material eligible for this use.]

## Tasks

| Task | Inputs to read | Do NOT load | Process or trigger | Output and location |
|---|---|---|---|---|
| [Task] | [Files and sections] | [Exclusions and reason; or None] | [How it proceeds] | [Artifact or code location] |

## Local guidance

[Voice, quality, or code conventions owned here, or links to their owner.]

## Review

[Acceptance criteria; evidence and input coverage checks where relevant; reviewer and decision, or None and why. Identify draft or reviewed status.]
````

## Decision brief (optional)

Use when a planning decision needs a durable handoff. Reuse an existing record rather than requiring an extra document or approval pause for settled work.

````markdown
# [Decision or task]

- Outcome and audience: [What should change and for whom]
- Evidence and limits: [Known facts with source pointers; constraints]
- Selected approach and rationale: [Choice and why]
- Unresolved questions: [What remains unknown]
- First output and destination: [One concrete deliverable]
- Acceptance and review: [Criteria and reviewer, if needed]
````

## Pipeline overview

Use instead of the simple workspace context when sequential handoffs need separate contracts. Add only needed stages; preserve established artifact locations. Human checks summarize the corresponding contract.

````markdown
# [Workspace]

[Purpose.]

## Pipeline

| Stage and contract | Command or trigger | Output artifact | Human check |
|---|---|---|---|
| [Stage 1](stages/01-[name]/CONTEXT.md) | [Command or request] | [Artifact and location] | [Review decision, or None and why] |
| [Stage 2](stages/02-[name]/CONTEXT.md) | [Command or request] | [Artifact and location] | [Review decision, or None and why] |

## Shared resources

| Resource | Location | Contains |
|---|---|---|
| [Reference or skill] | [Entry path and relevant section] | [What it provides] |
````

## Stage contract

Use for each actual stage's `CONTEXT.md`. Keep steps concrete enough to produce a reviewable artifact. A short local rule can stay in its relevant section.

````markdown
# [Stage]

[What this stage does.]

## Inputs

| Source | File/Location | Section/Scope | Do NOT load | Why |
|---|---|---|---|---|
| Task input or previous stage | [Artifact location] | Full file | None | Material to transform |
| Reference | `references/example.md` | [Relevant section] | [Unneeded sections] | [Applicable guidance] |

## Process

1. Read the declared inputs; report any coverage gaps
2. [Concrete transformation or drafting step]
3. [Apply the checks and handoff below]

## Checkpoints

<!-- For no human review, replace the table with None and why. -->

| After Step | Agent Presents | Human Decides |
|---|---|---|
| [Step number] | [Artifact or options] | [Reviewer, criteria, and decision] |

## Audit

<!-- Omit if inapplicable. Revise failed work before handing it on. -->

| Check | Pass Condition |
|---|---|
| [Quality or source-fidelity check] | [Observable acceptance criterion] |

## Outputs

| Artifact | Location | Format |
|---|---|---|
| [Name] | [Canonical location] | [Format and draft/review status] |
````

## Questionnaire

Use only for unresolved persistent configuration. Follow [questionnaire design](conventions.md#pattern-8-questionnaire-design); configure known values directly and collect per-run inputs at task entry.

````markdown
# Onboarding Questionnaire

Ask the remaining questions in one pass. Apply answers and derived values to the mapped target files, then check that those files contain no unresolved configuration. Mapping declarations and illustrative examples are not replacement targets.

### Q1: [Question]
- Placeholder: `{{PLACEHOLDER_NAME}}`
- Files: `path/to/target.md`
- Type: free text
- Default: [Value or example]
- Derived values: [Only values justified by this answer]

### Q2: [Optional feature]
- Type: yes/no
- If NO: [Omit the corresponding unused template section or stage]
- If YES: [Configure it]

## After onboarding

[What was configured and where to start.]
````

## Placeholder syntax

Use descriptive `{{SCREAMING_SNAKE_CASE}}` strings for unresolved configuration. Map each to questions or derived values and target files. Replace all mapped occurrences, then ask only for still-missing values. Entry routes must work before setup: keep configuration placeholders out of `AGENTS.md` and workspace routing structure. Stage Inputs values may contain them.

Conditional blocks wrap complete sections: a heading and its content up to the next heading of equal or higher level. Removing an inline phrase or list item can break Markdown.

```markdown
{{?VIDEO_PRODUCTION}}

## Video settings

- Resolution: {{VIDEO_RESOLUTION}}
- Frame rate: {{VIDEO_FRAME_RATE}}

{{/VIDEO_PRODUCTION}}
```

Use readable, related names such as `{{PRIMARY_COLOR}}`, `{{SECONDARY_COLOR}}`, and `{{VOICE_DESCRIPTION}}`. Mapping declarations document the placeholders; they are not themselves unresolved target values. Configured workspaces need no placeholder machinery.
