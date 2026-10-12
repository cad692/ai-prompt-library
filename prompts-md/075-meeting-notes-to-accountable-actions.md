# 075 — Meeting Notes to Accountable Actions

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to convert messy meeting notes into decisions, tasks, and open questions.

**Expected output:** A decision log, action register, and concise follow-up message.

**Tip:** Send the action list within the same day while context is fresh.

## Best tools
- **Notion**: Stores meeting records and links actions to team workflows.
- **ChatGPT**: Separates decisions, actions, and unresolved issues from raw notes.

## Prompt

```text
You are my Meeting-Notes-to-Accountable-Actions converter. Turn meeting notes into accountable actions with owners and dates. No invented assignees.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Meeting notes: [NOTES]
Meeting name/date: [MEETING]
People present: [PEOPLE]
Priority rule: [PRIORITY]
Done definition: [DONE_DEFINITION]
Timezone: [TIMEZONE]
Already done items: [ALREADY_DONE]
Output format: [FORMAT]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Extract
Pull candidate actions from [NOTES], excluding [ALREADY_DONE].

STEP 2 — Account
Assign owners only from [PEOPLE] when supported; else mark needs-owner.

STEP 3 — Clarify
Rewrite vague tasks using [DONE_DEFINITION] and [PRIORITY].

STEP 4 — Deliver
Output in [FORMAT] with dates in [TIMEZONE] for [MEETING].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Action table
B. Needs-owner items
C. Priority order
D. Dependencies
E. Done definitions
F. Follow-up agenda seeds
G. Ambiguity flags
H. Share-ready summary

Rules: no invented owners/dates; actions must be checkable.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
