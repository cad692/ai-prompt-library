# 033 — Grounded Answer Guardrails

**Category:** prompting · **Difficulty:** Advanced

**Usage:** Use this to design prompts that reduce unsupported claims and invented details.

**Expected output:** A hallucination-resistant prompt with evidence rules and adversarial tests.

**Tip:** Require an abstention phrase and source locations, then test the prompt with an unanswerable question.

## Best tools
- **NotebookLM**: Grounds responses in user-provided sources and exposes supporting source locations.
- **Claude**: Follows detailed evidence constraints across long source material.

## Prompt

```text
You are my Grounded Answer Guardrails designer. Design prompt rules that reduce unsupported claims and invented details.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Task the AI will perform: [TASK_TYPE]
Sources the AI may use: [ALLOWED_SOURCES]
Behaviours to forbid: [FORBIDDEN_BEHAVIOURS]
How evidence must be shown: [CITATION_RULE]
How to mark unknowns: [UNCERTAINTY_RULE]
Audience for answers: [AUDIENCE]
Risk if the AI invents facts: [RISK_LEVEL]
Sample user query to protect: [SAMPLE_QUERY]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Threat model
List how the AI might invent or overclaim on [TASK_TYPE] given [RISK_LEVEL].

STEP 2 — Guardrail pack
Write enforceable rules for sources, refusals, citations, and uncertainty using my fields.

STEP 3 — Ready prompt
Produce a ready-to-paste system/user prompt pair that embeds the guardrails.

STEP 4 — Test cases
Give pass/fail test queries including [SAMPLE_QUERY].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Invention risks
B. Guardrail rules
C. Ready-to-paste prompt
D. Citation behaviour
E. Uncertainty behaviour
F. Pass/fail tests
G. Escape hatches to avoid
H. Review checklist

Rules: prefer refusal or labelled uncertainty over fiction; honour [ALLOWED_SOURCES] and [FORBIDDEN_BEHAVIOURS].
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
