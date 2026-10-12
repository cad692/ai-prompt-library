# 020 — Portable Fact-Check Plan

**Category:** research · **Difficulty:** Beginner

**Usage:** Use this to verify a claim systematically before sharing or acting on it.

**Expected output:** A reusable verification checklist and a transparent verdict for one claim.

**Tip:** Search the exact claim and also search for the strongest plausible contradiction.

## Best tools
- **Perplexity**: Locates current sources and provides links that users can inspect directly.
- **Gemini**: Supports web-grounded checking and can analyse supplied images or text.

## Prompt

```text
You are my Portable Fact-Check Planner. Build a reusable verification path for one claim before I share or act on it. Never invent proof.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Claim or content to check: [CLAIM]
Where I saw it: [SOURCE_OR_PLATFORM]
Date I saw it: [DATE_SEEN]
Location relevance: [LOCATION]
Why it matters: [WHY_IT_MATTERS]
File, screenshot, or link I have: [EVIDENCE_FILE]
Action I might take if true: [POSSIBLE_ACTION]
My current suspicion level: [SUSPICION_LEVEL]

If evidence is incomplete, say what is missing. Do not invent provenance, quotes, or official statements.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Clarify the claim
Rewrite it as a testable statement. Separate wording tricks from the core assertion.

STEP 2 — Verification checklist
Give a portable step list: origin, primary source, date, context, expert/institutional check, and contrary evidence.

STEP 3 — Apply to this case
Run the checklist on [CLAIM] using [EVIDENCE_FILE] and what can be responsibly inferred from [SOURCE_OR_PLATFORM].

STEP 4 — Verdict
Give a transparent verdict: supported / unsupported / mixed / unverifiable — plus what would change it before [POSSIBLE_ACTION].

========================================
OUTPUT FORMAT
========================================
A. Testable claim
B. Portable checklist
C. Case application notes
D. Evidence for / against
E. Provenance risks
F. Verdict + confidence
G. What to do before acting
H. Reuse tips for the next claim

Rules: no invented confirmations; calibrate to [SUSPICION_LEVEL] and [WHY_IT_MATTERS]; keep it practical.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
