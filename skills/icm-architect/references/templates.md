# ICM Templates

Adapted from the supplied ICM core templates, walkthroughs, and customization lesson, using `AGENTS.md`. Start with the workspace entry and local context. Use the pipeline overview, stage contract, and questionnaire only when needed. The placeholder names below are authoring notation; finish them before delivering a configured workspace. See the [example index](examples.md) for three complete source examples.

## Workspace entry

Use for `AGENTS.md`: the project or workspace purpose, actual folder map, and task routes. For a collection, route to each workspace's local context. For one workspace, route to its own `CONTEXT.md`. Add rows and folders only for existing responsibilities.

````markdown
# [Project or Workspace Name]

[One sentence: what this project or workspace does and for whom.]

## Folder Map

```
[project-name]/
├── AGENTS.md          (you are here)
└── [area]/            ([responsibility])
    ├── CONTEXT.md     (local guidance and task routes)
    └── [working-folder]/
```

## Routing

| Task | Go to | Read |
|------|-------|------|
| [Task] | `[area]/` | `[area]/CONTEXT.md` |

## Shared conventions

[Only conventions or boundaries shared across these tasks. Link existing canonical guidance.]
````

For a single workspace, put `CONTEXT.md` and working folders beside `AGENTS.md` rather than adding an unnecessary `[area]/` folder. Add `setup`, `status`, and skill routes only if the workspace uses them; identify required skills and verify loading separately from listing their names.

## Workspace context

Use for a responsibility, client, or mode of work without a staged pipeline. Keep short local guidance here; extract it when it becomes long, shared, or duplicated. Adapt the sections to the task instead of filling empty tables.

````markdown
# [Workspace Name]

[Purpose, audience or client, and scope.]

## Tasks

| Task | Inputs to read | Process or trigger | Output and location |
|------|----------------|--------------------|---------------------|
| [Task] | [Permitted files and sections] | [How the task proceeds] | [Artifact or code location] |

## Local guidance

[Brief voice, quality, or code conventions owned here, or links to canonical references.]

## Review

[Relevant quality check; who reviews what before a handoff, or None and why.]
````

## Pipeline overview

Use instead of the simple workspace-context template when actual sequential handoffs need separate stage contracts. Preserve established artifact locations. Number stages where order matters; include only needed stages and shared-resource rows.

````markdown
# [Workspace Name]

[One sentence: what this workspace covers.]

## Pipeline

<!-- Use real commands or natural-language triggers. Name the artifact and location.
     The human check summarizes the corresponding stage's Checkpoints, without adding a gate. -->

| Stage and contract | Command or trigger | Output artifact | Human check |
|---|---|---|---|
| [Stage 1](stages/01-[name]/CONTEXT.md) | [Command or request] | [Artifact and location] | [What the reviewer checks before continuing, or None and why] |
| [Stage 2](stages/02-[name]/CONTEXT.md) | [Command or request] | [Artifact and location] | [What the reviewer checks before continuing, or None and why] |
| [Stage 3](stages/03-[name]/CONTEXT.md) | [Command or request] | [Artifact and location] | [What the reviewer checks before continuing, or None and why] |

## Shared Resources

| Resource | Location | Contains |
|----------|----------|----------|
| [Context folder] | `[folder]/CONTEXT.md` | [What it routes to] |
| [Shared files] | `shared/` | [What cross-stage files live here] |
| [Skill name] | `skills/[name]/SKILL.md` | [What domain knowledge this skill provides] |
````

## Stage contract

Use for each stage's `CONTEXT.md` when the pipeline needs separate stages. Inputs, Process, Outputs, and Checkpoints express the video's Input, Do, Output, and Human check. Audit is separate agent-side verification. A short local rule may stay in the relevant section; it need not become a reference file.

````markdown
# [Stage Name]

[One sentence: what this stage does.]

## Inputs

<!-- List every file the agent needs. Be specific about which sections. -->

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Task input or previous stage | [Actual artifact or source location] | Full file | The artifact to work from |
| Reference | `references/example.md` | "Relevant Section" | What it provides |

## Process

<!-- Numbered steps. Each step is one concrete action. Be specific enough that
     two different agents following these steps would produce structurally similar
     outputs.

     Too vague: "Write the script"
     Good: "Write the full script in one pass, then audit against the voice
            hard constraints and value brief"

     Too vague: "Generate ideas"
     Good: "Propose 3-5 concept angles, each as a single sentence. Tag each
            with its value type and format." -->

1. Read the declared task input or previous-stage artifact
2. [Step two]
3. [Step three]
4. Save to the declared output location after applicable checks

## Checkpoints

<!-- Points where the agent pauses for human input before continuing.
     Not every stage needs checkpoints. Linear stages (extract, render, validate)
     often run straight through. Creative stages (writing, design, ideation)
     benefit from at least one.

     Format: after which process step, what the agent presents, what the human decides.
     If the stage runs straight through, replace the table with "None" and a short reason. Do not add an approval pause. -->

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| [step #] | [artifact or options for review] | [who reviews, what they check, and the decision before continuing] |

## Audit

<!-- Quality checks before the output is considered done. The agent runs these
     after completing the process steps. If any check fails, revise before saving.

     Not every stage needs an audit. Data extraction or file conversion stages
     may not benefit. Creative and build stages almost always do.
     Delete this section if no audit applies. -->

| Check | Pass Condition |
|-------|---------------|
| [Check name] | [What "passing" looks like] |

## Outputs

<!-- What this stage produces and where it goes. -->

| Artifact | Location | Format |
|----------|----------|--------|
| [Name] | [Canonical location, e.g. `output/[slug]-[type].md`] | [Description of the format] |

<!-- Target: keep this file under 80 lines. -->
````

## Questionnaire

Use only for unresolved system-level choices in a reusable workspace. Configure known values directly. Omit this file, the setup trigger, and placeholder machinery when they add no value.

````markdown
# Onboarding Questionnaire

<!-- Agent instructions: Read this file when the user types "setup". Ask ALL questions
     in a single conversational pass. The user should be able to answer everything in one
     message. Collect answers. Replace placeholders across the specified files. After all
     replacements, verify no unresolved values remain in the configured target files.
     Exclude questionnaire mappings and preserved source examples. -->

<!-- Questionnaire design rules:
     1. FLAT STRUCTURE: No category groupings. Just a numbered list of questions.
     2. ALL AT ONCE: Every question appears in one pass. The user answers in one message.
     3. SYSTEM-LEVEL ONLY: Questions configure the production system, not a specific run.
        Per-run details (project name, topic, audience) are collected conversationally
        at the start of each pipeline run by the entry stage.
     4. DERIVE, DON'T ASK: If a field can be derived from other answers, the agent fills
        it in without asking. List derived fields under the question they depend on.
     5. SENSIBLE DEFAULTS: Every question should have a default or example so the user
        can skip what they don't care about.
     6. PERSIST ANSWERS: Reuse configured values on routine runs. Revisit them when
        requirements change or the user requests an update.
     7. EXAMPLES OVER DESCRIPTIONS: For voice/style questions, ask for concrete examples
        (sentences that sound right, sentences that sound wrong, specific error patterns)
        rather than abstract descriptions. Examples are pattern-matchable. Descriptions
        require interpretation and produce weaker constraints. -->

### Q1: [Question text]
- Placeholder: `{{PLACEHOLDER_NAME}}`
- Files: `path/to/file1.md`, `path/to/file2.md`
- Type: free text
- Default: [Default value if user wants to skip]

### Q2: [Question text]
- Placeholder: `{{PLACEHOLDER_NAME}}`
- Files: `path/to/file.md`
- Type: selection
- Options: Option A, Option B, Option C

### Q3: [Question about an optional feature -- yes/no]
- Type: yes/no
- If NO: Remove `stages/0N-name/` entirely
- If YES: Keep it

---

## After Onboarding

[Tell the user what was configured and where to start.]

After replacements, check configured target files for unresolved values. Exclude mapping declarations and preserved sources; ask only for information still needed to configure the workspace.
````

## Placeholder syntax

For reusable templates that need onboarding, placeholder variables mark unresolved configuration. The onboarding agent replaces these with real content when a user runs `setup`. Configured workspaces do not need this machinery.

---

## Basic Syntax

Placeholders use double braces and SCREAMING_SNAKE_CASE:

```
{{BRAND_NAME}}
{{TARGET_AUDIENCE}}
{{PRIMARY_COLOR}}
```

These are literal strings in markdown files. They are not code variables. The onboarding agent finds them and replaces them with the user's answers through string substitution.

---

## Replacement Rules

1. The onboarding agent reads `setup/questionnaire.md` for the list of questions
2. Each question maps to one or more placeholders
3. Each question specifies which files contain its placeholder
4. The agent asks the questions conversationally, collecting answers
5. The agent replaces every instance of each placeholder with the corresponding answer
6. After replacements, scan configured target files for unresolved `{{` patterns, excluding mapping declarations and preserved sources
7. If any remain, the agent flags them and asks the user for the missing information
8. Onboarding is complete when the configured target files have no unresolved values

---

## Where Placeholders Can Appear

Placeholders can appear in any markdown file within a workspace:
- Brand vault files (voice-rules.md, identity.md)
- Reference files (hook-system.md, design-system.md, etc.)
- Shared files (platform-specs.md)
- Stage CONTEXT.md files (only in Inputs table values, not in routing structure)

Placeholders should NOT appear in:
- AGENTS.md files (these need to work before onboarding runs)
- Top-level CONTEXT.md routing tables (these need to work before onboarding runs)
- The questionnaire.md itself (the questions are the source, not the target)

---

## Conditional Sections

Conditional sections wrap content that gets removed if the user indicates it is not needed.

Syntax:

```markdown
{{?SECTION_NAME}}

## Section Heading

Content that may or may not be relevant...

{{/SECTION_NAME}}
```

**Rule: Conditional blocks can only wrap entire sections.** A section means a heading and all content below it, up to the next heading of the same or higher level.

Valid:

```markdown
{{?VIDEO_PRODUCTION}}

## Video Production Settings

Resolution, frame rate, and export format for your video pipeline.

- Resolution: 1920x1080
- Frame rate: 30fps
- Export format: MP4

{{/VIDEO_PRODUCTION}}
```

Invalid (do not do this):

```markdown
- Item one
{{?OPTIONAL_ITEM}}
- Item two (optional)
{{/OPTIONAL_ITEM}}
- Item three
```

Invalid (do not do this):

```markdown
The brand voice is {{?FORMAL}}formal and authoritative{{/FORMAL}}
{{?CASUAL}}casual and conversational{{/CASUAL}}.
```

Why this rule exists: removing inline content leaves orphaned list markers, broken sentences, or malformed markdown. Wrapping complete sections means removal always produces clean markdown.

---

## Naming Conventions

Use descriptive names: `{{BRAND_NAME}}` not `{{BN}}`.

Group related placeholders with common prefixes:
- `{{VOICE_DESCRIPTION}}`, `{{VOICE_ADJECTIVES}}`
- `{{PRIMARY_COLOR}}`, `{{SECONDARY_COLOR}}`, `{{ACCENT_COLOR}}`
- `{{CONTENT_PILLAR_1}}`, `{{CONTENT_PILLAR_2}}`

Conditional section names should describe what they wrap:
- `{{?BUILD_STAGE}}` for the build stage section
- `{{?PILLAR_4}}` for the fourth content pillar

---

## Questionnaire Mapping

The `setup/questionnaire.md` file is the bridge between questions and placeholders. Each question entry specifies:

- The question text (what the agent asks the user)
- The placeholder(s) it populates
- The file(s) where those placeholders appear
- The input type (free text, multiple choice, yes/no)
- Optional: follow-up questions for vague answers
- Optional: conditional logic (if answer is X, remove section Y)

See [Questionnaire](#questionnaire) for the format.
