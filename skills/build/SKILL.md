---
name: build
description: "Interview the user to define a useful result, then build it and check the evidence. Use for /build, $build, or requests for an interview-led build workflow. Covers tools, documents, spreadsheets, skills, workflows, and prototypes. Skip ordinary questions, review-only requests, and trivial edits unless explicitly invoked."
---

# Build

Learn what the user needs through a focused interview, build the result, and check that it serves its purpose. A sketch, personal tool, reusable workflow, or finished document can each be a complete result. If the user asks only for a plan or review, deliver that and keep the work read-only.

## Interview before building

First read the relevant conversation and existing work. Separate what the user has already decided from missing information and assumptions. Do not ask them to repeat answers or supply facts you can inspect.

Ask the question whose answer would most change what you build or how you check it. Prefer one focused question at a time. Group up to three closely related questions when that is easier to answer. Use the available question tool when suitable. Wait for the answers before doing work that depends on them. Read-only inspection can continue meanwhile.

Use plain language and concrete examples. Offer a small set of choices with a recommendation when it helps, and allow a different answer. Keep routine technical choices with the agent. If the user is unsure, propose a small example or experiment that can help them decide.

Cover the gaps that matter from the following areas. These are interview topics, not a questionnaire to ask in full.

| Area | What to learn |
|---|---|
| Purpose and use | Who will use this, what they want to accomplish, and where or how they will use it |
| A real example | A typical input or starting situation and the result the user expects |
| Scope and limits | What belongs in this version, what is excluded, what must stay unchanged, and any relevant time, cost, data, or access limits |
| Quality | What would make the result useful or disappointing, with a reference or counterexample when helpful |
| Proof and ownership | What evidence would show success, how it can be checked, and any access or judgment only the user can provide |

Follow up when an answer still permits materially different builds. Turn words such as "simple," "reliable," or "good" into an example, limit, or observable result. Surface contradictions and ask the user to resolve consequential tradeoffs. Do not silently choose on their behalf.

Stop interviewing when the intended result and important boundaries are clear enough to build and check. Scale the interview to the task. If the supplied context already answers the needed questions, summarize it and proceed. If the user asks you to choose, state reasonable assumptions and work within that authority. For exploration, agree on what the first artifact should help them learn instead of inventing finished requirements.

## Turn the answers into a build brief

Before substantial building, give a short brief with the deliverable, scope, constraints, and checks. For each material requirement, connect the expected result to a feasible check, the evidence it will produce, and who will run or judge it. Derive technical checks from the user's examples rather than asking them to design tests.

Distinguish what the user specified, what you propose, and any unresolved choice that would block the work. Do not present proposed defaults as agreed answers. Missing user decisions stay open until answered. Once the brief follows from the answers and existing authorization, proceed without a routine extra approval question.

Keep evidence and verification distinct. Producing an artifact or test report is one step. Inspecting it against the agreed result is another. Assign the agent the building and checks it can perform, and identify only the access or judgment that needs another owner.

## Build the useful version

Confirm that the required inputs, tools, and access are available before work that depends on them. Continue independent work when another part needs user input.

Follow the owning workspace's rules and use relevant artifact skills for their specific methods. Keep existing approval gates intact.

Build a complete example or usable slice early when it can test the approach. Inspect it, fix what the evidence shows, and extend it until the requested scope is complete. Do not stop at a plan, scaffold, or first slice when the user asked for the finished artifact.

Keep effort proportional. A one-off artifact may need only direct inspection. Add reusable machinery, broad test suites, release work, or extra review only when the task warrants them. Production readiness is a task-specific choice.

## Check the result

Run the checks defined in the brief against the actual result where possible. A tool's success message or an agent's completion claim is evidence of an action, not proof of the whole task.

Use the smallest check that can expose a meaningful failure.

| What is being built | Useful checks |
|---|---|
| Document or deck | Read it against the brief, trace key claims to sources, and inspect the rendered output where layout matters |
| Spreadsheet or analysis | Check a known example, trace inputs and formulas, and inspect the conclusions |
| Tool or automation | Run a representative task and a relevant failure case in the intended environment when accessible |
| Skill or workflow | Walk through a realistic request and inspect the resulting decisions or output |
| Sketch or prototype | Check that it makes the idea concrete enough to answer the agreed question |

For a bug fix, reproduce the problem where feasible and show that the same check passes after the change. For reusable work, include an edge case when it could expose a real weakness.

Separate mechanical checks from judgment. A valid file does not prove a useful result. Check clarity, fit, and usefulness against the brief, and identify choices that still need the user's judgment.

Use a separate reviewer when the cost of a missed error warrants it and delegation is permitted. Give them the requirement and artifact, not just the builder's summary. A second agent's agreement is another judgment, not ground truth. Do not describe self-review as independent verification.

## Resolve gaps

When a check fails, use it to narrow the cause and revise the result. Do not weaken the success criteria just to pass. Change the approach when repeated attempts produce no new evidence. Escalate only the missing input, decision, or access needed to proceed.

If a required check cannot run, distinguish what was built from what remains unverified. A substitute check supports only the claim it actually tests.

## Hand over

Lead with the artifact or result. Briefly state what was checked and any material gap or remaining user decision. Link to the actual files or evidence when useful.

Keep the brief and evidence in the task by default. Create separate plans, logs, or tracking files only when they serve the requested work. Invoking `/build` does not itself authorize sending, publishing, deploying, or expanding the scope.
