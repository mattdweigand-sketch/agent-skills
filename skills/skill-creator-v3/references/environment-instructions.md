---
# Skill Creator — Environment Adaptations

How to run the skill creator workflow in environments without full tool access.

---

## Claude.ai (Web — No Subagents, No Browser)

**What's unavailable:**
- Spawning parallel agent runs for evals
- Opening the HTML viewer in a browser
- Running Python scripts directly

**Adaptations:**

**Eval runs:** Run test cases sequentially in the same conversation instead of parallel agents. After each prompt, record the output inline as a fenced block. Label each clearly:

```
### Eval 1: [prompt summary]
**Output:**
[response here]
```

**Viewer replacement:** Instead of generating the HTML viewer, present a formatted markdown summary:

```
## Eval Results

### Eval 1: [prompt]
**Output:** [response]
**Expected:** [expected_output from evals.json]
**Your assessment:** Pass / Fail?

### Eval 2: [prompt]
...
```

Ask the user to review and reply with pass/fail per eval. Wait before writing assertions.

**Grading and benchmark:** Write `grading.json` and `benchmark.json` manually based on user feedback. No automated runner.

**Packaging:** The `python -m scripts.package_skill` step is unavailable. Present the skill folder structure as a tree and list which files to create manually.

---

## Cowork Environment

**What's available:**
- Full subagent support
- File writes
- Python scripts

**What's different:**
- No browser for viewing the HTML output
- Feedback is collected via file download

**Viewer workflow:**
1. Run `python eval-viewer/generate_review.py evals/grading.json` — produces `eval-viewer/review.html`
2. Tell the user the file path and ask them to open it locally in a browser
3. The viewer has a "Download Feedback" button — user downloads `feedback.json`
4. Load it back: `python eval-viewer/load_feedback.py <path-to-feedback.json>`
5. This updates `grading.json` with `human_score` and `human_notes` per eval

**Everything else:** Runs as described in `eval-methodology.md` — parallel agents, automated grading, benchmark appending.

---

## Detecting Your Environment

| Signal | Environment |
|---|---|
| `present_files` tool available | CLI / Claude Code |
| No tool for spawning agents | Claude.ai web |
| Agents available, no browser MCP | Cowork |

When unsure, ask: "Are you running in Claude.ai, Cowork, or the CLI?" before starting the eval loop.
