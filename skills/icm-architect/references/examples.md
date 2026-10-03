# ICM Examples

These are compact authored adaptations, not verbatim course excerpts or recorded model results. [Lesson notes](sources/lesson-notes.md) provide attribution and links. Use only the structure needed for the next deliverable; the paths below are illustrative, not bundled fixtures.

## Workspace customization

| Work | Possible responsibilities | First useful task and destination |
|---|---|---|
| Content creation | Writing, production, distribution | Read audience guidance and one source; draft a script in `writing/drafts/` |
| Consulting | Client work, reusable templates, internal business development | Use one client's notes and an applicable template; save a follow-up in `clients/river/drafts/` |
| Software | Planning, existing code, documentation, operations | Read the relevant spec and code conventions; implement in existing source paths |

These responsibilities need separate folders only when their context or handoffs differ. For one client follow-up, a complete starting structure can be:

```text
client-follow-up/
├── AGENTS.md
├── CONTEXT.md
├── inputs/meeting.md
└── drafts/
```

`AGENTS.md` maps the task to local context. `CONTEXT.md` states the audience, eligible sources, brief style guidance, output, and review criteria. Add a separate reference only when needed.

## Read and skip routing

An authored workspace route could be:

| Task | Read | Do NOT load | Write |
|---|---|---|---|
| River follow-up | `clients/river/CONTEXT.md`; `clients/river/inputs/meeting.md` | Other clients' notes; unrelated outreach drafts | `clients/river/drafts/follow-up.md` |
| API documentation | `docs/CONTEXT.md`; relevant API source and tests | Unrelated application screens | `docs/api/` |

For the operational boundary behind these routes, see [loading and access](conventions.md#loading-and-access). Use the [entry and context templates](templates.md#workspace-entry) when building a real workspace.

## Repair and source fidelity

Fictional input: `planning-note-01.md`, section Next steps, says: "Iris will prepare a demo. The delivery date is still open."

| Item | Type | Owner | Due date | Evidence |
|---|---|---|---|---|
| Prepare the demo | Action | Iris | Unconfirmed | `planning-note-01.md`, Next steps, the two sentences above |

If a draft promises delivery Tuesday, the date is unsupported. Correct the source interpretation and rerun the same request using the [repair method](validation.md#representative-task-and-repair). Check that the date remains unconfirmed, then try another relevant example before treating the change as a reusable rule.

If a required second note was unreadable, state that limitation; this result cannot establish agreement across both notes. Use an existing Questions section for unresolved details when the output format calls for one, without imposing that format on every task.

## Planning handoff

Use the [optional decision brief](templates.md#decision-brief-optional) when another step needs the chosen approach and its reasons. An existing brief carrying those facts is sufficient.
