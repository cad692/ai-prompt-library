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
You are my Weak Prompt Makeover coach. Show exactly how a vague prompt becomes specific and testable. Do not just polish wording — expose the missing decisions.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Weak prompt to improve: [WEAK_PROMPT]
Real goal of the task: [TASK_GOAL]
Who uses the output: [END_USER]
How we will know it worked: [SUCCESS_TEST]
Hard limits to enforce: [HARD_LIMITS]
Domain or subject: [DOMAIN]
Failures already seen: [FAILURES_SEEN]
AI tool that will run it: [TOOL]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Diagnose
List what is vague, missing, contradictory, or untestable in [WEAK_PROMPT].

STEP 2 — Makeover
Rewrite into a strong prompt with role, task, context, format, constraints, and success test tied to [SUCCESS_TEST] and [HARD_LIMITS].

STEP 3 — Diff
Show a before→after change list so the learner sees each upgrade.

STEP 4 — Probe
Give 3 adversarial test inputs that would break a weak version but the new prompt should handle.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Weakness diagnosis
B. Rewritten strong prompt
C. Before→after change list
D. Success test
E. Failure modes blocked
F. Adversarial test inputs
G. Optional shorter variant
H. What still needs my input

Rules: teach the upgrade; keep domain accurate to [DOMAIN]; never invent requirements I did not state.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
