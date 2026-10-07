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

Fictional request: "Draft a client follow-up from the planning notes." The chosen scope is a draft for the account owner to review; a proposed interpretation that the client needs a delivery commitment is still an assumption. Keep the request and chosen scope in existing local context rather than adding another scope file.

Fictional input: `inputs/planning-note-01-v1.md`, section Next steps, says: "Iris will prepare a demo. The delivery date is still open."

| Item | Type | Owner | Due date | Evidence |
|---|---|---|---|---|
| Prepare the demo | Action | Iris | Unconfirmed | `inputs/planning-note-01-v1.md`, Next steps, the two sentences above |

A suitable draft says, "Iris will prepare the demo; the delivery date remains open." Acceptance requires the named action and owner, visible date uncertainty, and a source location in review notes. Reject a promised date without supporting evidence. The account owner should be able to find the selected note and draft, understand what remains open, and decide the next step without the workspace builder's explanation.

If a draft promises delivery Tuesday, the date is unsupported. Correct the source interpretation and rerun the same request using the [repair method](validation.md#representative-task-and-repair). Check that the date remains unconfirmed, then try another relevant example before treating the change as a reusable rule.

If a required second note was unreadable, state that limitation; this result cannot establish agreement across both notes. Use an existing Questions section for unresolved details when the output format calls for one, without imposing that format on every task.

Suppose the account owner reviewed `drafts/follow-up-v1.md` against that note. Identify that exact draft and source version in the existing review record. If `inputs/planning-note-01-v2.md` changes the demo owner to Morgan while leaving the date open, reconsider the owner claim and the draft's readiness. Review of v1 does not establish readiness for a revised draft. Check the selected result in the account owner's actual document or message preview; sending is a separate action requiring applicable authorization.

## Planning handoff

Use the [optional decision brief](templates.md#decision-brief-optional) when another step needs the chosen approach and its reasons. An existing brief carrying those facts is sufficient.

## Roles and stable steps

Fictional weekly client report: an existing export and spreadsheet tool produce totals, one model interprets the changes and drafts commentary, and the account owner reviews the result before any authorized sending. These are separate responsibilities in one task route, not three required agents.

Once the export-to-table rules are stable, a narrow command can accept one export and write one table in the existing artifact location. Compare it with a previously checked manual table, including a relevant missing-field case, before adding the command to the route. Keep interpretation with the model. Independent company research may justify a bounded helper when delegation is authorized and its benefit warrants the coordination cost. For handoff, the account owner should be able to locate the export, selected table, and review decision by following the map without AI assistance. This is an authored example, not a tested workflow.
