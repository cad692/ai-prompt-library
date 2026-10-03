# 022 — Agreement Risk Spotter

**Category:** documents · **Difficulty:** Advanced

**Usage:** Use this to spot contract clauses worth discussing with a qualified lawyer.

**Expected output:** A non-legal risk summary with clause references and lawyer questions.

**Tip:** Upload every schedule and annexure; key obligations are often outside the main document.

## Best tools
- **Claude**: Reviews lengthy agreements and tracks definitions across clauses.
- **ChatGPT**: Explains dense provisions in plain language and organises follow-up questions.

## Prompt

```text
Review [UPLOADED_AGREEMENT] as a plain-language issue spotter, not as a lawyer or substitute for legal advice.

I am the [PARTY_ROLE], the agreement concerns [PURPOSE], and the relevant jurisdiction appears to be [JURISDICTION]. My priorities are [PRIORITIES]. State clearly that enforceability and legal rights require advice from a qualified lawyer familiar with the applicable law.

Start with a deal snapshot: parties, term, payment, renewal, termination, and main obligations, each linked to clause or page numbers. Then create a red-flag register using severity—urgent, important, or monitor—for:
liability and indemnity; unilateral changes; intellectual property; confidentiality; data use; non-compete or exclusivity; payment and penalties; termination; dispute resolution; governing law; warranties; and missing schedules.

For every flag, quote only the minimum relevant wording, explain the practical effect in neutral language, identify who bears the risk, and draft one clarification or negotiation question. Do not declare a clause illegal or enforceable.

Add a cross-reference check for inconsistent definitions, dates, amounts, and annexures. List obligations due in the first 30 days. Finish with “Questions for a Pakistani lawyer” tailored to [JURISDICTION] and a missing-information list. Mask CNIC numbers, bank details, signatures, and personal addresses in your output.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
