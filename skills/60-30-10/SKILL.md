---
name: 60-30-10
description: "Evaluate how a project allocates judgment across owned data, deterministic code, and live model work. Invocation-only: use this skill only when the user explicitly invokes `$60-30-10` or `/60-30-10`, or explicitly asks to use or run the 60-30-10 skill. Do not infer its use from related audit, architecture, prompt, agent, harness, workflow, or judgment-allocation requests."
---

# Composition Audit

## Invocation Gate

Run this workflow only when the user directly invokes `$60-30-10` or `/60-30-10`, or explicitly asks to use or run the 60-30-10 skill. Do not trigger it from topic similarity or from phrases such as composition audit, structure audit, prompt allocation, or judgment allocation alone.

Evaluate whether a project puts each kind of judgment in its most durable home: facts and chosen policy in owned data, machine-checkable behavior in deterministic code, and only genuine interpretation and steering in live model work.

The principle this enforces: every piece of judgment has a right home, and the default home, prose in a prompt, is usually the wrong one. `60/30/10` is a memorable directional guideline for that principle, not a quota, score, compliance threshold, or required numerical result. A healthy system routes each piece to the bucket that fits; its actual ratio may differ substantially for good domain-specific reasons. The failure mode is not missing an exact percentage. It is trapping durable or machine-checkable judgment in perishable model context.

Produce an inline verdict. Do not write a file unless asked.

## Applicability Gate

Audit the target only if it holds reusable judgment: rules, policies, or criteria that decide outputs across runs. This includes agent harnesses, skills, `AGENTS.md` or `CLAUDE.md` systems, MCP workflows, eval pipelines, scoring or recommendation engines, RAG apps, sales or intelligence tools, and wiki or process systems that agents operate against.

If the target has no reusable judgment, say so in one sentence and stop. Do not force the rubric.

## Procedure

1. **Inventory.** Find where judgment physically lives. List prompt surface, owned data, and deterministic code. Correct for off-repo data and reference documents that actually load into model context.
2. **Classify the load-bearing judgment.** Load `references/composition-model.md`. Name the top eight to twelve rules that decide outputs. Record where each currently lives, where it belongs, and who writes it.
3. **Estimate the shape.** Anchor the estimate in that rule set, not a vibe. Give an approximate current split and state confidence. Treat it as a diagnostic aid, never a score.
4. **Name the biggest misallocation.** Identify the single highest-leverage move.
5. **Give a punch list.** Order concrete moves by leverage and lowest risk first.
6. **Render the verdict.** Use the template and field specification in `references/output-template.md`.

This skill produces the verdict and punch list only. It does not execute the moves. Apply-mode requests route to the target project's own tooling and authority boundaries.

## Reference Loading

- `references/composition-model.md` — required for step 2. Owns the buckets, routing sort, counting traps, and good or bad shapes.
- `references/output-template.md` — required for step 6. Owns the verdict template and field specification.
- `references/audit-worksheet.md` — load when the target is large enough that the estimate would otherwise become a vibe.
- `references/worked-example.md` — load before the first run in a session to calibrate depth. Treat its dated project facts as illustrative, not current.

## Sources

This Codex skill is ported from Matt's Claude `60-30-10` skill. It operationalizes the wiki concepts `judgment-routing`, `prompt-technical-debt`, `storage-vs-enforcement`, and `context-as-moat`. When auditing the wiki repo, read the relevant wiki pages only if needed for the target.
