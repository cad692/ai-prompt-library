# 027 — Transcript Clarity Editor

**Category:** documents · **Difficulty:** Intermediate

**Usage:** Use this to clean a meeting transcript while preserving meaning and accountability.

**Expected output:** A cleaned transcript, uncertainty log, decisions, and verified action items.

**Tip:** Keep the raw transcript unchanged alongside the edited version for auditability.

## Best tools
- **Claude**: Handles long transcripts and preserves context across speaker turns.
- **Microsoft Copilot**: Fits meeting workflows involving Teams transcripts and Microsoft documents.

## Prompt

```text
Clean [MEETING_TRANSCRIPT] into a readable record without changing what participants meant.

Meeting title and date: [MEETING_DETAILS]. Known speakers: [SPEAKER_LIST]. Desired output: [CLEAN_TRANSCRIPT_OR_MINUTES]. Treat the original as the authority. Do not invent names, fix factual disagreements, or turn tentative suggestions into decisions.

For the cleaned transcript, standardise speaker labels, punctuation, and paragraph breaks. Remove filler only when meaning and tone remain intact. Retain meaningful hesitation, disagreement, conditions, and uncertainty. Replace inaudible or doubtful segments with [UNCLEAR at TIMESTAMP] and include the nearest safe context.

Keep timestamps at [INTERVAL_OR_TOPIC_CHANGES]. Mark any proposed correction to a number, name, or technical term in braces as {VERIFY: ...}; never silently substitute it.

After the transcript, provide:
- decisions explicitly made;
- action items with owner, deadline, and timestamp;
- proposals not yet approved;
- unresolved questions;
- an uncertainty log for every [UNCLEAR] or {VERIFY} marker.

Finish with a five-sentence meeting summary that distinguishes discussion from commitment. If speakers shared personal, client, or confidential data, flag passages for redaction before circulation. Do not infer emotion from voice or wording unless it was explicitly stated.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
