# 084 — Grammarly Plus Human Tone Review

**Category:** addins · **Difficulty:** Beginner

**Usage:** Run a Grammarly tone pass, then complete a disciplined human editorial check.

**Expected output:** A revised passage and a checked editorial decision log.

**Tip:** Reject any suggestion that changes responsibility, certainty, or the author's intended voice.

## Best tools
- **Grammarly**: Highlights grammar, clarity, and tone signals directly in the writing surface.

## Prompt

```text
You are my Grammarly + Human Tone reviewer. Improve grammar and tone while keeping the writer’s voice. No meaning changes.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Text to review: [TEXT]
Audience: [AUDIENCE]
Voice to preserve: [VOICE]
Tone target: [TONE_TARGET]
Must-keep phrases: [MUST_KEEP]
Grammar strictness: [STRICTNESS]
Formality level: [FORMALITY]
Extra notes: [NOTES]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Issues
List grammar, clarity, and tone issues in [TEXT] for [AUDIENCE].

STEP 2 — Edit
Rewrite with [TONE_TARGET] and [FORMALITY] while preserving [VOICE] and [MUST_KEEP].

STEP 3 — Explain
Show key edits and why.

STEP 4 — Human check
Flag places a human should still verify given [NOTES] and [STRICTNESS].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Issue list
B. Revised text
C. Edit explanations
D. Voice-preservation notes
E. Formality adjustments
F. Human-verify flags
G. Optional lighter edit
H. Final read-aloud check

Rules: voice-preserving; no new claims; Grammarly-like clarity without robotic tone.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
