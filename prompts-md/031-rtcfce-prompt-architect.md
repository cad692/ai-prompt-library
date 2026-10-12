# 031 — RTCFCE Prompt Architect

**Category:** prompting · **Difficulty:** Intermediate

**Usage:** Use this to convert a rough task into a complete RTCFCE prompt (Role, Task, Context, Format, Constraints, and Examples).

**Expected output:** A completed RTCFCE worksheet and a ready-to-run prompt.

**Tip:** Use a role only when expertise or viewpoint changes how the task should be done.

## Best tools
- **ChatGPT**: Supports interactive prompt design and clearly explains structural choices.
- **Claude**: Follows detailed prompt specifications and handles rich context well.

## Prompt

```text
You are my RTCFCE Prompt Architect. Convert a rough task into a complete prompt using Role, Task, Context, Format, Constraints, Examples.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Rough task description: [ROUGH_TASK]
Intended AI tool: [AI_TOOL]
End user of the AI output: [END_USER]
Success looks like: [SUCCESS_LOOKS_LIKE]
Hard constraints: [HARD_CONSTRAINTS]
Tone or voice needed: [TONE]
Examples I can provide: [EXAMPLE_SEEDS]
Risks to avoid: [RISKS_TO_AVOID]
Output length target: [LENGTH_TARGET]

If examples are thin, create labelled placeholder example slots rather than fake domain facts.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Diagnose the rough ask
Name what is vague, missing, or risky in [ROUGH_TASK].

STEP 2 — Build RTCFCE
Fill Role, Task, Context, Format, Constraints, Examples aligned to [AI_TOOL], [END_USER], and [SUCCESS_LOOKS_LIKE].

STEP 3 — Stress constraints
Encode [HARD_CONSTRAINTS], [TONE], [LENGTH_TARGET], and [RISKS_TO_AVOID] as enforceable rules.

STEP 4 — Deliver ready-to-paste prompt
Provide the final prompt plus a short test checklist.

========================================
OUTPUT FORMAT
========================================
A. Diagnosis of the rough task
B. RTCFCE breakdown
C. Ready-to-paste final prompt
D. Example slots
E. Failure modes guarded against
F. Quick test checklist
G. Optional tighter variant
H. What I still need from you

Rules: specific; testable; no fake examples presented as real.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
