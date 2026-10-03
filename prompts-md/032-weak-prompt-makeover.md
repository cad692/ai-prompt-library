# 032 — Weak Prompt Makeover

**Category:** prompting · **Difficulty:** Beginner

**Usage:** Use this to see exactly how a vague prompt becomes specific and testable.

**Expected output:** An annotated before-and-after prompt with a reusable lesson.

**Tip:** Improve the missing information that affects success; extra words alone do not improve a prompt.

## Best tools
- **ChatGPT**: Provides clear prompt rewrites and demonstrates their likely output differences.
- **Gemini**: Generates varied reformulations and explains practical prompt improvements.

## Prompt

```text
Diagnose and improve this weak prompt as a practical prompt-writing teacher: [WEAK_PROMPT].

The intended outcome is [OUTCOME], the user is [USER], and the output will be used for [USE]. Preserve the legitimate goal; do not quietly change the task or add requirements unsupported by me.

Start by marking the original prompt with inline labels for five possible weaknesses: vague action, missing context, undefined audience, absent output format, and untestable quality words. If a category is already strong, say so.

Create three successive rewrites:
Version 1 — Minimal Repair: change as little as possible.
Version 2 — Reliable Prompt: add necessary context, constraints, and output shape.
Version 3 — Reusable Template: replace variable details with [PLACEHOLDERS].

Under each version, explain the likely change in output using one short “because” statement. Show a tiny mock output fragment—not a full completion—to make the difference visible.

Then run a deletion test on Version 2: remove one instruction that does not materially affect success, or state that every instruction earns its place. End with a three-rule lesson tailored to the original weaknesses and one challenge asking me to revise a second prompt myself.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
