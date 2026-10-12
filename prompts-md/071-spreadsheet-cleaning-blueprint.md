# 071 — Spreadsheet Cleaning Blueprint

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to plan safe cleaning before changing a messy spreadsheet.

**Expected output:** A staged cleaning plan with rules, checks, and rollback safeguards.

**Tip:** Never clean the only copy; preserve a read-only raw tab with an import date.

## Best tools
- **Excel/Sheets**: Provides filters, formulas, validation, and reproducible cleaning steps.
- **ChatGPT**: Helps diagnose column issues and draft transformation logic.

## Prompt

```text
You are my Spreadsheet Cleaning Blueprint maker. Create a cleaning plan for messy spreadsheet data before analysis. Do not invent values.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Sheet description: [SHEET_DESCRIPTION]
Analysis goal: [GOAL]
Known issues: [KNOWN_ISSUES]
Key fields: [KEY_FIELDS]
Cleaning rules I want: [RULES]
Values that must stay: [MUST_PRESERVE]
Tools available: [TOOLS]
Time available: [TIME]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Diagnose
List likely quality issues from [SHEET_DESCRIPTION] and [KNOWN_ISSUES].

STEP 2 — Plan
Write a step-ordered cleaning blueprint for [KEY_FIELDS] aimed at [GOAL].

STEP 3 — Rules
Encode [RULES] while preserving [MUST_PRESERVE]; never fabricate cells.

STEP 4 — Execute notes
Provide formulas/checks suited to [TOOLS] within [TIME].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Issue inventory
B. Cleaning step order
C. Field rules
D. Preserve list
E. Validation checks
F. Formula suggestions
G. Rollback plan
H. Ready-for-analysis criteria

Rules: no invented data; reversible steps; document every transform.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
