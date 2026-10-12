# 083 — Gmail Context-Aware Draft

**Category:** addins · **Difficulty:** Beginner

**Usage:** Draft a clear Gmail reply grounded in the thread and the sender's actual request.

**Expected output:** A concise email draft with subject, action, and verification flags.

**Tip:** Recheck recipients, attachments, dates, and promises before pressing Send.

## Best tools
- **Gemini in Gmail**: Uses the open email thread as context for drafting and summarising.

## Prompt

```text
You are my Gmail Context-Aware Draft coach. Draft a Gmail message that fits thread context and relationship. Do not invent prior promises.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Thread or context: [THREAD_CONTEXT]
Email goal: [GOAL]
Recipient relationship: [RECIPIENT]
Must-include points: [MUST_INCLUDE]
Tone: [TONE]
Length: [LENGTH]
Call to action: [CTA]
Things to avoid: [AVOID]
Deadline if any: [DEADLINE]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Context
Extract relevant context from [THREAD_CONTEXT] without inventing history.

STEP 2 — Draft
Write a Gmail-ready draft for [GOAL], [RECIPIENT], [TONE], and [LENGTH] including [MUST_INCLUDE] and [CTA].

STEP 3 — Safety
Remove [AVOID] issues; surface [DEADLINE] clearly.

STEP 4 — Alt
Provide a shorter variant.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Context used
B. Subject line options
C. Main draft
D. Shorter variant
E. CTA clarity
F. Assumptions labelled
G. Avoid list applied
H. Send checklist

Rules: context-faithful; easy reply; no fabricated commitments.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
