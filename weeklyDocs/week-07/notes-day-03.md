# 🔨 Week 7 · Day 3 — Run and Grade All 20 Inputs

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Run all 20 test inputs through the classifier, grade every output against expected results, document the one failure.

---

## Grading Rubric

For each input, I graded three things:

- **Category correct?** Yes / No
- **Confidence appropriate?** Yes / Overclaimed / Underclaimed
- **Reason accurate?** Yes / Partially / No

An output needs all three to be a full Pass. Category correct but confidence overclaimed = Partial.

---

## Results

| # | Category | Confidence | Reason | Grade |
|---|----------|-----------|--------|-------|
| 1 | ✅ billing | ✅ high | ✅ | Pass |
| 2 | ✅ technical_support | ✅ high | ✅ | Pass |
| 3 | ✅ billing | ✅ high | ✅ | Pass |
| 4 | ✅ sales | ✅ high | ✅ | Pass |
| 5 | ✅ complaint | ✅ high | ✅ | Pass |
| 6 | ✅ account | ✅ high | ✅ | Pass |
| 7 | ✅ billing | ✅ high | ✅ | Pass |
| 8 | ✅ technical_support | ✅ high | ✅ | Pass |
| 9 | ✅ account | ⚠️ high (expected medium) | ✅ | Partial |
| 10 | ✅ sales | ✅ high | ✅ | Pass |
| 11 | ✅ account | ✅ high | ✅ | Pass |
| 12 | ✅ complaint | ✅ high | ✅ | Pass |
| 13 | ❌ billing (expected account) | — | — | Fail |
| 14 | ✅ technical_support | ✅ high | ✅ | Pass |
| 15 | ✅ billing | ⚠️ high (expected medium) | ✅ | Partial |
| 16 | ✅ sales | ✅ medium | ✅ | Pass |
| 17 | ✅ other | ✅ medium | ✅ | Pass |
| 18 | ✅ technical_support | ✅ high | ✅ | Pass |
| 19 | ✅ billing | ✅ high | ✅ | Pass |
| 20 | ✅ other | ✅ high | ✅ | Pass |

**Summary: 17 Pass · 2 Partial · 1 Fail = 95% pass rate (85% strict)**

---

## Failure Analysis

### The One Fail — Input 13

> "Please update my billing address to 42 King St"

**Returned:** `billing`  
**Expected:** `account`

This is the exact same failure from Week 4 v1. The fix I added in v2 ("billing address changes belong to account") partially worked — it reduced the frequency — but not consistently. The phrase "billing address" triggers the billing category even with the disambiguation instruction.

**Root cause:** The word "billing" in "billing address" is dominating the classification signal. The prompt's disambiguation rule is there but being overridden by the surface-level keyword match.

**Fix needed:** Add an explicit example in the few-shot section — "Please update my billing address" → `account`. A direct example will outperform a rule in prose.

### The Two Partials — Inputs 9 and 15

Both cases involved messages I expected the model to rate as medium confidence. The model rated both as high. The categories were correct, but the confidence was overclaimed on genuinely ambiguous inputs.

This isn't a functional failure — the routing would still be correct. But in a real system, overclaimed confidence on ambiguous messages means edge cases won't get flagged for human review when they should be.

---

## Overall Assessment

95% accuracy (19/20 correct categories) is strong. The confidence calibration issue is more subtle and won't affect day-to-day routing — but it matters for building a trustworthy system.

---

## Tomorrow

Study LLM-as-judge — build an evaluator that can assess outputs at scale.
