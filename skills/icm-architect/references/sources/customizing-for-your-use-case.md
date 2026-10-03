3.2 Customizing for Your Use Case
Choose one example below and build only the part needed for your next deliverable. Run one task before adding more folders.
Illustrated practice guide. Choose one example below and build only the part needed for your next deliverable. Run one task before adding more folders.
The original examples use Claude and CLAUDE.md. With Codex, use AGENTS.md for project instructions. With ordinary chat, paste or attach the instructions and the specific source material for that task, then save the result yourself. A CONTEXT.md filename alone does not guarantee that its contents were read. [4.4: Project Instructions](https://www.skool.com/cliefnotes/classroom/036893d9?md=f0655889bd8c49b0a99f5afb9eb03229&utm_campaign=skool_link_classroom&utm_content=9a42d1d697754c499c3effeee8135e03 "https://www.skool.com/cliefnotes/classroom/036893d9?md=f0655889bd8c49b0a99f5afb9eb03229&utm_campaign=skool_link_classroom&utm_content=9a42d1d697754c499c3effeee8135e03") explains how to connect the pieces.
You will see how the three-layer folder architecture changes shape for three different kinds of work. The layers stay the same. The names, the context files, and the routing all change. You will walk away knowing how to build yours.
In [Section 3.1 ](https://skool.com/cliefnotes/classroom/036893d9?md=2b4a8ab7461c4f6d828e21c0eb196a6a&utm_campaign=skool_link_classroom&utm_content=9a42d1d697754c499c3effeee8135e03 "https://skool.com/cliefnotes/classroom/036893d9?md=2b4a8ab7461c4f6d828e21c0eb196a6a&utm_campaign=skool_link_classroom&utm_content=9a42d1d697754c499c3effeee8135e03")you saw the full architecture: a top-level identity file (CLAUDE.md), workspace-level context files, and skills or tools that plug in where needed. The example in the video used a fake project with a community workspace, a production workspace, and a writing room.
That example was intentional. It is close enough to real work that you can see the logic, but generic enough that you have to make it your own. This lesson shows you how.
The principle is short: the layers do not change. The labels do. Your CLAUDE.md still sits at the top and routes everything. Each workspace still has its own context file. Skills still plug in where they are needed. But what each workspace is called, what the context files say, and what skills are wired in will look completely different depending on what you actually do.
Here are three illustrative structures. Find the one closest to your situation, study it, then build your own.
You make videos, write posts, manage a social presence, and probably do it mostly alone or with a very small team. Your work moves through a cycle: come up with ideas, write scripts or outlines, produce the content, publish it.
Your workspaces:
```
my-content-project/
├── CLAUDE.md
├── script-lab/
│   ├── CONTEXT.md
│   ├── ideas/
│   ├── drafts/
│   └── final/
├── production/
│   ├── CONTEXT.md
│   ├── briefs/
│   ├── specs/
│   ├── builds/
│   └── output/
└── distribution/
    ├── CONTEXT.md
    ├── platforms/
    ├── scheduling/
    └── analytics/





```
🟠 Script Lab — This is where thinking happens. Ideas go in. Drafts come out. The CONTEXT.md in this folder describes your voice, your audience, the kind of content you make, and the process you follow from idea to finished script. If those details grow, put them in separate Markdown files and reference them by name. If you have a style guide or a list of topics you keep coming back to, that goes in here. Give the assistant this context, then check the draft against a real example of your writing.
🟡 Production — This is where content gets built. If you are making animations (like the pipeline in [Section 2.6](https://skool.com/cliefnotes/classroom/036893d9?md=3a82e3222c2c4cbc9d07c6f9f6d4265a&utm_campaign=skool_link_classroom&utm_content=9a42d1d697754c499c3effeee8135e03 "https://skool.com/cliefnotes/classroom/036893d9?md=3a82e3222c2c4cbc9d07c6f9f6d4265a&utm_campaign=skool_link_classroom&utm_content=9a42d1d697754c499c3effeee8135e03")), this is where your briefs, specs, and build files live. If you are making simple videos, this might be where your shot lists, thumbnails, and description templates go. The CONTEXT.md here describes your production process, your tools, your visual standards.
🟢 Distribution — This is where finished content goes out. Platform-specific formatting (what works on Instagram vs LinkedIn vs YouTube), scheduling, repurposing long content into short clips. The CONTEXT.md describes your platforms, posting cadence, and any rules about how content should be adapted per channel.
Your top-level file tells Claude what this project is and how to route between the three workspaces. Something like:
```
# My Content Project

I create [TYPE OF CONTENT] for [AUDIENCE].

## Workspaces
- /script-lab — Idea development, writing, drafts
- /production — Building and producing content
- /distribution — Publishing, scheduling, repurposing

## Routing
| Task | Go to | Read |
|------|-------|------|
| Write or brainstorm | /script-lab | CONTEXT.md |
| Build or produce | /production | CONTEXT.md |
| Publish or repurpose | /distribution | CONTEXT.md |

## Naming conventions
- Drafts: topic-name_draft.md
- Final scripts: topic-name_final.md
- Published: YYYY-MM-platform-topic.md





```


You work with multiple clients. Each engagement has a lifecycle: intake, scoping, delivery, follow-up. You need Claude to shift between clients without bleeding context. You also need your own internal workspace for business development, templates, and admin.
```
my-consulting-practice/
├── CLAUDE.md
├── client-alpha/
│   ├── CONTEXT.md
│   ├── intake/
│   ├── deliverables/
│   └── communications/
├── client-beta/
│   ├── CONTEXT.md
│   ├── intake/
│   ├── deliverables/
│   └── communications/
├── templates/
│   ├── CONTEXT.md
│   ├── proposals/
│   ├── reports/
│   └── frameworks/
└── business-dev/
    ├── CONTEXT.md
    ├── pipeline/
    ├── outreach/
    └── case-studies/





```
🟠 Client workspaces (one per client) — Keep each client’s project facts, sources, and outputs together. Name the permitted sources for the task and inspect what the assistant used. Access depends on tool permissions and environment isolation; separate folders alone do not enforce it.
🟡 Templates — Your reusable frameworks. Proposal templates, report structures, analysis frameworks. The CONTEXT.md here describes what each template is for and how to use it. When you start a new engagement, you pull from templates into the client folder and customize.
🟢 Business Dev — Pipeline tracking, outreach drafts, case studies from past work. The CONTEXT.md describes your ideal client, your services, your positioning. When you need Claude to help draft an outreach email or build a case study, it reads this context.
```
# My Consulting Practice

I am a [TYPE] consultant working with [TYPES OF CLIENTS].

## Active Clients
- /client-alpha — [One-line description of engagement]
- /client-beta — [One-line description of engagement]

## Internal
- /templates — Reusable proposals, reports, frameworks
- /business-dev — Pipeline, outreach, case studies

## Routing
| Task | Go to | Read |
|------|-------|------|
| Client work for Alpha | /client-alpha | CONTEXT.md |
| Client work for Beta | /client-beta | CONTEXT.md |
| Build a new proposal | /templates | CONTEXT.md, then client folder |
| Outreach or pipeline | /business-dev | CONTEXT.md |

## Rules
- Never reference one client's information in another client's workspace
- Proposals always start from /templates and get customized in the client folder
- Deliverables go in /client-[name]/deliverables, drafts stay in working folders





```
The key for freelancers: the client folders multiply. When you onboard a new client, you copy the structure, write a new CONTEXT.md, and Claude is ready. The CLAUDE.md at the top gets one new line in the routing table. That is it.


You build software. You might work on one project or several. Your work involves planning, writing code, testing, deploying, and documenting. You probably already have opinions about folder structure. The difference here is that Claude reads it.
```
my-app/
├── CLAUDE.md
├── planning/
│   ├── CONTEXT.md
│   ├── specs/
│   ├── architecture/
│   └── decisions/
├── src/
│   ├── CONTEXT.md
│   ├── components/
│   ├── services/
│   ├── utils/
│   └── tests/
├── docs/
│   ├── CONTEXT.md
│   ├── api/
│   ├── guides/
│   └── changelog/
└── ops/
    ├── CONTEXT.md
    ├── deploy/
    ├── monitoring/
    └── scripts/





```
🟠 Planning — Specs, architecture decisions, design docs. The CONTEXT.md describes the app, the tech stack, the current priorities, and any architectural principles you follow. When you tell Claude to help you spec a new feature, it reads this context and works within your existing architecture.
🟡 Src — The actual codebase. Its CONTEXT.md can describe naming conventions, patterns, testing requirements, and relevant libraries. Ask the assistant to read that guidance, then review and test the proposed change against the codebase.
🟢 Docs — API documentation, user guides, changelogs. The CONTEXT.md describes your documentation standards, the audience for each type of doc, and how docs relate to the code.
🔵 Ops — Deployment, monitoring, operational scripts. The CONTEXT.md describes your infrastructure, deploy process, and any runbook conventions.
```
# My App

[APP NAME] — [One sentence description]

## Tech Stack
- Frontend: [framework]
- Backend: [language/framework]
- Database: [type]
- Deploy: [platform]

## Workspaces
- /planning — Specs, architecture, decisions
- /src — Application code
- /docs — Documentation
- /ops — Deployment and operations

## Routing
| Task | Go to | Read | Skills |
|------|-------|------|--------|
| Spec a feature | /planning | CONTEXT.md | — |
| Write code | /src | CONTEXT.md | testing-skill |
| Write docs | /docs | CONTEXT.md | doc-authoring-skill |
| Deploy or debug | /ops | CONTEXT.md | — |

## Naming conventions
- Specs: feature-name_spec.md
- Components: PascalCase
- Tests: feature-name.test.ts
- Decision records: YYYY-MM-DD-decision-title.md





```
The Skills column names procedures that may help with a task, such as testing or documentation. Follow your tool’s skill-loading rules and verify that the relevant guidance was used. Listing a skill in a table does not install or activate it.


You do not need to match any of these exactly. The process is the same regardless of what you do.
Step 1: List your workspaces. Think about the 2-4 major areas of your work. What are the modes you shift between? Writing and building are different workspaces. Client A and Client B are different workspaces. Planning and executing might be different workspaces. If you find yourself wishing Claude would "forget" what it was just doing and focus on something else, that is a workspace boundary.
Step 2: Write a CONTEXT.md for each one. Describe what happens in this workspace, what the process is, what files live here, and what good work looks like. Keep it under a page. You can always add more later.
Step 3: Write your CLAUDE.md. List the workspaces and build the routing table. For each type of task, tell Claude where to go and what to read. Add naming conventions so Claude knows how to organize files.
Step 4: Start working. Point Claude at the folder and give it a task. See what happens. Adjust the context files based on what Claude gets right and what it gets wrong. The first version will not be perfect. Keep changes that improve the task when you rerun it; remove instructions that add noise.
The context files are living documents. Edit them as your projects change, as you learn what Claude needs to know, as you figure out what to cut. The people who get the most out of this system are the ones who treat the context files like working notes, not finished documents.