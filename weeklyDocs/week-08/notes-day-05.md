# 📝 Week 8 · Day 5 — Architecture Documentation + Eval Results

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Write complete documentation — architecture decisions, prompt design rationale, and the full evaluation report.

---

## Architecture Documentation

### System Overview

A 3-prompt pipeline that answers questions from documents without hallucinating. Each prompt has a single, clearly defined responsibility:

```
[Document + Question]
        ↓
  Prompt 1: Chunk Router
  → Identifies relevant sections
        ↓
  Prompt 2: Answer Extractor
  → Extracts answer from relevant sections only
        ↓
  Prompt 3: Quality Checker
  → Verifies answer is supported by source
        ↓
[Answer + Citation + Confidence + Verification]
```

### Why Three Prompts Instead of One

A single-prompt approach sends the full document + question to the model and asks it to answer. This works on short documents but degrades on longer ones because relevant content competes with irrelevant content for the model's attention.

The three-prompt design solves this by giving each step a smaller, clearer job:
- The Router reduces noise before answering begins
- The Extractor works only on pre-filtered content
- The Checker catches failures independently

### Key Design Decisions

**Decision 1: Inclusive routing**  
The Chunk Router is instructed to be inclusive — include any section that might be relevant. False positives here are cheap. False negatives (excluding a section that contains the answer) are catastrophic.

**Decision 2: Explicit anti-inference rule**  
The Answer Extractor has an explicit rule prohibiting inference and estimation. Without it, the model will helpfully derive answers from related content. That behaviour looks useful but is hallucination.

**Decision 3: Quality Checker as the last line of defence**  
The Quality Checker runs on every output, not just suspicious ones. It's the system's memory of what was promised in the brief: zero hallucination.

---

## Evaluation Report Summary

**Test corpus:** 5 documents, 35 questions (25 in-document, 10 not-in-document)

**Final results after all fixes:**

| Metric | Result |
|--------|--------|
| In-document accuracy | 25/25 (100%) |
| Abstention rate | 10/10 (100%) |
| Hallucination rate | 0/25 (0%) |
| Quality Checker agreement | 35/35 (100%) |

**Iterations to reach these results:**
- v1 (Day 2): 23/25 in-document · 9/10 abstention · 1 hallucination
- v2 (Day 4): 25/25 in-document · 10/10 abstention · 0 hallucinations

**What changed between v1 and v2:**
1. Anti-inference rule added to Answer Extractor
2. Section citation tiebreaker added
3. Footnote/parenthetical instruction added

---

## What This Project Demonstrates

Every skill from the past 8 weeks appears in this project:

| Skill | Where it appears |
|-------|-----------------|
| System prompt design (Week 2) | All 3 prompts have system-level constraints |
| Structured JSON output (Week 3) | All 3 prompts return JSON |
| Prompt chaining (Week 3/4) | The pipeline is a 3-step chain |
| Few-shot examples (Week 1) | Inference example in Answer Extractor |
| Edge case handling (Week 4/6) | Anti-inference rule, tiebreaker, footnote instruction |
| LLM-as-judge (Week 7) | Quality Checker is the evaluator |
| Evaluation methodology (Week 7) | 35-input test set, pre-written expected outputs |
| Niche application (Week 5/6) | Internal business tools — document knowledge |

---

## Tomorrow

Record the Loom walkthrough.
