# 060 — Brand Consistent Image Family

**Category:** images-video · **Difficulty:** Beginner

**Usage:** Use to generate several campaign images that feel related but not repetitive.

**Expected output:** A visual system, anchor prompt, and five coordinated scene prompts.

**Tip:** Approve one anchor image before generating the rest of the set.

## Best tools
- **Leonardo**: Supports consistent visual development across a coordinated image series.
- **Adobe Firefly**: Generates varied campaign scenes from controlled brand art direction.

## Prompt

```text
You are my Brand-Consistent Image Family director. Design a set of images that look like one family. Lock style tokens; don’t invent brand rules.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Brand name: [BRAND_NAME]
Known style rules: [KNOWN_STYLE]
Use cases for the set: [USE_CASES]
How many images: [COUNT]
Must-have elements: [MUST_ELEMENTS]
Forbidden elements: [FORBIDDEN]
Colour / type cues: [COLOUR_TYPE]
Mediums to support: [MEDIUMS]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Style lock
Codify [KNOWN_STYLE], [COLOUR_TYPE], [MUST_ELEMENTS], and [FORBIDDEN] for [BRAND_NAME].

STEP 2 — Family plan
Propose [COUNT] image concepts mapped to [USE_CASES] and [MEDIUMS].

STEP 3 — Prompts
Write matched prompts/briefs that share tokens.

STEP 4 — QC
Give a consistency checklist.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Style token lock
B. Image family plan
C. Matched briefs/prompts
D. Shared do/don’t
E. Consistency checklist
F. Edge-case warnings
G. Rollout order
H. Missing brand inputs

Rules: consistency over novelty; never invent logos or trademarks you lack rights to.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
