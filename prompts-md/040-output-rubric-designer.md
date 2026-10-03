# 040 — Output Rubric Designer

**Category:** prompting · **Difficulty:** Advanced

**Usage:** Use this to define measurable criteria for evaluating an AI-generated output.

**Expected output:** A weighted rubric with anchors, failure gates, and a calibration exercise.

**Tip:** Weight factuality and safety separately from style so polished errors cannot score highly.

## Best tools
- **ChatGPT**: Builds task-specific rubrics and applies them iteratively to sample outputs.
- **Claude**: Provides nuanced criterion definitions and evidence-based evaluations of long outputs.

## Prompt

```text
Design an evaluation rubric for AI-generated [OUTPUT_TYPE] used by [AUDIENCE] for [PURPOSE].

Success requirements are [REQUIREMENTS], likely risks are [RISKS], and sample outputs if available are [SAMPLES]. Begin by separating threshold requirements from quality dimensions. A threshold is pass/fail—such as no invented citations—while a quality dimension can improve by degree.

Propose five to eight non-overlapping criteria. For each provide: definition, weight, evidence the evaluator should inspect, and anchors for scores 1, 3, and 5. Ensure weights total 100. Include accuracy, source grounding, or safety where relevant; do not allow fluency to compensate for dangerous or materially false content.

Add automatic failure gates for [CRITICAL_FAILURES]. Define how “not applicable” changes the denominator. Write instructions for two evaluators to resolve disagreements by pointing to output evidence rather than personal taste.

Calibrate the rubric on [SAMPLE_A] and [SAMPLE_B], if supplied. Show criterion scores with short justifications, identify any criterion that both samples expose as ambiguous, and revise its wording once. If no samples are supplied, create two tiny synthetic fragments solely for calibration.

Finish with a compact evaluator form and interpretation bands—unusable, needs revision, usable with checks, strong—tied to both score and failure gates. State what the rubric cannot measure and when a subject-matter expert must override the numeric result.
```

---
Thrive Wellness & Development · Last updated: 3 October 2026
