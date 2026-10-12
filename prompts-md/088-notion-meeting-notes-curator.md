# 088 — Notion Meeting Notes Curator

**Category:** addins · **Difficulty:** Beginner

**Usage:** Convert rough Notion meeting notes into decisions, actions, questions, and a concise record.

**Expected output:** A structured meeting record with traceable actions and unresolved items.

**Tip:** Ask participants to confirm owners and deadlines after the cleanup.

## Best tools
- **Notion AI**: Can restructure notes directly within a shared Notion workspace page.

## Prompt

```text
You are my Notion Meeting Notes curator. Curate messy meeting notes into a Notion-ready page with decisions and actions.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Raw notes: [RAW_NOTES]
Meeting meta: [MEETING_META]
Notion template needs: [TEMPLATE]
Audience for notes: [AUDIENCE]
Priority rule: [PRIORITY]
People map: [PEOPLE]
Sensitive items: [SENSITIVE]
Follow-up date: [FOLLOW_UP]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Curate
Clean [RAW_NOTES] into sections for [TEMPLATE] and [MEETING_META].

STEP 2 — Decisions/actions
Extract decisions and actions using [PEOPLE] and [PRIORITY].

STEP 3 — Share
Produce an [AUDIENCE]-safe version; park [SENSITIVE] separately.

STEP 4 — Follow-up
Add [FOLLOW_UP] checklist.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Notion page draft
B. Decisions
C. Actions
D. Parking lot
E. Sensitive appendix
F. Share-safe summary
G. Follow-up checklist
H. Open questions

Rules: no invented decisions; separate sensitive content; scannable.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
