# 095 — Data-to-Decision Operating Workflow

**Category:** workflows · **Difficulty:** Advanced

**Usage:** Turn operational data into a documented recommendation with validation and accountability.

**Expected output:** A controlled analytical workflow ending in a decision record.

**Tip:** Reconcile totals to the source system before discussing trends.

## Best tools
- **Microsoft Copilot**: Works across spreadsheet analysis, written summaries, and presentation preparation.

## Prompt

```text
You are my Data-to-Decision Operating workflow designer. Create an operating workflow from raw data to a decision meeting with clear owners.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Decision forum: [DECISION_FORUM]
Data sources: [DATA_SOURCES]
Cadence: [CADENCE]
Owners: [OWNERS]
Core metrics: [METRICS]
When to escalate: [SLACK_RULES]
Recurring outputs: [OUTPUTS]
Tools: [TOOLS]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Pipeline
Design data→QA→insight→decision stages for [DECISION_FORUM] at [CADENCE].

STEP 2 — Roles
Assign work using [OWNERS], [DATA_SOURCES], [METRICS], and [TOOLS].

STEP 3 — Escalation
Define [SLACK_RULES] / escalation thresholds.

STEP 4 — Artifacts
Specify [OUTPUTS] and a meeting agenda.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Operating workflow
B. RACI/owners
C. Metric set
D. QA steps
E. Decision agenda
F. Escalation rules
G. Recurring artifacts
H. Failure modes

Rules: decisions on schedule; data quality before debate.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
