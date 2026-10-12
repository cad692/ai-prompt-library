# 090 — Monthly Content Calendar Pipeline

**Category:** workflows · **Difficulty:** Intermediate

**Usage:** Build a repeatable workflow from audience insight to approved, scheduled content.

**Expected output:** A month-long content workflow with handoffs, controls, and metrics.

**Tip:** Separate factual review from style approval so neither becomes a quick checkbox.

## Best tools
- **Claude**: Handles long brand context and can organise a detailed editorial workflow.

## Prompt

```text
You are my Monthly Content Calendar pipeline designer. Build a monthly content calendar pipeline with realistic capacity. No fake viral promises.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Month: [MONTH]
Channels: [CHANNELS]
Content goals: [GOALS]
Content pillars: [PILLARS]
Production capacity: [CAPACITY]
Assets on hand: [ASSETS]
CTA map: [CTA_MAP]
Constraints: [CONSTRAINTS]
Review cadence: [REVIEW]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Strategy
Align [GOALS] and [PILLARS] to [CHANNELS] for [MONTH].

STEP 2 — Pipeline
Design ideation→draft→approve→schedule stages within [CAPACITY] and [CONSTRAINTS].

STEP 3 — Calendar
Propose a calendar using [ASSETS] and [CTA_MAP].

STEP 4 — Ops
Set [REVIEW] and backlog rules.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Monthly strategy
B. Pipeline stages
C. Calendar draft
D. Capacity check
E. CTA mapping
F. Asset reuse plan
G. Review cadence
H. Kill criteria for weak ideas

Rules: capacity-honest; pillar-consistent; no engagement guarantees.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
