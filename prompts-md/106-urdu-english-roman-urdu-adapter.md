# 106 — Urdu, English, and Roman Urdu Adapter

**Category:** pakistan · **Difficulty:** Intermediate

**Usage:** Adapt one message across Urdu, English, and Roman Urdu while preserving intent and register.

**Expected output:** Three aligned language versions plus notes on ambiguity and terminology.

**Tip:** Have a fluent human review public-facing Urdu and names written in Urdu script.

## Best tools
- **ChatGPT**: Can compare multilingual phrasing and explain register choices in context.

## Prompt

```text
You are my Urdu/English/Roman-Urdu Adapter. Adapt a message across Urdu, English, and Roman Urdu while preserving meaning and respect.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Source text: [SOURCE_TEXT]
Source language: [SOURCE_LANG]
Target variants needed: [TARGETS]
Audience: [AUDIENCE]
Formality: [FORMALITY]
Must-keep terms: [MUST_KEEP]
Channel: [CHANNEL]
Sensitivity notes: [SENSITIVITY]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Meaning
Lock meaning from [SOURCE_TEXT] before adapting.

STEP 2 — Adapt
Produce [TARGETS] at [FORMALITY] for [AUDIENCE] and [CHANNEL], preserving [MUST_KEEP].

STEP 3 — Check
Flag untranslatable nuances and [SENSITIVITY] risks.

STEP 4 — Pick
Recommend which variant to send when.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Meaning lock
B. English version
C. Urdu version
D. Roman Urdu version
E. Terms preserved
F. Nuance warnings
G. Channel recommendation
H. QA checklist

Rules: meaning-faithful; no offensive shifts; mark uncertain translations.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
