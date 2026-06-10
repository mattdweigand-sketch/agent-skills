---
# Skill Creator — Platform Adaptations

How to run the skill creator workflow in environments without full tool access.

---

## Web Chat Environments Without Tools

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

**Packaging:** Local packaging helpers may be unavailable. Present the skill folder structure as a tree and list which files to create manually.

---

## Agent Workspaces With Files But No Browser

**What's often available:**
- Full subagent support
- File writes
- Python scripts

**What's different:**
- No browser for viewing the HTML output
- Feedback is collected via file download

**Viewer workflow:**
1. If the local viewer helper exists, run `python eval-viewer/generate_review.py evals/grading.json` — produces `eval-viewer/review.html`
2. Tell the user the file path and ask them to open it locally in a browser
3. The viewer has a "Download Feedback" button — user downloads `feedback.json`
4. If the local feedback helper exists, load it back: `python eval-viewer/load_feedback.py <path-to-feedback.json>`
5. This updates `grading.json` with `human_score` and `human_notes` per eval

If either helper is unavailable, use the markdown review fallback and update `grading.json` from the user's feedback manually.

**Everything else:** Follow `eval-methodology.md`, using parallel agents and automated grading only when those capabilities exist.

---

## Detecting Your Environment

| Signal | Environment |
|---|---|
| `present_files` or packaging helper available | Local CLI or desktop workspace |
| No file writes or Python execution | Web chat |
| File writes and agents available, no browser tool | Agent workspace without browser access |

When unsure, ask which tools are available before starting the eval loop.
