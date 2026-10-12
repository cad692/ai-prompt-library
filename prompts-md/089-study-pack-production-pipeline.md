# 089 — Study Pack Production Pipeline

**Category:** workflows · **Difficulty:** Intermediate

**Usage:** Design a multi-tool pipeline that turns learning material into an ethical study pack.

**Expected output:** A sequenced workflow with tools, handoffs, quality gates, and file names.

**Tip:** Keep source citations attached to notes throughout every transformation.

## Best tools
- **ChatGPT**: Coordinates staged transformations and produces clear reusable instructions.

## Prompt

```text
You are my Study Pack Production pipeline designer. Design a pipeline that turns course material into a study pack with recall practice.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Course or exam: [COURSE]
Materials available: [MATERIALS]
Level: [LEVEL]
Desired pack contents: [PACK_CONTENTS]
Days until need: [DAYS]
Daily study time: [DAILY_TIME]
Weak areas: [WEAK_AREAS]
Output format: [FORMAT]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Pipeline
Design stages from [MATERIALS] to [PACK_CONTENTS] for [COURSE] at [LEVEL].

STEP 2 — Schedule
Fit production and study into [DAYS] and [DAILY_TIME], prioritising [WEAK_AREAS].

STEP 3 — Templates
Provide templates in [FORMAT].

STEP 4 — QA
Add quality checks so the pack stays source-faithful.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Pipeline stages
B. Schedule
C. Pack templates
D. Weak-area emphasis
E. Recall components
F. QA checks
G. Daily workflow
H. Risk if behind

Rules: active recall > passive notes; no invented syllabus facts.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
