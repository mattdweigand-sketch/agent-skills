# Code Project Structure — Starter Templates

## `CLAUDE.md` Starter

```markdown
# [Project Name]

## What this is
[One paragraph. What the project does, who uses it.]

## How to run it
\```bash
[install / test / dev commands]
\```

## Project-specific notes
[Anything Claude wouldn't know from the code alone. Conventions, gotchas, never-do-without-asking. Delete this section if you have nothing to add yet.]
```

---

## `.claude/settings.json` Baseline

Safe permission defaults — read-only operations allowed, destructive ones denied. Adjust per project as needed.

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(git status)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(git show:*)",
      "Bash(ls:*)",
      "Read",
      "Grep",
      "Glob"
    ],
    "deny": [
      "Bash(git push --force:*)",
      "Bash(git push --force-with-lease:*)",
      "Bash(rm -rf:*)"
    ]
  }
}
```

---

## `.gitignore` Baseline

```
.DS_Store
.claude/settings.local.json
.env
*.swp
*.swo
```

---

## Code Project Day-One File List

After `CLAUDE.md`, add:

- `README.md` — human-facing intro (skip if `CLAUDE.md` already orients well)
- `.env.example` — env var template
- A stack manifest — `package.json`, `pyproject.toml`, `Cargo.toml`, or `go.mod`
- The lockfile alongside the manifest, committed
