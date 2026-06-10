# Repo Structure Starter Templates

## `AGENTS.md` Starter

```markdown
# [Project Name]

## What This Is

[One paragraph. What the project does and who uses it.]

## How To Run It

\```bash
[install / test / dev commands]
\```

## Conventions

[Non-obvious project conventions, naming rules, or layout notes.]

## Do Not Do Without Asking

- [Approval boundary, destructive action, external action, or credential-sensitive operation.]

## Pointers

- `README.md` - human intro
- `docs/` - architecture, specs, ADRs, and deeper context
```

## `.Codex/settings.json` Baseline

Shared settings should be safe by default. Put personal overrides in
`.Codex/settings.local.json` and keep that file gitignored.

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Grep",
      "Glob",
      "Bash(git status)",
      "Bash(git diff:*)",
      "Bash(git log:*)",
      "Bash(git show:*)",
      "Bash(ls:*)"
    ],
    "deny": [
      "Bash(git push --force:*)",
      "Bash(git push --force-with-lease:*)",
      "Bash(rm -rf:*)"
    ]
  }
}
```

## `.gitignore` Baseline

```gitignore
.DS_Store
.Codex/settings.local.json
.env
*.swp
*.swo
```

## Code Project Day-One File List

- `AGENTS.md` - agent operating map
- `README.md` - human-facing intro
- `.gitignore` - local settings, env files, and OS/editor noise
- `.env.example` - env var template, no secrets
- stack manifest - `package.json`, `pyproject.toml`, `Cargo.toml`, or `go.mod`
- lockfile - committed when the stack uses one

