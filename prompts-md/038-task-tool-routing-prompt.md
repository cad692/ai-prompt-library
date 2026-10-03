# 038 — Task Tool Routing Prompt

**Category:** prompting · **Difficulty:** Beginner

**Usage:** Use this to choose an appropriate AI tool based on task capabilities.

**Expected output:** A capability-based recommendation with alternatives, limitations, and a test task.

**Tip:** Choose by required capability and data sensitivity before considering familiarity.

## Best tools
- **ChatGPT**: Can elicit requirements and compare tools across common general-purpose capabilities.
- **Perplexity**: Useful when tool selection depends on current, source-linked capability information.

## Prompt

```text
Help me choose the most suitable AI tool for [TASK] based on capabilities, access, and risk—not popularity.

My inputs are [TEXT_FILES_IMAGES_LINKS_OR_OTHER], expected output is [OUTPUT], workflow is [WORKFLOW], data sensitivity is [PUBLIC_INTERNAL_CONFIDENTIAL], and devices or accounts available are [ACCESS]. I prefer [PREFERENCES], but they are not hard requirements.

Ask up to five clarifying questions if any decisive requirement is missing. Then create a capability checklist covering current web access, citations, file type and length, multimodal input, office integration, collaboration, privacy controls, and required human verification.

Compare only tools you can describe accurately from current knowledge or verifiable official information. Candidate tools may include ChatGPT, Gemini, Claude, Perplexity, NotebookLM, DeepSeek, Meta AI, and Microsoft Copilot; omit irrelevant ones. Do not discuss prices unless I explicitly ask, and do not claim a feature exists without confidence.

Recommend one primary tool and up to two alternatives. For each, state task fit, key limitation, and the condition that would change the choice. If a simple non-AI tool is safer or sufficient, say so.

End with a ten-minute test task using non-sensitive sample data and a scorecard for accuracy, effort, traceability, and fit. Remind me to verify availability and organisational policy before uploading data.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
