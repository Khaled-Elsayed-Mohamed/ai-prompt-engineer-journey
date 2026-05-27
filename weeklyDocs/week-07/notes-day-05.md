# 🔨 Week 7 · Day 5 — Build the LLM-as-Judge Evaluator Prompt

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Build a second prompt that evaluates the quality of classifier outputs — specifically targeting correctness, confidence calibration, and reason quality.

---

## What the Evaluator Needs to Assess

From the Day 3 results, I know the failure modes:
1. **Wrong category** — the hard failure (Input 13)
2. **Overclaimed confidence** — the model is too certain on ambiguous inputs (Inputs 9, 15)
3. **Reason inaccuracy** — the reason doesn't accurately explain the classification

The evaluator prompt needs to check all three, independently.

---

## The Evaluator Prompt

```
You are an evaluator for a customer message classifier. Your job is to assess whether the classifier's output is correct and well-calibrated.

You will be given:
1. The original customer message
2. The classifier's output (category, confidence, reason)
3. The expected category

Assess the output on three dimensions and return a JSON object:

{
  "category_correct": true or false,
  "confidence_appropriate": "appropriate", "overclaimed", or "underclaimed",
  "reason_accurate": true or false,
  "overall": "pass", "partial", or "fail",
  "notes": "One sentence explaining any issues found, or 'No issues' if all dimensions pass"
}

CONFIDENCE CALIBRATION RULES:
- "high" confidence is appropriate when the message unambiguously maps to one category
- "high" confidence is overclaimed when the message could reasonably belong to 2+ categories
- "medium" confidence is appropriate for genuinely ambiguous messages
- "low" confidence is appropriate when the message barely maps to any category

OVERALL GRADING:
- pass: category correct + confidence appropriate + reason accurate
- partial: category correct but confidence overclaimed/underclaimed OR reason partially inaccurate
- fail: category incorrect

CUSTOMER MESSAGE: {{message}}
EXPECTED CATEGORY: {{expected_category}}
CLASSIFIER OUTPUT: {{classifier_output}}
```

---

## Running the Evaluator on All 20 Outputs

Ran all 20 classifier outputs through the evaluator. The evaluator's verdicts:

| # | Evaluator Verdict | Matches My Grade? |
|---|------------------|-----------------|
| 1–8 | Pass × 8 | ✅ Yes |
| 9 | Partial (confidence overclaimed) | ✅ Yes |
| 10–12 | Pass × 3 | ✅ Yes |
| 13 | Fail (wrong category) | ✅ Yes |
| 14 | Pass | ✅ Yes |
| 15 | Partial (confidence overclaimed) | ✅ Yes |
| 16–20 | Pass × 5 | ✅ Yes |

**Agreement rate between my manual grading and the LLM judge: 20/20 (100%).**

---

## What the Notes Field Added

For Input 9, the evaluator returned:
> "Category is correct (account) but confidence is overclaimed — 'I want to cancel my subscription' could be an account action or a complaint escalation, making medium confidence more appropriate."

For Input 13, the evaluator returned:
> "Category is incorrect — 'billing address' is an account setting, not a payment or billing issue. Expected: account."

Both explanations are accurate and more detailed than I would have written manually. The notes field is genuinely useful for debugging.

---

## Observation: The Evaluator Is a Spec Document

Writing the evaluator prompt forced me to define the grading criteria precisely — the confidence calibration rules in particular. Those rules now exist as a written spec, not just intuition in my head.

If I hand this project to someone else, they can run the evaluator without asking me what "overclaimed confidence" means. That's the hidden value of LLM-as-judge: it externalises the rubric.

---

## Tomorrow

Write the full evaluation report.
