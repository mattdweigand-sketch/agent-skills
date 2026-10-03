# ICM Conventions

Core specification extracted from Jake Van Clief's user-supplied Interpretable-Context-Methodology-main snapshot on 2026-10-01. Entry files use the requested `AGENTS.md` adaptation. Workspace overviews and explicit human-check declarations incorporate the author walkthroughs. The supplied lessons, preserved on 2026-10-02, add task-sized workspaces, conditional pipeline patterns, and focused maintenance and repair. Original repository examples and bundled production tools are omitted; the supplied lessons and examples are retained through the [example index](examples.md).

---

## Workspace Shape and Routing Layers

Start with one real task and the smallest useful workspace. A workspace groups a responsibility, client, or mode of work; a stage performs one step in a sequential workflow. A collection can route directly from its `AGENTS.md` to each workspace's `CONTEXT.md`. One simple workspace can use `AGENTS.md` and local context without a `stages/` tree or an extra collection router.

The supplied routing lesson explicitly describes map, rooms, and tools (entry, workspace context, skills/tools) as a teaching model distinct from the five-layer numbering below. Use the expanded view for workflows that need stage contracts and separate references. These are routing roles, not a requirement to create five levels of folders. Select patterns only where they apply; retain established source-code and artifact locations.

Agents read down the layers. They stop as soon as they have what they need.

```
Layer 0: AGENTS.md           -> "Where am I?"            (entry instructions)
Layer 1: CONTEXT.md          -> "Where do I go?"          (read for the workspace)
Layer 2: Stage CONTEXT.md    -> "What do I do?"            (when stages are needed)
Layer 3: Reference material  -> "What rules apply?"        (loaded selectively, varies)
Layer 4: Working artifacts   -> "What am I working with?"  (loaded selectively, varies)
```

**Layer 0 -- AGENTS.md** is the project or workspace entry file. Use a harness that loads it automatically, or provide it explicitly as entry instructions. It contains the purpose, folder map, naming conventions, and task routes. Add nested entry files only when the environment and scope require them.

**Layer 1 -- Workspace CONTEXT.md** describes its purpose, task routes, scoped inputs, process, outputs, and quality expectations. Concise guidance owned only here can remain inline. A staged workspace uses a pipeline table with each stage and contract route, command or trigger, output artifact and location, and human check. Shared-resource routes follow as needed.

**Layer 2 -- Stage CONTEXT.md files**, where needed, contain the scope definition, what-to-load tables, and step-by-step process. Their Inputs tables scope the references and working artifacts for that stage. A simple workspace can express its task directly without this extra layer.

**Layer 3 -- Reference material** is reusable context: design systems, voice rules, build conventions, style guides, and domain skills. Extract guidance here when it becomes long, shared, or duplicated. It persists across runs and is updated deliberately as requirements change. It can live in stage `references/`, workspace configuration, `shared/`, or skill folders. Larger collections can have their own routing files.

**Layer 4 -- Working artifacts** are the per-run context: previous stage outputs, supplied source material, and other task-specific files. Use explicit canonical locations such as `drafts/`, `deliverables/`, existing code paths, or stage `output/` folders.

The distinction between Layers 3 and 4 matters because they require different things from the model. Layer 3 material needs to be internalized as constraints and patterns -- write like this, use these colors, follow these conventions. Layer 4 material needs to be processed as input -- transform this research into a script, convert this script into a specification. Layer 3 is the factory. Layer 4 is the product.

A rendering agent might only need Layers 0 through 2. A script-writing agent reads down to Layer 4 to access both voice rules (Layer 3) and source material (Layer 4). No agent reads everything.

Map each task to the relevant files and sections. Verify that the routed guidance was actually read; a `CONTEXT.md` filename does not establish that. Naming a skill in a routing table does not install or activate it. Follow the environment's loading rules and verify availability. Client or workspace folders organize context; name permitted sources and inspect their use. Access isolation depends on tool permissions and the execution environment.

Source eligibility depends on the task's audience and intended use as well as access. Internal notes may support a private action list while a public post needs material cleared for that use. Use existing user authorization; resolve unclear sharing scope before including restricted material. A folder name such as `approved-material/` does not itself establish permission.

Run one representative task before adding more structure, within the authorized scope. Use the [representative-task and repair check](validation.md#representative-task-and-repair) to evaluate changes. If execution is unavailable, label the navigation check as a static trace and leave task behavior unverified.

---

## Pattern 1: Stage Contracts

Every stage CONTEXT.md has the following execution contract. Inputs, Process, and Outputs correspond to Input, Do, and Output in the walkthrough. Checkpoints declares the Human check separately under Pattern 11; Audit is agent-side verification under Pattern 12:

```markdown
## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| ... | ... | ... | ... |

## Process

1. Step one
2. Step two
3. Step three

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| ... | ... | ... |
```

Every stage uses these three execution sections plus an explicit Checkpoints declaration. Keep the contract readable by humans and precise enough for an agent to follow.

---

## Pattern 2: Stage Handoffs via Output Folders

For file-based pipelines, a stage `output/` subfolder is the default handoff location. The next stage reads the declared artifact there. A simple workspace can use its existing draft or deliverable folders; code stays in its established source paths. Preserve deliberate external handoffs and document their producer, consumer, location, and review point instead of inventing a duplicate file copy.

The convention:
- Stage N produces: `stages/0N-name/output/artifact-name.md`
- Stage N+1's CONTEXT.md says: "Read `../0N-name/output/artifact-name.md` as your input"

This is the handoff. A human can open the output file, edit it, and the next stage picks up the edited version. No state management. No orchestration layer. Just files in predictable places.

Distinguish source material, working drafts, and reviewed outputs through clear locations, filenames, or existing status metadata; separate folders are optional. Preserve source uncertainty and approval status through each transformation. A suggestion or unconfirmed date must not become an approved commitment without supporting evidence. File presence or a `final` filename alone does not establish review.

File naming in output folders: `[topic-slug]-[stage-artifact].md`
- Example: `hello-world-script.md`, `hello-world-spec.md`

---

## Pattern 3: One-Way Cross-References

Every folder points outward to what it needs. No folder points back.

If Stage 03 references Stage 02's component registry, Stage 02 does NOT reference anything in Stage 03. If the brand-vault is referenced by multiple stages, the brand-vault does NOT reference any stage.

This prevents reference growth from going N-squared as the system scales. When adding a new reference, check: "Does the target file already reference my folder?" If yes, restructure.

---

## Pattern 4: Selective Section Routing

CONTEXT.md Inputs tables do not just say "read voice-rules.md." They say "read the Voice Rules section of voice-rules.md."

This keeps token cost low. A 150-line file might have only 60 lines of actionable rules for a specific stage. The other 90 lines of strategic rationale stay unloaded.

Format in CONTEXT.md Inputs tables:

```
| File | Section to Load | Why |
|------|----------------|-----|
| voice-rules.md | "Voice Rules" through "What the Voice Is NOT" | Tone guidance |
| identity.md | "One-Sentence Brand" and "Audience" sections | Audience context |
```

When a full file is needed, write "Full file" in the Section/Scope column.

Compare the required input scope with what was actually read. Report unreadable, omitted, or partially read files and sections, with the resulting limits on the output. A partial review must not appear complete. For larger inputs, use manageable groups and retain the same coverage check; file count alone does not establish that the material fits.

For extracted decisions, commitments, or consequential factual claims, keep a source identifier plus a short supporting passage or precise location beside each item, or in its review notes when the final format requires it. Separate decisions, suggestions, actions, and contradictions where the task calls for that distinction. Scope this evidence requirement to source-derived work; it does not require citations for every line of an unrelated creative or code artifact.

---

## Pattern 5: Canonical Sources

Every piece of information has ONE home. Other files point there. They do not duplicate it.

If you need to update a rule, you update it in one place. Every other file has a pointer. If you find the same information in two files, one of them should be replaced with a reference to the other.

When a fact or decision changes, update its canonical source. Date information whose currency matters, remove or clearly retire superseded active directions, and retain the reason for consequential decisions in the existing context or decision record. Preserve historical source captures as evidence and route current tasks to the current guidance; a new tracking system is unnecessary.

Smell test: search the repo for a specific phrase. If it appears in more than one file and both instances are meant to be authoritative, one needs to become a pointer.

---

## Pattern 6: Concise Local Context

CONTEXT.md files answer three questions:
1. What is this folder?
2. What do I load?
3. What is the process?

They can also contain short, locally owned guidance about voice, audience, conventions, and what good work looks like. Aim for a page of useful guidance. Extract material into a canonical reference when it becomes long, shared, or duplicated, and route to the relevant section. Do not create a separate file for every short rule. Stage contracts retain their execution sections; a brief local rule does not make them invalid.

---

## Pattern 7: Tool Prerequisites

Some stages require external tools (Node.js, LibreOffice, ffmpeg, etc.). Setup guides for these tools live in the `references/` folder of the stage that uses them (e.g., `stages/03-build/references/remotion-setup.md`).

Setup guides are written for someone who has never installed the tool: what it is (one sentence), installation steps, how to verify it works, and how the workspace uses it.

If a tool is needed by multiple stages, it can live in `shared/` instead. The `setup` onboarding process should check which tools are needed based on the user's answers and point them to the right setup guide.

Note: When a workspace bundles skills (Pattern 9), many tools that would have needed separate prerequisites (scripts, libraries, utilities) come bundled inside the skill folder. Only tools that require system-level installation (Node.js, Python, LibreOffice) still need setup guides.

---

## Trigger Keywords

Add these triggers only when the workspace needs onboarding or pipeline status. A simple task workspace need not define either.

**`setup`** -- For a reusable workspace with unresolved system-level choices, reads `setup/questionnaire.md`, collects missing answers, replaces mapped placeholders, and verifies the configuration. Use known values directly; do not create a questionnaire just to restate them.

**`status`** -- Shows the declared handoffs and completion checks. For a file-based staged pipeline, inspect its output locations and summarize them, for example:

```
Pipeline Status: [workspace-name]

  [01-stage-name]  ------>  [02-stage-name]  ------>  [03-stage-name]
     COMPLETE                  PENDING                  PENDING
  (artifact.md)              (empty)                  (empty)
```

For each stage, list the declared output artifact and whether it exists. File presence alone does not prove completion or review; use the stage's quality and human-check requirements before reporting COMPLETE. For other handoff locations, inspect the declared location rather than assuming an `output/` folder.

Workspaces can define additional trigger keywords in their own AGENTS.md.

---

## Naming Conventions

- New workflow folders and files: `lowercase-with-hyphens`; preserve required entry filenames and established codebase conventions
- Stage folders, when sequence matters: zero-padded numbers prefix: `01-`, `02-`, `03-`
- Placeholders: `{{SCREAMING_SNAKE_CASE}}`
- Output artifacts: `[topic-slug]-[artifact-type].md`
- Avoid spaces in new workflow file or folder names; do not rename existing paths just to fit an example

---

## Pattern 8: Questionnaire Design

Use a questionnaire only when a reusable workspace has unresolved system-level choices. It configures persistent defaults, not a specific run. Where needed, follow these rules:

1. **Flat structure.** No category groupings. Just a numbered list of questions.
2. **All at once.** Every question appears in one pass. The user should be able to answer everything in a single message.
3. **System-level only.** Questions configure things that stay the same across runs: identity, brand, design, tool preferences, default workflow. Per-run details (project name, topic, audience, scope) are collected conversationally at the start of each pipeline run by the entry stage.
4. **Derive, do not ask.** If a field can be inferred from another answer, the agent fills it in. List derived fields under the question they depend on. Do not add a separate question.
5. **Sensible defaults.** Every question should have a default or example so the user can skip what they do not care about.
6. **Persist the answers.** Reuse configured values on later runs. Revisit them only when requirements change or the user requests an update.

The questionnaire template at [questionnaire template](templates.md#questionnaire) encodes these rules.

---

## Pattern 9: Bundled Skills

Workspaces can bundle domain skills (APIs, best practices, code examples) when portability requires a local copy. Use the environment's supported discovery or explicit-read mechanism; a generic `skills/` folder is not a guarantee of discovery, installation, or activation. Existing available skills can be used without copying them.

```
workspace/
├── skills/
│   ├── [skill-name]/          (copied from a local skill installation or cloned from GitHub)
│   │   ├── SKILL.md           (skill entry point)
│   │   ├── rules/             (detailed rule files, if any)
│   │   └── scripts/           (utility scripts, if any)
│   └── [another-skill]/
│       └── SKILL.md
```

**Discovery:** When the task needs domain guidance, identify relevant skills by:
1. Checking the current environment's configured skill directories for locally installed skills
2. Searching GitHub for skill repos matching the workspace domain (e.g., "remotion skill", "pptx skill")
3. Presenting candidates to the user for selection

**Bundling:** When a local copy is needed, copy or clone the selected skill into the supported location and preserve its dependencies and notices. Verify its loading path and prerequisites before calling the workspace ready to run.

**Referencing:** Stage CONTEXT.md files reference skills in their Inputs table:

```
| Skill | `../../skills/[name]/SKILL.md` | Index, then load rules as needed | [What it provides] |
```

Skills replace custom reference docs when an official skill covers the same ground. Keep workspace-specific files (design systems, brand config, build conventions) alongside skills, not inside them.

**When NOT to bundle:** Do not bundle skills that are purely about configuring or extending the agent platform (e.g., skill-creator, mcp-builder). Only bundle skills that provide domain knowledge the workspace's agents need at runtime.

---

## Pattern 10: Specs Are Contracts

Specification stages define the intended outcome and acceptance criteria for their consumer. In the original video-production workflow, the spec defines WHAT and WHEN, leaving HOW to the build stage within the design system's quality requirements. Other domains can require architecture or implementation constraints in the spec.

For a video-production workflow, a spec can contain:
- **Beat map** with approximate durations, narration, and mood
- **Visual philosophy** describing what a muted viewer should understand
- **Key moments** that MUST land, and why each matters
- **Audio sync points** mapping narration words to visual events
- **Color flow** with per-scene dominant color and mood

In that workflow, frame numbers, component names, pixel positions, spring configs, and prop definitions belong to the build stage. Use domain-appropriate specification criteria elsewhere; these video examples are not universal requirements for software architecture or other workspaces.

---

## Pattern 11: Checkpoints

Creative stages should include at least one checkpoint where the agent pauses and the human steers. The agent completes a full unit of work, presents options or a draft, and the human redirects before the next unit begins. Checkpoints go between process steps, not within them.

Not every stage needs a review pause. Linear stages (extract, render, validate) can declare "None" with a short reason in Checkpoints. Creative stages (writing, design, ideation) should include at least one review point. State who reviews the artifact, what they check, and the decision before work continues.

The Checkpoints section in a stage CONTEXT.md is a table:

```
| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| [step #] | [what to show] | [what to choose] |
```

---

## Pattern 12: Stage Audits

Creative and build stages should include an Audit section: a checklist the agent runs after completing the process but before writing to output/. Audits catch quality issues before they propagate downstream. Each check should be specific enough that pass/fail is unambiguous.

Not every stage needs an audit. Data extraction or file conversion stages may not benefit. Creative and build stages almost always do.

The Audit section in a stage CONTEXT.md is a table:

```
| Check | Pass Condition |
|-------|---------------|
| [Check name] | [What "passing" looks like] |
```

If any check fails, the agent revises before saving to output/.

---

## Pattern 13: Value Validation

Content-producing stages should define what types of value their output can deliver. Before the main creative work begins (ideally at a checkpoint), the agent and human should agree on which value types this specific piece will hit. This prevents "interesting but doesn't DO anything" output.

Value types are workspace-specific. A content workspace might use NOVEL, USABLE, QUESTION-GENERATING, INTERESTING. A course workspace might use TEACHES, PRACTICES, CHALLENGES. The framework is defined once in a reference file and used at every checkpoint.

---

## Pattern 14: Docs Over Outputs

Canonical guidance (local context, design systems, build conventions, skill rules) defines how to build. Prior outputs do not automatically become templates or authority. Explicitly selected writing samples and approved examples can guide or evaluate a task; identify their role and keep their facts scoped to their original context. Update canonical guidance deliberately when a tested example reveals a useful improvement.

---

## Pattern 15: Shared Constants

Where code reuses configurable values (colors, fonts, timing, layout), keep them in shared files that relevant outputs import from. Configure known values directly, or populate them through onboarding when needed. Change a shared value once to update its consumers.

This is Pattern 5 (Canonical Sources) applied to code values. Without shared constants, the same hex code or font name is hardcoded in every output file. Changing the brand color means a find-and-replace across every file ever built.

For non-code workspaces (content writing, course design), this pattern does not apply. Shared values live in reference docs instead.

---

## Quality Guardrails

- CONTEXT.md files: aim for a page; review files over 80 lines for avoidable detail or repetition
- Maintained workspace reference files: review files over 200 lines for useful section routing or splitting; preserved sources and template collections are not subject to automatic splitting
- Use plain English. Avoid jargon. If a term needs explaining, it is too specialized.
- For newly authored workflow guidance, use plain punctuation; preserve source text and existing codebase conventions
- Required empty folders that must persist in Git get a `.gitkeep` file
- Every markdown file should be readable by someone who understands markdown and git basics but does not have a deep engineering background

## Source record

Source: the user-supplied `Interpretable-Context-Methodology-main` snapshot, checked on 2026-10-01. No upstream commit ID was recorded. The source archive and full video captions are not bundled. These fingerprints identify the local source material, not a verified upstream release.

| Source paths, relative to that snapshot | SHA-256 group fingerprint |
|---|---|
| `_core/CONVENTIONS.md` | `14e97ef3f0bb838c17ae8a7cbb889fab39f0273674c8e2c05b414da717656c00` |
| `_core/templates/*.md and _core/placeholder-syntax.md` | `97d84535d07cf9023241b1026b5edd8261b24d22ee0a27d745917119f65ed16a` |
| `workspaces/workspace-builder/stages/*/CONTEXT.md` | `3eee615cbb618c40ef065e6edc705d9d313baf452ccf00ddb4c9083745c04a1c` |

Each fingerprint hashes a UTF-8 JSON object mapping relative POSIX file paths to their whole-file SHA-256 hashes, with sorted keys, no spaces, and no trailing newline.

Walkthrough evidence is paraphrased from English auto-generated captions retrieved on 2026-10-01:

- [Folder architecture, 1:11](https://www.youtube.com/watch?v=n1qE6NU7K_4&t=71s): entry map; [2:17](https://www.youtube.com/watch?v=n1qE6NU7K_4&t=137s): Input, Do, Output, Human check; [7:51](https://www.youtube.com/watch?v=n1qE6NU7K_4&t=471s): fresh-chat navigation check.
- [Reviewable stages, 2:34](https://www.youtube.com/watch?v=EhWlGingCl0&t=154s): workspace pipeline table; [4:11](https://www.youtube.com/watch?v=EhWlGingCl0&t=251s): review before downstream production.

Supplementary sources supplied by the user and stored on 2026-10-02:

| Source | Capture | SHA-256 |
|---|---|---|
| [3.2 Customizing for Your Use Case](sources/customizing-for-your-use-case.md) | Attachment bytes unchanged, including all three example trees and routing tables | `ab3f740795797e6972bd75e875b1d0738d393b62b1f003fb57d17433cbb6718e` |
| [The three layer routing system](sources/three-layer-routing-system.md) | Attachment bytes unchanged, including the three-file starter and research qualifications | `ebf671c85c605ca23ca703b69612fa087a3bb95b93c65298eb1ff7e1e37c6509` |
| [3.3 Common Mistakes and How to Fix Them](sources/common-mistakes-and-how-to-fix-them.md) | Full lesson captured from the user's inline Markdown, including seven mistakes, the fictional repair, and links | `4cf525e376904d55f82b4b5d773398cf72c29be5a2f02127357604df5e468bd5` |

These fingerprints identify local captures, not verified live course revisions. The inline lesson has no separate original attachment for a byte comparison. Research-paper descriptions and cross-tool evidence limits in the routing lesson remain attributed to that supplied text; the paper was not independently checked for this update. Original `CLAUDE.md` wording and sample rules remain source evidence. Use `AGENTS.md` here, and adopt example-specific permissions or output formats only when they fit the user's actual requirements.

The written Foundation lessons 4.1-4.5 were also reviewed in the browser on 2026-10-02. See the [review notes and source links](sources/foundation-lessons-review.md) for the adopted refinements and optional decision-brief example. Those notes are an authored summary, not a verbatim capture. The videos were not reviewed and the Foundation Practice download required login, so its files remain uninspected.

Deliberate adaptations: `AGENTS.md` entry files, platform-neutral skill discovery, explicit file-role and human-review declarations, and a representative task run or clearly labeled static trace. The 2026-10-02 updates adopt task-sized workspaces, conditional pipeline scaffolding, concise inline context, canonical maintenance, source coverage and evidence, use-specific source eligibility, preservation of uncertainty, and comparable repair runs. These supersede the earlier blanket pipeline and context-purity requirements in this maintained guidance; the supplied sources retain their differing formulations. Safe-migration checks are local safeguards restored from `mattdweigand-sketch/agent-skills` commit `ae2ae17`, not requirements attributed to the videos. Other demonstrated variants do not automatically override these conventions.

## Upstream notices

The supplied source names Model Workspace Protocol Contributors; the earlier skill package names Jake Van Clief. Both notices are retained here with their common MIT terms.

```text
MIT License

Copyright (c) 2026 Model Workspace Protocol Contributors
Copyright (c) 2026 Jake Van Clief

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
