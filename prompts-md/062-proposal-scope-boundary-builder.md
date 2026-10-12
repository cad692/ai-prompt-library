# 062 — Proposal Scope Boundary Builder

**Category:** work-business · **Difficulty:** Beginner

**Usage:** Use to define project deliverables, exclusions, acceptance, and change handling.

**Expected output:** A proposal scope with deliverables, boundaries, assumptions, and acceptance criteria.

**Tip:** Write acceptance criteria so both sides can observe whether the work is complete.

## Best tools
- **Claude**: Structures detailed scope language across long project notes.
- **Notion**: Keeps scope, deliverables, and decisions in a collaborative workspace.

## Prompt

```text
You are my Proposal Scope Boundary builder. Define what is in, out, and negotiable in a proposal so scope creep is harder. Do not invent client promises.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Project: [PROJECT]
Client goal: [CLIENT_GOAL]
In-scope items: [IN_SCOPE]
Out-of-scope items: [OUT_SCOPE]
Assumptions: [ASSUMPTIONS]
Dependencies: [DEPENDENCIES]
Timeline: [TIMELINE]
Budget band: [BUDGET_BAND]
Change-request rule: [CHANGE_RULE]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Boundaries
Turn [IN_SCOPE] and [OUT_SCOPE] into crisp boundary statements for [PROJECT].

STEP 2 — Assumptions
List [ASSUMPTIONS] and [DEPENDENCIES] that must hold.

STEP 3 — Commercial
Align [TIMELINE], [BUDGET_BAND], and [CHANGE_RULE] to [CLIENT_GOAL].

STEP 4 — Proposal text
Write paste-ready scope sections.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. In-scope list
B. Out-of-scope list
C. Assumptions
D. Dependencies
E. Timeline & budget band
F. Change-request rule
G. Client confirmation questions
H. Risk if boundaries blur

Rules: clear boundaries; no hidden free work; no fake deliverables.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
