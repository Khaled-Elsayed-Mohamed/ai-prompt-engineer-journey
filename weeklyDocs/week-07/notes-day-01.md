# 📖 Week 7 · Day 1 — What "Evaluation" Means in Prompt Engineering

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Understand evaluation as a discipline — not just "does it work?" but how to measure it rigorously.

---

## The Problem With "It Looks Good"

Before this week, my testing process was: run a few examples, check if the output looks reasonable, ship it. That's not evaluation — that's optimism.

The problem: you can't improve what you can't measure. And you can't trust a prompt in production if you only tested it on the three examples you thought of in advance.

Real evaluation answers a different question: **"How does this prompt perform across the full distribution of inputs it will actually encounter?"**

---

## What Evaluation Actually Is

Evaluation in prompt engineering means:

1. **Defining what "correct" looks like** — before you test, you need a rubric or expected output
2. **Building a representative test set** — inputs that reflect the real variety of what the prompt will see
3. **Running the prompt on every input** — not cherry-picking
4. **Grading every output** — Pass, Fail, or Partial against the defined rubric
5. **Analysing failures** — not just counting them, understanding *why* they fail
6. **Iterating and re-running** — tracking improvement across versions

This is the difference between a demo and a reliable system.

---

## Three Types of Evaluation

### Pass/Fail Eval
Used for tasks with a clear right answer: classification, extraction, structured output.

Example: "Did the classifier return the correct category?"  
Grade: correct / incorrect. No partial credit.

### Rubric-Based Eval
Used for tasks where quality exists on a spectrum: summaries, drafts, explanations.

Example: "Rate this meeting summary on accuracy (1–5), conciseness (1–5), and actionability (1–5)."  
Grade: numeric score per dimension.

### LLM-as-Judge
Use a second AI model to evaluate the output of the first.

Example: Send the original input + the model's output to a separate "evaluator" prompt. Ask it to grade based on a rubric.

Useful when: you have too many outputs to grade manually, or the rubric is complex enough that consistent human grading would be slow and expensive.

---

## Why This Comes Up in Every Interview

Every prompt engineering job involves iterating on prompts over time. To know whether a change made things better or worse, you need a baseline. Without evaluation methodology, you're guessing.

The question "How do you know your prompt is working?" has a real answer now:

> "I build a test set of representative inputs with expected outputs, run every input through the prompt, and grade each output against the expected result. I track Pass/Fail/Partial and document failures with root cause analysis. When I make changes, I re-run the full test set and compare scores."

---

## Tomorrow

Build a 20-input test set for the customer message classifier from Week 4.
