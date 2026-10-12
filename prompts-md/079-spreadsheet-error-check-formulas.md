# 079 — Spreadsheet Error Check Formulas

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to design formula-based checks that flag likely spreadsheet errors.

**Expected output:** A formula check library with test cases and review guidance.

**Tip:** Keep every flag column visible during testing and investigate false positives.

## Best tools
- **Excel/Sheets**: Supports transparent formulas, validation rules, and conditional formatting.
- **ChatGPT**: Drafts formula patterns from a supplied schema and business rules.

## Prompt

```text
You are my Spreadsheet Error-Check Formulas coach. Propose error-checking formulas and QA steps for a sheet. Do not invent business rules.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Sheet goal: [SHEET_GOAL]
Key columns: [KEY_COLUMNS]
Known business rules: [KNOWN_RULES]
Error types to catch: [ERROR_TYPES]
Spreadsheet tool: [TOOL]
Sample rows or patterns: [SAMPLE_ROWS]
Who maintains the sheet: [OWNER]
QA cadence: [CADENCE]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Risks
Identify failure modes for [KEY_COLUMNS] given [KNOWN_RULES] and [ERROR_TYPES].

STEP 2 — Checks
Write concrete checks/formulas for [TOOL] using patterns from [SAMPLE_ROWS].

STEP 3 — Workflow
Create a QA checklist for [OWNER] at [CADENCE] aimed at [SHEET_GOAL].

STEP 4 — Flags
Suggest a visible error flag column strategy.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Error risk list
B. Check formulas
C. Flagging approach
D. QA checklist
E. Sample walkthrough
F. False-positive warnings
G. Owner cadence
H. Still-unchecked risks

Rules: tool-accurate; no fake rules; prefer simple robust checks.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
