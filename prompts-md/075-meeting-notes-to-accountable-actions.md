# 075 — Meeting Notes to Accountable Actions

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to convert messy meeting notes into decisions, tasks, and open questions.

**Expected output:** A decision log, action register, and concise follow-up message.

**Tip:** Send the action list within the same day while context is fresh.

## Best tools
- **Notion**: Stores meeting records and links actions to team workflows.
- **ChatGPT**: Separates decisions, actions, and unresolved issues from raw notes.

## Prompt

```text
Act as a precise meeting secretary turning rough notes into accountable follow-through without filling gaps from imagination.

Meeting notes or transcript: [NOTES]
Meeting purpose: [PURPOSE]
Participant names and roles: [PARTICIPANTS]
Project context: [CONTEXT]

Separate the material into five buckets: decisions made, action items, open questions, risks or blockers, and contextual discussion. A decision must state what was agreed and, if present, why. An action must begin with a verb and include owner, deliverable, due date, dependency, and completion evidence. If any field was not explicitly agreed, write [CONFIRM] rather than assigning it.

Detect conflicting statements, tentative language, and decisions that appear to have been reopened later in the meeting. Quote a short source phrase beside ambiguous items so participants can resolve them. Exclude conversational filler and do not transform every suggestion into a task.

Produce a compact decision log followed by the action register in priority order. Add an “awaiting confirmation” section and a parking-lot list. Finish with a neutral follow-up message that summarizes the top decisions, asks owners to confirm actions, and names the next checkpoint. Preserve sensitive material only if it is necessary for execution.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
