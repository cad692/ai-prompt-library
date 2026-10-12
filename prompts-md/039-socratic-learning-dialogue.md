# 039 — Socratic Learning Dialogue

**Category:** prompting · **Difficulty:** Intermediate

**Usage:** Use this to create a tutor prompt that guides learning through questions.

**Expected output:** An adaptive Socratic tutor prompt with hint levels and learning checks.

**Tip:** Require the tutor to wait after every question; otherwise it may answer itself.

## Best tools
- **ChatGPT**: Maintains responsive multi-turn tutoring and adjusts hints to learner answers.
- **Gemini**: Supports conversational explanation and varied examples across subjects.

## Prompt

```text
You are my Socratic Learning Dialogue designer. Create a tutor prompt that guides learning through questions, not answer dumps.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Topic to teach: [TOPIC]
Learner level: [LEARNER_LEVEL]
Learning goal: [GOAL]
Session length in minutes: [SESSION_MINUTES]
Known gaps or misconceptions: [KNOWN_GAPS]
How quickly to give hints: [HINT_POLICY]
What counts as understanding: [SUCCESS_CHECK]
Local or course context: [CONTEXT]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Tutor stance
Define a Socratic stance for [TOPIC] at [LEARNER_LEVEL] aimed at [GOAL].

STEP 2 — Dialogue flow
Plan question ladders, hint tiers per [HINT_POLICY], and checks for [KNOWN_GAPS].

STEP 3 — Ready tutor prompt
Write the reusable tutor prompt including wait-for-learner rules and [SESSION_MINUTES] pacing.

STEP 4 — Exit test
Include a final check aligned to [SUCCESS_CHECK] in [CONTEXT].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Tutor stance
B. Question ladder
C. Hint tiers
D. Misconception handling
E. Ready tutor prompt
F. Pacing plan
G. Success check
H. If learner is stuck

Rules: ask before telling; no completing graded work; keep curiosity kind and rigorous.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
