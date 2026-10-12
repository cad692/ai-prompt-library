# 065 — SOP First Draft Mapper

**Category:** work-business · **Difficulty:** Beginner

**Usage:** Use to turn process knowledge into a testable first SOP.

**Expected output:** A versioned SOP draft with steps, exceptions, and a test plan.

**Tip:** Have a new team member test the SOP while the process owner only observes.

## Best tools
- **Notion**: Publishes searchable SOPs with linked templates and revision history.
- **Claude**: Structures detailed process notes and edge cases coherently.

## Prompt

```text
You are my SOP First-Draft mapper. Map a practical SOP first draft from real work steps. Do not invent unsafe procedures.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Process name: [PROCESS_NAME]
Process goal: [GOAL]
Actors involved: [ACTORS]
What triggers the process: [TRIGGER]
Known steps: [STEPS_KNOWN]
Tools used: [TOOLS]
Risks or failure points: [RISKS]
Compliance notes: [COMPLIANCE]
Who will follow the SOP: [AUDIENCE]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Scope
Define start/end from [TRIGGER] and [GOAL] for [PROCESS_NAME].

STEP 2 — Steps
Turn [STEPS_KNOWN] into numbered steps with actors from [ACTORS] and [TOOLS].

STEP 3 — Risks
Add checks for [RISKS] and [COMPLIANCE].

STEP 4 — Draft
Produce an SOP draft suited to [AUDIENCE] with open questions marked.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. SOP purpose & scope
B. Roles
C. Step-by-step draft
D. Tools checklist
E. Risk controls
F. Compliance notes
G. Open questions
H. Revision owners suggestion

Rules: practical and safe; mark unknowns; no fake policy citations.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
