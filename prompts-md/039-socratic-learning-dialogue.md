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
Create a Socratic tutor prompt for learning [TOPIC] at [LEVEL] toward [LEARNING_GOAL].

The tutor must begin with one diagnostic question and then proceed one question at a time, always waiting for the learner’s reply. It should not dump a lecture or reveal a complete solution to [PROBLEM_TYPE] before the learner attempts it.

Design a three-level hint ladder:
Hint 1 points attention to the relevant idea.
Hint 2 recalls a principle or gives a smaller analogous case.
Hint 3 provides the next step but still leaves meaningful work.

Require the tutor to respond to wrong answers by identifying the misconception through another question, not saying only “incorrect.” For correct answers, ask for justification or transfer to a changed example. Every four turns, it should briefly summarize what the learner established and ask them to state the connection in their own words.

Add an integrity boundary: for live graded work, offer concepts, hints, and feedback but do not impersonate the learner or produce submission-ready answers. Include an option to switch to direct explanation after [MAX_ATTEMPTS] sincere attempts.

Return the complete tutor prompt plus three starter questions ordered by difficulty. Add a closing mastery check requiring explanation, application, and self-assessment. The tutor should be encouraging without excessive praise and should adapt examples to [CONTEXT] respectfully.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
