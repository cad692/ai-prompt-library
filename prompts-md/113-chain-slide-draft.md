# 113 — Chain Step 5 - Slide Draft

**Category:** chains · **Difficulty:** Intermediate

**Usage:** Draft concise slide content from an approved evidence-mapped presentation outline.

**Expected output:** A complete textual slide draft with source footers and visual directions.

**Tip:** Keep nuance in evidence labels and reserve explanation for speaker notes.

## Best tools
- **Microsoft Copilot**: Can help draft presentation content within PowerPoint from a structured outline.

## Prompt

```text
Role: You are the slide writer at step five; turn the approved outline in [PREVIOUS_OUTPUT] into a restrained, evidence-faithful draft.

For every numbered slide, create a short assertion-style title and only the minimum body copy needed for [AUDIENCE] to grasp the takeaway. Prefer one visual idea over stacked bullet lists. Where a chart is proposed, define chart type, categories, measure, unit, period, source, and the message it should reveal; never fabricate data points.

Add source footers using the evidence IDs supplied. Preserve confidence labels and caveats where omission could mislead. Use [BRAND_GUIDANCE] for terminology and tone, but do not prioritise style over readability. Include an accessible text alternative for each substantive visual.

Mark slides that require an image, permission, updated figure, or manual data build. Avoid tiny citations, decorative clutter, unsupported quotations, and exaggerated headlines. Keep detailed explanation out of slide bodies.

Close with “HANDOFF TO STEP 6”: all slide titles, on-slide text, visual briefs, footers, and unresolved production tasks. The handoff must work as standalone [PREVIOUS_OUTPUT] for speaker-note creation.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
