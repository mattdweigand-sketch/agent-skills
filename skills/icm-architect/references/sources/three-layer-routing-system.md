The three layer routing system

This is the core of the whole thing. Three layers. Each one has a job.

Layer 1: The Map (your entry instructions)

The top-level instruction file is the map. Use CLAUDE.md for Claude Code or AGENTS.md for Codex, following the tool’s supported scope and loading rules. Put the project purpose and routing guidance here.

Think of it as the floor plan. You walk into any building, the floor plan is on the wall, and you know where to go. The CLAUDE.md file tells the AI:





What this project is



What the folder structure looks like



Naming conventions for files



Where things go

This is the most important pattern in the whole system. Inside it, you put a simple table that tells the AI: for this task, read these files, skip those files, you might need these skills.

A routing table makes the intended source selection explicit. Check the files the assistant used and inspect the output; the table does not guarantee correct behavior.





Layer 2: The Rooms (Workspace Context Files)

Each workspace has a context file describing that work. Route the task to the file by name and ask the assistant to read it. The folder name by itself does not control what is loaded.

These context files describe:





What this workspace is for



What the process looks like (first I do this, then I do that)



What files are in here and how they are organized



What skills or tools to use in this workspace

You can write these by hand or have Claude help you write them. They are plain English. Short documents. A few paragraphs.

The recorded Writing Room example uses prepared routing and context files. In your own workspace, ask the assistant to read the named context file and relevant voice or style guidance, then list what it used. Check the result before relying on a shorter request next time.



Layer 3: The Tools (Skills, MCP Servers, and Plug-and-Play)

Layer 3 is where skills and tools live. Skills are processes that someone figured out and packaged into a set of files that tell Claude how to do a specific thing. A PowerPoint skill. A humanizer skill. A doc co-authoring skill.

The key here: you do not load every skill into every workspace. You wire skills into the workspaces where they are needed. Your Production workspace might reference a front-end design skill and a web app testing skill. Your Writing Room might reference a humanizer skill and a doc co-authoring skill.

Reference the skills a task needs and follow your tool’s rules for discovering and loading them. Keeping a list of skills does not prove they were used. Confirm the selected procedure and inspect the output before extending the workflow.



Naming conventions that help you find files

One more thing that makes this system work without any code or databases. In your CLAUDE.md, you add naming conventions.

If a blog draft is created, it gets named like: api-auth-guide_draft.md If it is a newsletter, it gets named like: 2026-03-launch-week.md If it is a demo script version 2, it gets named like: demo_v2.md

Consistent filenames make files easier to find and distinguish. They do not replace every database or search system. Start with names that tell you the topic, stage, and version.



How to make this yours

The template in the video uses a fake project with fake blog posts and demo scripts. That is intentional. You swap the names and rewrite the context files for your own work. The layers stay the same.

If you are a content creator:





Writing Room → Script Lab



Production → Edit Bay



Community → Distribution Hub

If you are a freelancer:





Swap workspaces for: Client Intake, Delivery, Admin



Your context files describe your client process instead of content production

If you are a developer:





Swap workspaces for: Frontend, Backend, Docs



Wire in the skills you actually use (testing, deployment, code review)

The three-layer routing system (map → rooms → tools) works the same way no matter what you do. You change the labels and the context. The architecture holds.







The research behind this

This is not a prompt trick. The thinking behind it comes from decades of software engineering, all the way back to 1972. Separation of concerns. Modular composition. The idea that systems work better when each part does one job and the routing between parts is clear.

The ICM paper, version 2 (18 March 2026), describes five context layers in Section 3: project identity, workspace routing, a stage’s instructions, reusable reference material, and inputs or outputs for the current run. This lesson’s map, rooms and tools are a simpler teaching model, not the paper’s layer numbering.

To extend a workspace into a repeatable process, name each stage’s inputs, work and output, then review that output before continuing. Keep reusable guidance separate from the notes and drafts for one run.

Read Section 3 for the structure and Section 4.6 for the evidence limits. The reported implementations used Claude Opus and Sonnet 4.6; equivalent results across tools were not established. Section 5.2 discusses why concurrent or heavily automated systems can need additional infrastructure.

Research Paper: Interpretable Context Methodology: Folder Structure as Agentic Architecture



Adapt the three-file pattern

Use these blanks to adapt your first folder to your own project. Keep one current set of project facts and reference material, then choose a small task whose result you can check.

Entry file: use AGENTS.md for Codex or CLAUDE.md for Claude Code. Describe the project and where the work belongs.

# Identity
You are helping [YOUR NAME] with [WHAT YOU DO].

# Folder Structure
- /drafts — work in progress
- /final — finished outputs
- /references — background material

# Rules
- Read this file first on every new task
- Ask before creating files outside of /drafts
- When unsure, ask






CONTEXT.md — Describe the current project.

# Current Project
[What you are building or working on. 2-3 sentences.]

# What good looks like
[What a successful output looks like.]

# What to avoid
[Common mistakes or things you do not want.]






REFERENCES.md — Supporting material for the task: excerpts, examples or links to inspect.

# References
[Examples, source excerpts, style guides or notes. Name which material the current task needs.]






With a file-capable assistant, open the project folder and explicitly request your entry file, CONTEXT.md and the relevant references. Ask for one draft, its saved path and the sources it used. In ordinary chat, paste those contents with their filenames, request the same draft and save it yourself. Compare the result with its sources before using it.



