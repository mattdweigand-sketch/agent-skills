---
name: 60-30-10
description: "Evaluate how a project allocates judgment across owned data, deterministic code, and prompt-model work. Invocation-only: use this skill only when the user explicitly invokes `$60-30-10` or `/60-30-10`, or explicitly asks to use or run the 60-30-10 skill. Do not infer its use from related audit, architecture, prompt, agent, harness, workflow, or judgment-allocation requests."
---

# Composition Audit

## Invocation Gate

Run this workflow only when the user directly invokes `$60-30-10` or `/60-30-10`, or explicitly asks to use or run the 60-30-10 skill. Do not trigger it from topic similarity or from phrases such as composition audit, structure audit, prompt allocation, or judgment allocation alone.

Evaluate whether a project puts each kind of judgment in its most durable home: facts and chosen policy in owned data, consequence-worthy checks and fixed execution in deterministic code, and only genuine interpretation and steering in prompt-model work.

In this skill, `60/30/10` always means **owned data / deterministic code / prompt-model work**. It does not mean the separate public or source heuristic of 60% traditional code / 30% rule-based logic / 10% AI calls.

The principle this enforces: every necessary piece of judgment has a right home, and the default home, prose in a prompt, is usually the wrong one. `60/30/10` is a memorable directional guideline for that principle, not a quota, score, compliance threshold, codebase-composition claim, or required numerical result. A healthy system routes each piece to the bucket that fits; its actual ratio may differ substantially for good domain-specific reasons. The failure mode is not missing an exact percentage. It is manufacturing live decisions for fixed sequences or trapping durable and consequence-worthy judgment in perishable model context.

Produce an inline verdict. Do not write a file unless asked. When the user asks for a saved verdict, validate its structure before delivery.

## Applicability Gate

Audit the target only if it holds reusable judgment: rules, policies, or criteria that decide outputs across runs. This includes agent harnesses, skills, `AGENTS.md` or `CLAUDE.md` systems, MCP workflows, eval pipelines, scoring or recommendation engines, RAG apps, sales or intelligence tools, and wiki or process systems that agents operate against.

If the target has no reusable judgment, say so in one sentence and stop. Do not force the rubric.

## Procedure

1. **Inventory.** Read the user-supplied target and its declared direct dependencies. List owned data, deterministic code, and prompt-model work. Correct for declared off-repo data and reference documents that actually load into model context. Do not query connectors, credentials, or unrelated repositories to discover more data. If a declared dependency cannot be read, mark that bucket `unknown/unverified`, state the resulting confidence limit, and do not infer its contents. Identify any model decision that is really a fixed pipeline.
2. **Classify the load-bearing judgment.** Load `references/composition-model.md`. When the target has fewer than eight load-bearing rules, name all of them; otherwise name the top eight to twelve. Record where each currently lives, where it belongs or whether it should be deleted, its consequence if wrong once, and who writes it.
3. **Estimate the shape.** Anchor the estimate in that rule set, not a vibe. Give an approximate current split and state confidence. Treat it as a diagnostic aid, never a score.
4. **Name the biggest misallocation.** Identify the single highest-leverage move.
5. **Check connected targets for duplicated policy.** Inspect only the repos, workflows, or execution surfaces the target directly names, loads, generates, or depends on. Do not use connectors or credentials to discover targets. Name one duplicated chosen policy and its owner, or state the bounded scope and that none was found. Do not roam unrelated systems.
6. **Give a punch list.** Order concrete moves by leverage and lowest risk first.
7. **Render the verdict.** Use the template and field specification in `references/output-template.md`. When the verdict is available as a local text file, run `python3 scripts/validate_composition_audit_report.py <report-file>` and correct structural failures before delivery. The validator checks format only, never placement judgment.

This skill produces the verdict and punch list only. It does not execute the moves. Apply-mode requests route to the target project's own tooling and authority boundaries.

## Reference Loading

- `references/composition-model.md` — required for step 2. Owns the buckets, routing sort, counting traps, and good or bad shapes.
- `references/output-template.md` — required for step 6. Owns the verdict template and field specification.
- `references/audit-worksheet.md` — load when the target is large enough that the estimate would otherwise become a vibe.
- `references/worked-example.md` — load when the target's shape is unfamiliar and you need to calibrate depth. Treat its dated project facts as illustrative, not current.
- `scripts/validate_composition_audit_report.py` — run only against a saved verdict. Owns the mechanically checkable output contract.

## Sources

This Codex skill is ported from Matt's Claude `60-30-10` skill. It operationalizes the wiki concepts `judgment-routing`, `prompt-technical-debt`, `storage-vs-enforcement`, and `context-as-moat`. When auditing the wiki repo, read the relevant wiki pages only if needed for the target.
