# 051 — Studio Product Photo Director

**Category:** images-video · **Difficulty:** Beginner

**Usage:** Use to create a production-ready product image prompt without false features.

**Expected output:** A tool-ready product photo prompt plus negative constraints.

**Tip:** Attach a clean reference image and list features the model must not alter.

## Best tools
- **Adobe Firefly**: Creates controlled commercial-style imagery with detailed visual direction.
- **Leonardo**: Supports polished product concepts and consistent art direction.

## Prompt

```text
You are my Studio Product Photo Director. Write a precise product-photo brief for studio or phone setups. No fake brand assets.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Product: [PRODUCT]
Audience: [AUDIENCE]
Where photos will be used: [USE]
Hero message: [HERO_MESSAGE]
Surface and lighting constraints: [SURFACE_LIGHT]
Details that must show: [MUST_SHOW]
What to avoid in frame: [AVOID]
Gear available: [GEAR]
Shot variants needed: [VARIANTS]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Intent
Clarify photo job for [USE], [AUDIENCE], and [HERO_MESSAGE].

STEP 2 — Shot list
Create a shot list covering [MUST_SHOW] and [VARIANTS] within [GEAR] and [SURFACE_LIGHT].

STEP 3 — Art direction
Specify composition, colour, and [AVOID] rules.

STEP 4 — Capture order
Give a practical shoot order.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Photo intent
B. Shot list
C. Lighting and surface setup
D. Composition rules
E. Must-show details
F. Avoid list
G. Capture order
H. Export/crop notes

Rules: specific and shootable; no impossible studio fantasy for the gear you have.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
