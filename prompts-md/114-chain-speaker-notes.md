# 114 — Chain Step 6 - Speaker Notes

**Category:** chains · **Difficulty:** Intermediate

**Usage:** Create natural speaker notes that add context without reading the slides aloud.

**Expected output:** Timed notes for every slide plus transitions and Q&A preparation.

**Tip:** Rehearse aloud and replace any phrase that does not sound like the actual presenter.

## Best tools
- **Claude**: Can maintain narrative continuity across a complete slide draft and its evidence context.

## Prompt

```text
Goal: Act as the presentation coach for step six; write speaker notes for the slide draft contained in [PREVIOUS_OUTPUT].

Use the presenter's voice [VOICE], audience knowledge [AUDIENCE_LEVEL], and total duration [DURATION]. For each slide, provide an opening sentence, the explanation that is not already visible, evidence nuance, a natural transition, and an estimated speaking time. Expand abbreviations on first use and give pronunciation cues for unfamiliar names where verified.

Notes should sound spoken, not like an essay. Preserve uncertainty and explain chart denominators or baselines that audiences may miss. Add a pause or interaction cue only when it advances the goal. Never introduce new facts without an evidence reference; mark unsupported additions [VERIFY].

Prepare five likely questions, concise evidence-based responses, and an honest fallback for questions outside the research. Include reminders for accessibility, remote delivery, or handouts from [SETTING].

Finish with “HANDOFF TO STEP 7”: the slide-linked notes, timing total, Q&A sheet, and all [VERIFY] items. Ensure this block can be reviewed independently as [PREVIOUS_OUTPUT].
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
