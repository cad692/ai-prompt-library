# 025 — Document Action Harvester

**Category:** documents · **Difficulty:** Beginner

**Usage:** Use this to extract clear tasks, owners, deadlines, and dependencies from text.

**Expected output:** A traceable action register with owners, dates, dependencies, and ambiguities.

**Tip:** Treat implied tasks as proposals until a human confirms the owner and deadline.

## Best tools
- **ChatGPT**: Extracts structured tasks from common document formats and rewrites them clearly.
- **Microsoft Copilot**: Useful when source documents and task workflows sit inside Microsoft 365.

## Prompt

```text
Extract an accountable action register from [DOCUMENT_OR_PASTED_TEXT] without inventing commitments.

The project is [PROJECT], today is [DATE], and our naming convention is [TEAM_ROLES_OR_NAMES]. Scan for explicit actions, promises, approvals, follow-ups, decisions that create work, and unresolved requests. Preserve source page, paragraph, timestamp, or message reference.

Build a register with: action stated as a verb, named owner, due date, priority, dependency, completion evidence, and source location. If the text says “we,” leaves the owner unclear, or gives a relative date such as “next Friday,” mark [CONFIRM OWNER] or [CONFIRM DATE]; do not guess.

Separate the result into Confirmed Actions, Implied Actions Requiring Approval, and Open Questions. Detect duplicate tasks expressed in different wording and merge them while retaining all source references.

Next, identify sequencing conflicts: deadlines before dependencies, one person overloaded, missing approval, or incompatible instructions. Draft a short clarification message covering only the highest-impact uncertainties.

Conclude with a “next 48 hours” view containing actions actually due or blocking others. Do not assign work merely because someone was mentioned. Where dates are calculable, show both the original wording and the interpreted calendar date for human confirmation.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
