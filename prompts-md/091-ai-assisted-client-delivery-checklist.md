# 091 — AI-Assisted Client Delivery Checklist

**Category:** workflows · **Difficulty:** Advanced

**Usage:** Create a controlled client-delivery process with transparent and reviewable AI assistance.

**Expected output:** A stage-gated checklist from intake through handover and retention.

**Tip:** Remove confidential identifiers before any tool not approved by the client.

## Best tools
- **Microsoft Copilot**: Supports documents, spreadsheets, email, and presentations in a connected work environment.

## Prompt

```text
You are my AI-Assisted Client Delivery checklist designer. Create a delivery checklist that uses AI safely without leaking client secrets or inventing work done.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Deliverable: [DELIVERABLE]
Client type: [CLIENT]
Delivery stages: [STAGES]
Where AI may help: [AI_USES]
Where AI is banned: [AI_BANS]
QA requirements: [QA]
Client assets: [ASSETS]
Deadline: [DEADLINE]
Risks: [RISKS]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent unverified facts, numbers, citations, or quotes.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Map
Map [STAGES] for [DELIVERABLE] toward [DEADLINE].

STEP 2 — AI policy
Allow [AI_USES] and enforce [AI_BANS] with confidentiality for [CLIENT] and [ASSETS].

STEP 3 — Checklist
Build a stage checklist with [QA] gates.

STEP 4 — Risks
Address [RISKS] and handoff notes.

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Delivery stages
B. Stage checklist
C. AI allow list
D. AI ban list
E. QA gates
F. Confidentiality rules
G. Risk controls
H. Client handoff checklist

Rules: confidentiality first; AI assists not invents delivery; human QA required.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
