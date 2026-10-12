# 113 — Chain Step 5 - Slide Draft

**Category:** chains · **Difficulty:** Intermediate

**Usage:** Draft concise slide content from an approved evidence-mapped presentation outline.

**Expected output:** A complete textual slide draft with source footers and visual directions.

**Tip:** Keep nuance in evidence labels and reserve explanation for speaker notes.

## Best tools
- **Microsoft Copilot**: Can help draft presentation content within PowerPoint from a structured outline.

## Prompt

```text
You are my Chain Slide Draft writer. Draft slides from the chain outline with one message per slide. No invented charts.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Presentation outline: [OUTLINE]
Slide count: [SLIDE_COUNT]
Audience: [AUDIENCE]
Data allowed on slides: [DATA_ALLOWED]
Visual notes: [VISUAL_NOTES]
Brand/template notes: [BRAND]
Closing ask: [ASK]
Handoff to speaker notes: [HANDOFF]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Draft
Create [SLIDE_COUNT] slides from [OUTLINE] for [AUDIENCE].

STEP 2 — Evidence
Use only [DATA_ALLOWED]; suggest visuals via [VISUAL_NOTES] without faking numbers.

STEP 3 — Polish
Apply [BRAND] constraints and make [ASK] unmistakable.

STEP 4 — Handoff
Prepare speaker-note hooks for [HANDOFF].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Slide-by-slide draft
B. One-message titles
C. Allowed data used
D. Visual suggestions
E. Ask slide
F. Caveats slide
G. Notes hooks
H. Still-missing assets

Rules: one message per slide; chain-faithful; no decorative fake charts.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
