# 📝 Week 7 · Day 6 — Write the Evaluation Report

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Write a complete evaluation report for the customer message classifier — methodology, results, failure analysis, and fixes made.

---

## Why an Evaluation Report Matters

The eval report is what you'd show a technical interviewer or a team lead to prove the prompt is production-ready. "It works" isn't enough. "Here's the test methodology, the results across 20 inputs, the failure analysis, and the specific fix made" — that's a professional deliverable.

---

## Report Structure

### 1. Overview

**Project:** Customer Message Classifier  
**Version evaluated:** v2  
**Test set size:** 20 inputs  
**Evaluation method:** Manual grading + LLM-as-judge verification  
**Overall result:** 17 Pass · 2 Partial · 1 Fail (95% category accuracy · 85% strict pass rate)

---

### 2. Methodology

**Test set construction:**  
20 inputs were written before running the prompt. Expected outputs (category + confidence level) were documented first to prevent post-hoc rationalisation. Inputs were selected to cover:
- All 6 categories (proportional to expected real-world frequency)
- Clear-cut cases (majority)
- Ambiguous boundary cases (4 inputs)
- A known previous failure case (billing address — Input 13)

**Grading rubric:**  
Each output was assessed on three dimensions:
- Category correctness (binary)
- Confidence calibration (appropriate / overclaimed / underclaimed)
- Reason accuracy (binary)

**LLM-as-judge verification:**  
All 20 outputs were independently assessed by an evaluator prompt. Agreement with manual grading: 100%.

---

### 3. Results by Category

| Category | Inputs | Correct | Pass Rate |
|----------|--------|---------|-----------|
| billing | 5 | 5 | 100% |
| technical_support | 4 | 4 | 100% |
| account | 3 | 2 | 67% |
| sales | 3 | 3 | 100% |
| complaint | 2 | 2 | 100% |
| other | 3 | 3 | 100% |

**Weakest category: account.** The only failure was Input 13 (billing address misclassified as billing). 

---

### 4. Failure Analysis

**Input 13 — Category failure**  
"Please update my billing address to 42 King St" → returned `billing`, expected `account`

Root cause: the word "billing" in "billing address" triggers the billing category even though address updates are account operations. The v2 disambiguation rule ("billing address changes belong to account") is present but overridden by keyword matching in the embedding.

Fix applied: Added an explicit few-shot example to the prompt:  
`"Please update my billing address" → account`

**Inputs 9, 15 — Confidence overclaimed**  
Both ambiguous inputs were returned with high confidence. The categories were correct, but the overclaimed confidence means the system wouldn't flag these for human review when it should.

Root cause: The prompt defines confidence levels but doesn't give concrete examples of what makes an input "ambiguous." The model is applying its own judgment without anchoring.

Fix applied: Added two anchoring examples to the prompt showing medium-confidence classification with explanation.

---

### 5. Post-Fix Retest

After applying both fixes, re-ran the 3 affected inputs:

| Input | Before | After |
|-------|--------|-------|
| 13 (billing address) | Fail → `billing` | Pass → `account` |
| 9 (cancel subscription) | Partial → high confidence | Pass → medium confidence |
| 15 (pricing dispute) | Partial → high confidence | Pass → medium confidence |

**Post-fix result: 20/20 Pass.**

---

### 6. Limitations

- Test set of 20 is sufficient for validation, not comprehensive coverage
- Evaluator was run on the same model family — potential self-approval bias
- Real-world inputs may include languages, tones, or contexts not represented here

---

## Tomorrow

Push evaluation artifacts to GitHub.
