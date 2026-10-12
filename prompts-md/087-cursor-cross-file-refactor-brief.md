# 087 — Cursor Multi-File Refactor Brief

**Category:** addins · **Difficulty:** Advanced

**Usage:** Ask Cursor to refactor several files while preserving public behavior and limiting scope.

**Expected output:** A scoped refactor, affected-file summary, and test evidence.

**Tip:** Name the permitted files and verification command before authorising edits.

## Best tools
- **Cursor**: Can inspect related files and apply coordinated edits across a codebase.

## Prompt

```text
You are my Cursor Multi-File Refactor brief writer. Create a precise multi-file refactor brief for Cursor. Scope tightly; no drive-by rewrites.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Refactor goal: [REFACTOR_GOAL]
Files involved: [FILES]
Current pain: [CURRENT_PAIN]
Invariants to preserve: [INVARIANTS]
Done looks like: [DONE_LOOKS_LIKE]
Tests to run: [TESTS]
Out of scope: [OUT_OF_SCOPE]
Risks: [RISKS]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Scope
Define a tight refactor from [REFACTOR_GOAL], [FILES], and [OUT_OF_SCOPE].

STEP 2 — Brief
Write a Cursor agent brief with steps, [INVARIANTS], and [DONE_LOOKS_LIKE].

STEP 3 — Verify
Specify [TESTS] and risk checks from [RISKS]/[CURRENT_PAIN].

STEP 4 — Stop
State stop conditions and review checklist.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Refactor brief
B. File touch list
C. Invariants
D. Step plan
E. Tests to run
F. Out-of-scope walls
G. Risk notes
H. Review checklist

Rules: surgical; preserve behaviour; no unrelated cleanup.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
