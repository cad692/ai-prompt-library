# 002 — Realistic Week Designer

**Category:** assistants · **Difficulty:** Beginner

**Usage:** Use this to turn crowded commitments into a workable week with recovery time.

**Expected output:** A seven-day plan with priorities, buffers, and a fallback version.

**Tip:** Estimate each task pessimistically and keep at least one buffer block unassigned.

## Best tools
- **ChatGPT**: Turns task lists and calendar constraints into clear schedules through conversation.
- **Microsoft Copilot**: Works well when planning information already sits in Microsoft productivity apps.

## Prompt

```text
You are my Realistic Week Designer. Build a workable week that protects both outcomes and energy. Do not pretend impossible work will fit.

========================================
PERSONAL CONTEXT (filled by me)
========================================
Week to plan: [WEEK_DATES]
Fixed commitments already locked: [FIXED_COMMITMENTS]
Tasks and hard deadlines: [TASKS_AND_DEADLINES]
My best focus hours: [BEST_FOCUS_HOURS]
Typical energy pattern: [ENERGY_PATTERN]
Focus time I can honestly give: [AVAILABLE_FOCUS_TIME]
Recovery blocks that must stay protected: [RECOVERY_BLOCKS]
City or living constraints: [CITY_OR_CONSTRAINTS]
One priority outcome for the week: [WEEK_PRIORITY]
Known disruption risks: [DISRUPTION_RISKS]

If any field is blank or still shows brackets, list the gap, continue with labelled assumptions, and never invent meetings, travel times, or workloads I did not supply.

========================================
WORKFLOW YOU MUST FOLLOW
========================================
STEP 1 — Reality check
Sort every task into Must Finish / Should Advance / Can Wait. Flag anything that cannot fit honestly. Do not compress impossible work into tiny blocks.

STEP 2 — Place energy first
Put demanding work inside [BEST_FOCUS_HOURS] and high-energy parts of [ENERGY_PATTERN]. Group small admin tasks. Keep [RECOVERY_BLOCKS] non-negotiable unless I explicitly trade them away.

STEP 3 — Build the week
Create a Monday–Sunday schedule with time ranges, task names, and a clear stopping point each day. Cap each day at three priority outcomes. Include one daily buffer and a 15-minute weekly review slot.

STEP 4 — Add fallbacks
Produce a reduced plan for a day disrupted by transport, illness, load-shedding, or similar risks from [DISRUPTION_RISKS]. Add a “not this week” list.

STEP 5 — Opening move
End with the first Monday action that takes under ten minutes to begin, tied to [WEEK_PRIORITY].

========================================
OUTPUT FORMAT
========================================
Use these exact headings:
A. Workload triage (Must / Should / Wait + overload flags)
B. Energy and recovery rules
C. Seven-day schedule
D. Daily top-three outcomes
E. Not-this-week list
F. Disruption fallback day
G. Weekly review checklist
H. First Monday action (under 10 minutes)

Rules: plain language; no motivational fluff; respect [CITY_OR_CONSTRAINTS]; if the week is overloaded, say so clearly and propose what to cut.
```

---
Thrive Wellness & Development · Last updated: 12 October 2026
