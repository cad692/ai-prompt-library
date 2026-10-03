# 004 — Tone-Safe Email Rewriter

**Category:** assistants · **Difficulty:** Beginner

**Usage:** Use this to improve an email while preserving facts, intent, and your voice.

**Expected output:** Two polished email versions plus a brief explanation of tone choices.

**Tip:** Name the relationship and desired response; tone depends more on context than vocabulary.

## Best tools
- **ChatGPT**: Quickly rewrites short messages across professional tones while following constraints.
- **Claude**: Useful for preserving nuance and intent in sensitive correspondence.

## Prompt

```text
Rewrite my email as a careful communications editor while preserving every verified fact and my intended request.

Draft: [PASTE_EMAIL]
Recipient and relationship: [RECIPIENT_CONTEXT]
Desired outcome: [OUTCOME]
Tone: [WARM_DIRECT_FORMAL_DIPLOMATIC]
Cultural or workplace considerations: [CONSIDERATIONS]
Maximum length: [WORD_LIMIT]

Apply these non-negotiable constraints: do not invent dates, promises, attachments, titles, or reasons; do not add exaggerated praise; retain any necessary Urdu terms; and keep the request easy to answer. If the original sounds accusatory, remove blame without hiding the issue.

Produce Version A as the safest professional rewrite. Produce Version B as a slightly warmer alternative. For each, provide a subject line and complete email. Afterward, list no more than four important edits in the form “Changed X → Y because…”.

Check names, dates, pronouns, and the requested action against my draft. If an essential detail is absent, insert [CONFIRM DETAIL] rather than guessing. End with a one-line recommendation naming which version better suits [RECIPIENT_CONTEXT]. Avoid clichés such as “I hope this email finds you well” unless I explicitly request them.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
