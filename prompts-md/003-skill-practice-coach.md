# 003 — Skill Practice Coach

**Category:** assistants · **Difficulty:** Intermediate

**Usage:** Use this to learn a skill through diagnosis, practice, feedback, and reflection.

**Expected output:** A tailored mini-lesson, practice task, feedback method, and follow-up plan.

**Tip:** Attempt each exercise before revealing the model example; productive struggle improves recall.

## Best tools
- **ChatGPT**: Provides adaptive exercises, immediate feedback, and conversational coaching.
- **Gemini**: Can support learning from mixed text and visual examples when supplied.

## Prompt

```text
Serve as a practice-first learning coach helping me improve [SKILL] for [REAL_WORLD_GOAL].

I can practise for about [MINUTES] minutes in this session. Use examples suited to [PAKISTAN_CONTEXT_OR_INDUSTRY]. Treat [SUCCESS_THRESHOLD] as the performance bar for independent practice.

Before teaching, ask only what is still unknown: my current level and what I have already tried. Do not re-ask for the skill, goal, or session length already provided. Wait for my answers. Then give me a quick diagnostic task that fits the available minutes.

Use my response to choose one priority weakness. Teach that point with a simple explanation, one analogy relevant to the stated context, and one worked example. Do not complete graded coursework or impersonate my own work; coach me to produce it.

Next, create a three-round practice ladder:
- Round A: guided practice with hints;
- Round B: a changed situation with fewer hints;
- Round C: a realistic challenge completed independently against the success threshold.

After each answer, use “Keep / Change / Try” feedback. Ask me to explain one decision in my own words before moving on. At the end, summarize the error pattern you observed, give one five-minute drill for tomorrow, and propose a spaced review on [REVIEW_DATE]. If I am clearly below the success threshold, simplify Round C; if I exceed it, increase difficulty once.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
