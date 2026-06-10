---
name: skill-creator-v3
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
metadata:
  version: "2.0"
  category: "meta"
  tags: ["skill-creation", "meta", "templates"]
---

# Skill Creator

Create new skills and iteratively improve them. Core loop: draft the skill, create test prompts, run evals, review with the user, rewrite based on feedback, repeat. After the skill is done, offer description optimization (`references/description-optimization.md`).

## Contract

**Produces:** A complete skill folder (SKILL.md + optional bundled resources), packaged as a .skill file when tooling is available. During development, produces eval results, benchmark reports, and human-review artifacts.
**Upstream input:** User intent (conversation context, example workflows, existing skill drafts). Available MCPs for research. Prior eval results for iteration.
**Downstream consumers:** skill-eval tests the finished skill in production. skill-manager handles packaging and distribution.
**Does NOT produce:** Production-ready skills without human review. Does not run ongoing production testing (use skill-eval). Does not manage or install skills (use skill-manager).

Figure out where the user is in this loop and help them progress. If they say "just vibe with me," skip the formal eval machinery. Match technical language to the user's comfort level. "Evaluation" and "benchmark" are fine. For "JSON" and "assertion," look for cues before using them without explaining.

## Creating a Skill

### Capture Intent

Understand what the user wants. If the current conversation already contains a workflow to capture (e.g., "turn this into a skill"), extract answers from conversation history first: tools used, sequence of steps, corrections, input/output formats. The user fills the gaps and confirms.

1. What should this skill enable an agent to do?
2. When should it trigger? (user phrases/contexts)
3. What's the expected output format?
4. Should we set up test cases? Skills with objectively verifiable outputs (file transforms, data extraction, code generation) benefit from test cases. Subjective skills (writing style, art) often don't. Suggest the appropriate default, let the user decide.

### Interview and Research

Ask about edge cases, input/output formats, example files, success criteria, and dependencies. Wait to write test prompts until this is ironed out. Check available MCPs for research. Come prepared with context.

### Write the SKILL.md

#### v2.0 Frontmatter (all 5 fields required)

```yaml
---
name: skill-name-kebab-case
description: "When to trigger and what it does. Include specific user phrases and contexts."
version: "2.0"
category: "category-name"
tags: ["tag1", "tag2", "tag3"]
---
```

**`name`** — kebab-case identifier matching the folder name.

**`description`** — the primary triggering mechanism. Include both what the skill does AND specific trigger contexts. Make it "pushy" because skill selectors tend to undertrigger. Example: instead of "How to build a dashboard", write "How to build a dashboard. Use whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of data, even if they don't explicitly ask for a dashboard." All "when to use" logic goes here, not in the body.

**`version`** — `"2.0"` for all new skills.

**`category`** — one of: `sales-ops`, `writing`, `tooling`, `meta`, `research`, `reporting`, `design`, `analysis`, `agentic-systems`, `market-intelligence`, `strategy`

**`tags`** — 2-5 keywords for search and grouping.

#### v2.0 Architecture: Point Don't Dump

```
skill-name/
  SKILL.md            (required — keep under 150 lines)
    YAML frontmatter  (all 5 fields)
    Process/routing logic only
    Reference index at bottom
  references/         (loaded on demand, unlimited size)
    topic-a.md        - procedures, templates, scoring tables
    topic-b.md
  scripts/            - executable code for repetitive tasks
  assets/             - templates, icons, fonts
```

**Three-level loading:**
1. **Frontmatter** (always in context, ~100 words) — description drives triggering
2. **SKILL.md body** (loaded on trigger, ≤150 lines) — process and routing only
3. **references/\*** (loaded as needed, unlimited) — all detail

When SKILL.md would exceed 150 lines, move the excess to a reference file with a one-line pointer. When a skill supports multiple variants, put each variant's detail in its own reference file.

**What lives in SKILL.md:** Contract, high-level steps, decision logic, invariants, reference index.
**What lives in references/:** SQL queries, JSON templates, multi-step procedures, scoring tables, output templates — anything needed for only one specific task.

#### Writing Patterns

Use imperative form. Explain the why rather than heavy-handed MUSTs. Use theory of mind. Make skills general, not narrow to specific examples. Write a draft, look at it fresh, improve.

Use exact templates for output formats. Include concrete input/output examples so the model can pattern match.

### Test Cases

After the draft, create 2-3 realistic test prompts. Share with the user for review. Then run them. Save to `evals/evals.json` as prompts only (no assertions yet).

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```

See `references/schemas.md` for the full schema including the assertions field.

## Running and Evaluating Test Cases

Read `references/eval-methodology.md` for the complete eval workflow: running prompts, drafting assertions, grading, aggregating benchmarks, using optional review tooling, and reading feedback. That file is the single source of truth for the eval process.

Get eval outputs in front of the human before evaluating them yourself. If a local `eval-viewer/generate_review.py` tool is available, use it; otherwise present a concise markdown review table.

## Improving the Skill

Four principles for improvement:

1. **Generalize from feedback.** The skill will be used across many prompts. You're iterating on a few examples because it's faster. If changes only fix those examples, they're useless. Rather than fiddly overfitty changes or oppressive MUSTs, try different metaphors or patterns.

2. **Keep the prompt lean.** Remove what isn't pulling its weight. Read transcripts, not just outputs. If the skill makes the model waste time on unproductive steps, cut those parts.

3. **Explain the why.** Today's LLMs are smart. When given reasoning, they go beyond rote instructions. If you find yourself writing ALWAYS or NEVER in all caps, reframe and explain why the thing matters.

4. **Look for repeated work.** Read transcripts. If all test cases independently wrote similar helper scripts, bundle that script in `scripts/` and tell the skill to use it.

After improving, rerun all test cases, prepare human review, and iterate. See `references/eval-methodology.md` for the full loop.

## Description Optimization
Read `references/description-optimization.md` for the complete process: generating trigger eval queries, reviewing with the user, running the optimization loop, and applying results.

## Package and Present
If packaging tooling is available, package the skill and direct the user to the `.skill` file. Some environments provide `python -m scripts.package_skill <path/to/skill-folder>` outside the skill folder; if unavailable, present the folder tree and files to deliver.

## Environment Notes
Read `references/environment-instructions.md` for platform-specific adaptations when tooling differs from the local CLI.

## Reference Files

- `agents/grader.md`, `agents/comparator.md`, `agents/analyzer.md`: Optional eval subagent instructions
- `references/schemas.md`: JSON structures for evals.json, grading.json, benchmark.json
- `references/eval-methodology.md`: Complete eval running workflow
- `references/description-optimization.md`: Trigger accuracy optimization
- `references/environment-instructions.md`: Platform-specific adaptations

Add "Create evals JSON and put eval outputs in front of the human before self-grading" to your TodoList.
