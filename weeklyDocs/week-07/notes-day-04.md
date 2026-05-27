# 📖 Week 7 · Day 4 — LLM-as-Judge Concept

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Understand what LLM-as-judge is, when to use it, and what its limitations are before building one tomorrow.

---

## What LLM-as-Judge Is

LLM-as-judge means using a language model to evaluate the output of another language model (or the same one). You write an evaluator prompt that takes:

- The original input
- The model's output
- A grading rubric

And returns a structured assessment: a score, a verdict, and a reason.

---

## Why It Exists

Manual evaluation doesn't scale. If you have 20 test cases, grading by hand takes 20 minutes. If you have 500, it takes hours. If your system is live and you want to continuously monitor output quality on real traffic, human grading is impossible.

LLM-as-judge fills that gap. It's not perfect — it has its own failure modes — but it's fast, consistent, and surprisingly accurate for well-defined rubrics.

---

## When to Use It

| Situation | Eval Approach |
|-----------|--------------|
| Binary correctness (classifier, extractor) | Pass/Fail by comparison — LLM judge optional |
| Quality on a spectrum (summaries, drafts) | Rubric-based — LLM judge very useful |
| Large scale (hundreds of inputs) | LLM judge almost necessary |
| High stakes (medical, legal) | Human in the loop — don't rely on LLM judge alone |
| Confidence calibration check | LLM judge works well |

For my classifier evaluation, the main use case is **confidence calibration checking** — catching cases where the category is right but the confidence score is poorly calibrated.

---

## How to Write a Good Evaluator Prompt

The key principles:

**1. Give it the full context.** The evaluator needs the original input AND the output — it can't grade blindly.

**2. Use a structured rubric.** Vague instructions like "assess quality" produce inconsistent results. Specific dimensions like "Is the category correct? (yes/no)" produce consistent ones.

**3. Ask for a reason.** The reason is more valuable than the score — it tells you *why* something failed, which is what you need for fixing it.

**4. Use a separate model if possible.** Having the same model evaluate its own outputs introduces a bias toward approving its own work. If you're evaluating Claude outputs, using a separate Claude call (or a different model) reduces this.

**5. Keep the rubric simple.** Each dimension should be a single, clear question. If a dimension requires the evaluator to make a judgment call, you'll get inconsistent scores.

---

## Known Limitations of LLM-as-Judge

- **Self-serving bias** — models tend to rate outputs from models like themselves more favourably
- **Verbosity bias** — longer, more detailed answers often score higher even when concision was the goal
- **Position bias** — when comparing two options, models often prefer the first one shown
- **Rubric drift** — without anchoring examples, the model's interpretation of a 3/5 vs 4/5 can shift across a test run

For a classifier evaluation (binary correctness + calibration check), most of these biases don't apply — the questions are too concrete for subjectivity to creep in.

---

## Tomorrow

Build the evaluator prompt and run it on the 20 classifier outputs.
