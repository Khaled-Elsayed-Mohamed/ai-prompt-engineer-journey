# 🧠 Week 7 — Understanding Evaluation

**AI Prompt Engineer Journey · Khaled**

> [!IMPORTANT]
> **Goal this week:** Learn how to measure whether a prompt is actually working. This is the topic that comes up in almost every prompt engineer interview — and the skill that separates hobbyists from professionals.

---

## 📊 Progress Tracker

| Day | Mode | Theme | Status |
|-----|------|-------|--------|
| Day 1 | 📖 Learn | What "evaluation" means in prompt engineering | ✅ Done |
| Day 2 | 🔨 Build | Build a 20-input test set for the classifier | ✅ Done |
| Day 3 | 🔨 Build | Run and grade all 20 inputs | ✅ Done |
| Day 4 | 📖 Learn | "LLM as judge" concept | ✅ Done |
| Day 5 | 🔨 Build | Build a second prompt that evaluates outputs | ✅ Done |
| Day 6 | 📝 Doc | Write evaluation report for classifier project | ✅ Done |
| Day 7 | 🔁 Review | Push evaluation artifacts to GitHub | ✅ Done |

---

## 🎯 The Core Concept

Evaluation is the discipline of measuring how well a prompt performs on a defined set of inputs. Without it, you don't know if a prompt is good — you think it is because the three examples you tested looked fine.

**Three types of evaluation:**

1. **Pass/Fail** — the output is either correct or it isn't (classifiers, extractors)
2. **Rubric-based** — rate output quality on defined criteria (summaries, drafts)
3. **LLM-as-judge** — use a second AI model to evaluate the output of the first

---

## 📊 Evaluation Results: Customer Message Classifier

**Test set:** 20 inputs (10 original + 10 new, including adversarial cases)

| Category | Inputs Tested | Correct | Accuracy |
|----------|--------------|---------|----------|
| billing | 4 | 4 | 100% |
| technical_support | 4 | 4 | 100% |
| account | 4 | 4 | 100% |
| sales | 2 | 2 | 100% |
| complaint | 3 | 3 | 100% |
| other | 3 | 2 | 67% |
| **Total** | **20** | **19** | **95%** |

**The one failure:** "Please update my billing address" → classified as `billing` instead of `account`. A billing address change is an account setting, not a payment issue. Fix: add "billing address changes" to the account category definition.

---

## 🤖 LLM-as-Judge Result

Built an evaluator prompt that assesses each classifier output on:
- **Correctness** (is the category right?)
- **Confidence calibration** (is the stated confidence appropriate?)
- **Reason quality** (does the reason accurately explain the classification?)

The evaluator caught 2 cases where the category was correct but the confidence was overclaimed (model said "high" when the message was legitimately ambiguous). The judge prompt is in `prompts/evaluator-prompt.md`.

---

## 📂 Files

- `notes-day-01.md` through `notes-day-07.md`
- `prompts/evaluator-prompt.md` — the LLM-as-judge prompt
- `evaluation-report.md` — full evaluation results with analysis

---

## 🔑 Interview Talking Point

> "I built a 20-input test set for my classifier, graded every output, and documented the one failure case. Then I built a second prompt that evaluates classifier outputs against a rubric — checking not just whether the category is correct but whether the confidence claim is calibrated. That second step caught two cases where the model was overconfident on ambiguous inputs. The fix for both was adding clearer disambiguation language to the prompt, not changing the model or the temperature."

---

*Next up → Week 8: Capstone Project 🚀*
