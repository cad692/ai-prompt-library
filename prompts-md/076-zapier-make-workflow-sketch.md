# 076 — Zapier or Make Workflow Sketch

**Category:** data-productivity · **Difficulty:** Beginner

**Usage:** Use to map an automation before connecting live accounts or customer data.

**Expected output:** A workflow map with fields, branches, safeguards, and test cases.

**Tip:** Test with fake records before granting access to production accounts.

## Best tools
- **Zapier/Make**: Connects supported apps through triggers, actions, filters, and branching.
- **Notion**: Documents the automation specification, test cases, and ownership.

## Prompt

```text
Work as an automation architect sketching the logic before anyone connects production systems.

Desired outcome: [OUTCOME]
Triggering app and event: [TRIGGER]
Source fields: [SOURCE_FIELDS]
Destination apps and actions: [DESTINATIONS]
Conditions or approvals: [CONDITIONS]
Expected volume and urgency: [VOLUME]
Sensitive data: [SENSITIVE_DATA]

Map the workflow as numbered nodes: trigger, validation, lookup, transformation, filter, branch, action, confirmation, and logging. Use only the node types actually required. At each node, list input fields, output fields, matching key, required condition, and what happens if data is blank, duplicated, malformed, delayed, or rejected.

Compare a Zapier-style linear design with a Make-style scenario when branching or iteration is involved, but do not claim a connector or feature exists unless the user confirms it. Identify human approval points for payments, public messages, record deletion, or consequential decisions.

Add safeguards for least-privilege access, test data, idempotency, duplicate prevention, rate limits, retry behavior, error notification, audit log, and manual recovery. Provide five test cases including happy path, duplicate, missing field, app outage, and unauthorized value. Finish with implementation order, owner, monitoring cadence, and a rollback switch. Never place passwords or API keys in the specification.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
