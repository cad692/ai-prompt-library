# 043 — One Message per Slide Editor

**Category:** presentations · **Difficulty:** Beginner

**Usage:** Use when slides contain dense paragraphs, mixed messages, or unclear headlines.

**Expected output:** A slide rewrite map with message headlines, cuts, and split recommendations.

**Tip:** Read only the revised headlines in order; they should tell the complete story.

## Best tools
- **ChatGPT**: Reorganizes pasted slide copy while preserving the intended argument.
- **Claude**: Handles long decks and maintains narrative continuity across slides.

## Prompt

```text
Work as a ruthless-but-faithful slide editor whose rule is one meaningful message per slide.

Here is the current slide content: [PASTE_SLIDES]
The audience is [AUDIENCE], the decision or learning goal is [GOAL], and the tone should be [TONE].

First, write the deck's current argument in one sentence. Then process each slide individually. Identify its strongest intended takeaway, rewrite the title as a complete message rather than a topic label, and retain only content that proves or explains that message. Put useful but nonessential material in a “move to notes” line. Mark repetition with the slide number where the idea already appears.

When a slide contains two indispensable messages, propose a split and name both new slides. When several slides make one weak point, recommend a merge. Do not compress text merely by making sentences vague, and do not alter numbers or factual meaning.

Present the result as a numbered rewrite map with: new headline, visible content, suggested visual, notes material, and action (keep/split/merge/remove). Conclude with the revised headline-only story and flag any logical jump where a new bridge slide or missing evidence is needed.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
