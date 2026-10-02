# ICM Templates

Adapted from the supplied ICM core templates, using `AGENTS.md` and the author walkthroughs' explicit file roles. Copy only the relevant template into the target workspace. The placeholder names below are authoring notation; finish them before delivering a configured workspace.

## Workspace entry

Use for `AGENTS.md`: the workspace purpose, folder map, and routes to the right job.

````markdown
# [Workspace Name]

[One sentence: what this workspace does.]

## Folder Map

```
[workspace-name]/
├── AGENTS.md          (you are here)
├── CONTEXT.md         (start here for task routing)
├── setup/             (onboarding questionnaire)
├── skills/            (bundled Claude skills for domain knowledge)
├── [context-folder]/  (shared context files)
├── stages/
│   ├── 01-[name]/     ([brief description])
│   ├── 02-[name]/     ([brief description])
│   └── 03-[name]/     ([brief description])
└── shared/            (cross-stage reference files)
```

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run onboarding questionnaire |
| `status` | Show pipeline completion for all stages |

## Routing

| Task | Go To |
|------|-------|
| [Task type 1] | `stages/01-[name]/CONTEXT.md` |
| [Task type 2] | `stages/02-[name]/CONTEXT.md` |
| [Task type 3] | `stages/03-[name]/CONTEXT.md` |

## What to Load

<!-- Map each task to its minimal file set. Loading more files dilutes quality.
     The context window is working memory, not storage. -->

| Task | Load These | Do NOT Load |
|------|-----------|-------------|
| [Task 1] | [minimal file list] | [what to skip and why] |
| [Task 2] | [minimal file list] | [what to skip and why] |

## Stage Handoffs

Each stage writes its output to its own `output/` folder. The next stage reads from there. If you edit an output file, the next stage picks up your edits.
````

## Workspace routing

Use for the workspace `CONTEXT.md`: the pipeline overview and shared-resource routes.

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

Use for each stage's `CONTEXT.md`. Inputs, Process, Outputs, and Checkpoints express the video's Input, Do, Output, and Human check. Audit is separate agent-side verification.

````markdown
# [Stage Name]

[One sentence: what this stage does.]

## Inputs

<!-- List every file the agent needs. Be specific about which sections. -->

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../0N-prev/output/artifact.md` | Full file | The artifact to work from |
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

1. Read the input artifact from the previous stage
2. [Step two]
3. [Step three]
4. Save to output/

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
| [Name] | `output/[slug]-[type].md` | [Description of the format] |

<!-- Target: keep this file under 80 lines. -->
````

## Questionnaire

````markdown
# Onboarding Questionnaire

<!-- Agent instructions: Read this file when the user types "setup". Ask ALL questions
     in a single conversational pass. The user should be able to answer everything in one
     message. Collect answers. Replace placeholders across the specified files. After all
     replacements, verify no {{PLACEHOLDER}} patterns remain in the workspace. -->

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
     6. ASK ONCE, NEVER AGAIN: After setup, the user should never be asked these questions
        again. The answers are baked into the workspace files permanently.
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

After all replacements, scan the entire workspace for remaining `{{` patterns. If any remain, ask for the missing info.
````

## Placeholder syntax

How the onboarding system works. Workspaces ship with placeholder variables in their markdown files. The onboarding agent replaces these with real content when a user runs `setup`.

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
6. After all replacements, the agent scans the entire workspace for any remaining `{{` patterns
7. If any remain, the agent flags them and asks the user for the missing information
8. Onboarding is complete only when zero placeholders remain

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
