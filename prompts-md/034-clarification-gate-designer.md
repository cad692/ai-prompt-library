# 034 — Clarification Gate Designer

**Category:** prompting · **Difficulty:** Intermediate

**Usage:** Use this to make an AI ask important questions before attempting the task.

**Expected output:** A two-stage prompt with a strict clarification gate and fallback assumptions.

**Tip:** Tell the model to ask only decision-changing questions, or the intake can become tedious.

## Best tools
- **ChatGPT**: Handles multi-turn clarification and adapts later output to user responses.
- **Claude**: Maintains detailed answers from an intake phase through final delivery.

## Prompt

```text
Create a two-stage clarification-gate prompt for [TASK] so the model cannot rush into an answer.

The minimum information needed is [REQUIRED_INPUTS]. Optional helpful context is [OPTIONAL_INPUTS]. The user may have limited time, so questions must be high value and easy to answer.

Stage One must instruct the model to inspect the request, identify only gaps that could materially alter the output, and ask up to [MAX_QUESTIONS] numbered questions in one message. It must not draft, outline, research, or solve the task yet. Include “Why I need this” after each question in eight words or fewer. Offer selectable options when users may not know the terminology.

Define a gate condition: Stage Two begins only after the user responds or explicitly says “Use reasonable assumptions.” If assumptions are authorised, they must be listed before work begins and must avoid sensitive personal, legal, medical, or financial guesses.

Stage Two should restate the agreed requirements as a compact brief, invite one correction, and then produce [OUTPUT_FORMAT] under [CONSTRAINTS].

Test the resulting prompt against two cases: a complete request that needs no questions and a vague request missing three essentials. Show expected model behaviour, not the task answer. Finish with one escape hatch for users who want a quick draft and a warning label for high-stakes use.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
