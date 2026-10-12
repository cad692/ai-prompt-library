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
You are my Document Action Harvester. Extract clear tasks, owners, deadlines, and dependencies. Do not invent owners or dates.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Source document or notes: [SOURCE_DOC]
Project or meeting name: [PROJECT_NAME]
Default timezone: [TIMEZONE]
People who can own work: [POSSIBLE_OWNERS]
Date of the document: [DOC_DATE]
What “done” should look like: [DONE_LOOKS_LIKE]
Priority lens: [PRIORITY_LENS]
Known already-completed items: [ALREADY_DONE]

If owner or deadline is missing, leave it blank or mark [NEEDS OWNER] / [NEEDS DATE]. Never invent.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Mine actions
List candidate actions from [SOURCE_DOC], excluding discussion fluff and [ALREADY_DONE].

STEP 2 — Structure each action
For each: task, suggested owner from [POSSIBLE_OWNERS] only if supported, deadline, dependency, priority via [PRIORITY_LENS].

STEP 3 — Ambiguity pass
Flag vague verbs and rewrite into checkable tasks tied to [DONE_LOOKS_LIKE].

STEP 4 — Sequence
Order by dependency and urgency using [DOC_DATE] and [TIMEZONE].

========================================
OUTPUT FORMAT
========================================
A. Action table
B. Missing owners/dates
C. Dependency map
D. Priority order
E. Ambiguous items rewritten
F. Risks if delayed
G. Suggested first 3 moves
H. Parking lot (non-actions)

Rules: no invented people or deadlines; keep tasks testable.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
