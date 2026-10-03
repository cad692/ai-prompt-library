# 031 — RTCFCE Prompt Architect

**Category:** prompting · **Difficulty:** Intermediate

**Usage:** Use this to convert a rough task into a complete RTCFCE prompt.

**Expected output:** A completed RTCFCE worksheet and a ready-to-run prompt.

**Tip:** Use a role only when expertise or viewpoint changes how the task should be done.

## Best tools
- **ChatGPT**: Supports interactive prompt design and clearly explains structural choices.
- **Claude**: Follows detailed prompt specifications and handles rich context well.

## Prompt

```text
Act as an RTCFCE prompt architect helping me turn [ROUGH_TASK] into a precise, reusable instruction.

Do not fill gaps immediately. Interview me one question at a time about Role, Task, Context, Format, Constraints, and Examples. Ask only questions whose answers could materially change the result, with a maximum of eight. If a role adds no value, recommend omitting it. Wait for my replies before building the prompt.

After the interview, create an RTCFCE worksheet:
R — useful expertise or perspective;
T — exact action and success condition;
C — audience, background, inputs, and purpose;
F — output shape and length;
C — hard limits, safety, tone, and exclusions;
E — one positive example or pattern, plus a counterexample if helpful.

Label any assumption you still need to make. Then assemble a natural prompt rather than mechanically repeating the six headings. Put the most important goal in its opening line and represent reusable inputs as [PLACEHOLDERS].

Provide a compact version and a detailed version. Explain when each is preferable. Finally, simulate one likely model misunderstanding, identify which RTCFCE element failed to prevent it, and patch only that section. The final prompt should be vendor-neutral and should not request hidden chain-of-thought.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
