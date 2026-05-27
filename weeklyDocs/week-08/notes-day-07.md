# 🔁 Week 8 · Day 7 — Publish Everything + Month 2 Reflection

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Push the capstone to GitHub, write the final reflection on Month 2, and look at what's ahead.

---

## What Got Published Today

- `prompts/doc-qa-system.md` — full 3-prompt system with architecture notes and design decisions
- `scripts/doc_qa.py` — complete Python implementation of the pipeline
- `eval-results.md` — evaluation report (35 cases, methodology, results, iterations)
- `notes-day-01.md` through `notes-day-06.md` — daily build notes
- `notes.md` — weekly summary

---

## Month 2 Complete — Full Reflection

### What Was Built in Weeks 5–8

| Project | What It Demonstrates |
|---------|---------------------|
| Meeting Notes Processor (W6) | System prompt design, JSON extraction, edge case handling, documentation |
| Evaluation methodology (W7) | Test set construction, LLM-as-judge, grading rubrics, failure analysis |
| Document Q&A System (W8) | Multi-prompt pipelines, hallucination prevention, abstention, production thinking |

Three projects. All documented. All tested. All on GitHub.

### What Changed From Month 1

**Month 1** was about understanding the building blocks — tokens, temperature, few-shot, CoT, APIs. The outputs were scripts and experiments.

**Month 2** was about building complete, documented systems that solve real problems in a specific niche. The outputs are portfolio pieces.

The shift wasn't just in complexity — it was in thinking. Month 1: "Does this output look correct?" Month 2: "How do I define correct, measure it systematically, and prove the system meets the spec?"

### The Hardest Thing This Month

**Abstention.** Getting a model to say "I don't know" is genuinely hard. The default behaviour is to be helpful — which means producing an answer even when the right answer is nothing. The anti-inference rule in the capstone took four test cycles to get right. It's one sentence in the prompt. But finding the right sentence took real work.

### Confidence Scores: End of Month 2

| Skill | Month 1 End | Month 2 End |
|-------|------------|-------------|
| Prompt structure | 8/10 | 9/10 |
| System prompt design | 5/10 | 9/10 |
| Multi-prompt pipelines | 2/10 | 8/10 |
| Evaluation methodology | 2/10 | 9/10 |
| Technical documentation | 4/10 | 8/10 |
| Edge case handling | 5/10 | 9/10 |

### One Sentence Summary of Month 2

> *"I learned that building a prompt that works once is easy — building a system that works consistently, on messy inputs, with documented proof, is the actual job."*

---

*8 weeks complete. 3 projects live. Month 3 ahead. 🎯*
