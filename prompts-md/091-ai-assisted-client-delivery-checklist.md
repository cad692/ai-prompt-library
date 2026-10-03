# 091 — AI-Assisted Client Delivery Checklist

**Category:** workflows · **Difficulty:** Advanced

**Usage:** Create a controlled client-delivery process with transparent and reviewable AI assistance.

**Expected output:** A stage-gated checklist from intake through handover and retention.

**Tip:** Remove confidential identifiers before any tool not approved by the client.

## Best tools
- **Microsoft Copilot**: Supports documents, spreadsheets, email, and presentations in a connected work environment.

## Prompt

```text
Role: Operate as a client-delivery quality manager; build a checklist for [SERVICE] from signed brief to final handover.

Account for [CLIENT_REQUIREMENTS], [DELIVERABLES], [DEADLINE], and [APPROVED_AI_TOOLS]. Divide the workflow into intake, scope confirmation, source collection, production, internal review, client review, revision control, delivery, and closeout. At each stage, identify where AI can assist and where a named human must decide.

Provide checklist items for consent, data classification, redaction, prompt logging if required, factual verification, accessibility, brand compliance, and version naming. Include a stop condition when confidential data, unclear ownership, or out-of-scope requests appear. Generated work must never be described as independently verified.

Define the handoff artifact between tools—such as a sanitised brief, draft document, issue log, or approved PDF—and who accepts it. Add a change-request route that records impact on timeline and scope.

Finish with a delivery manifest listing files, versions, approvals, unresolved limitations, and retention or deletion actions. Make the checklist usable in [PROJECT_PLATFORM].
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
