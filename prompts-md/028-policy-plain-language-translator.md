# 028 — Policy Plain-Language Translator

**Category:** documents · **Difficulty:** Intermediate

**Usage:** Use this to explain a policy clearly without weakening its actual requirements.

**Expected output:** A plain-language policy guide with duties, examples, exceptions, and traceability.

**Tip:** Have the policy owner verify every obligation after simplification.

## Best tools
- **ChatGPT**: Rewrites complex policy language for defined reading levels and audiences.
- **Claude**: Preserves cross-references and exceptions across long policy documents.

## Prompt

```text
Translate [POLICY_DOCUMENT] into a plain-language guide for [AUDIENCE] while preserving its rules and exceptions.

Target reading level: [READING_LEVEL]. Preferred language: [ENGLISH_URDU_OR_BILINGUAL]. Jurisdiction or organisation: [CONTEXT]. This is an explanation, not legal advice or a replacement for the official policy.

Begin with “What this policy is for” and “Who it applies to.” Then explain duties as direct questions: What must I do? What must I not do? When do I need approval? What happens if something goes wrong? Who can help? Attach each answer to the original clause or page.

Define technical terms at first use. Convert long sentences into short steps, but retain mandatory words such as must, may, and should with their different force. Use two realistic examples and one non-example for each high-risk rule. Clearly label exceptions and appeal or reporting routes.

Create a fidelity ledger listing any phrase that could not be simplified safely and why. Add [ORGANISATION TO CONFIRM] wherever the document is ambiguous or internally inconsistent.

Close with a one-page quick guide and five comprehension questions. Do not introduce new requirements, deadlines, penalties, or promises. Recommend review by the policy owner and, where necessary, a qualified adviser before publication.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
