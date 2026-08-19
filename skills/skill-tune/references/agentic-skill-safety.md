# Agentic Skill Safety Checklist

Load this reference from `skill-tune` when the target artifact grants any of: tool use, file writes, external actions, memory reads or writes, credentials, or approval gates. Skip it for pure prose skills.

Check each dimension. Missing or vague answers are findings.

| Dimension | What to verify |
|---|---|
| Identity | Who the artifact acts as, and whether that identity is stated or assumed. |
| Tools | Which tools or connectors it may call, named explicitly. No open-ended "any tool" grants. |
| Denials | What it must refuse, and how refusals are phrased. |
| Approvals | Which actions require explicit user approval through the available platform gate; whether approval is mandatory and scoped to the exact action. |
| Logs | What gets written to memory, session context, or external systems, and whether the user is told. |
| Retention | How long anything the skill writes persists, and where the deletion path is. |
| Failure behavior | What happens on tool error, quota exhaustion, or partial success. Silent fallback is a finding. |

Each dimension is a Tier 2 rule at minimum. Prefer deterministic wrappers, scripts, or hooks for approvals, denials, and failure behavior when the platform supports them.
