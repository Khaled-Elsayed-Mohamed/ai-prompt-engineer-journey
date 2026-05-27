# 🧠 Week 8 — Capstone Project: Document Q&A System

**AI Prompt Engineer Journey · Khaled**

> [!IMPORTANT]
> **Goal this week:** Build your best work. An ambitious project that demonstrates the full range of what you've learned over 8 weeks — and is worth showing to every potential employer.

---

## 📊 Progress Tracker

| Day | Mode | Theme | Status |
|-----|------|-------|--------|
| Day 1 | 🔨 Build | Project brief + architecture planning | ✅ Done |
| Day 2 | 🔨 Build | Core prompt system (2-3 prompts) | ✅ Done |
| Day 3 | 🔨 Build | Test with diverse, messy real-world inputs | ✅ Done |
| Day 4 | 🔨 Build | Refine, add guardrails for edge cases | ✅ Done |
| Day 5 | 📝 Doc | Full architecture documentation + eval results | ✅ Done |
| Day 6 | 🔨 Build | Record Loom demo walkthrough | ✅ Done |
| Day 7 | 🔁 Review | Publish everything, LinkedIn announcement | ✅ Done |

---

## 🎯 The Capstone: Document Q&A System

**What it does:** Given a text document and a user question, answers the question accurately using only content from the document. Returns the answer, the source section, and a confidence indicator. Says "I don't have that information" when the answer isn't in the document.

**Why this is the capstone:** It combines everything from the journey:
- System prompt design (Week 2)
- JSON structured output (Week 3)
- Multi-step prompt chaining (Week 3/4)
- Edge case handling and guardrails (Week 4)
- Evaluation methodology (Week 7)
- Internal tools niche expertise (Week 5/6)

---

## 🏗️ Architecture

**3-prompt pipeline:**

1. **Chunk Router** — splits a long document into sections and identifies which sections are relevant to the question
2. **Answer Extractor** — reads the relevant sections and extracts an answer, citing the source section
3. **Quality Checker** — validates the answer against the source text (LLM-as-judge from Week 7)

---

## 📊 Results

**Test corpus:** 5 documents across different domains (HR policy, product spec, meeting transcript, technical guide, financial summary)

**Accuracy (answer in document):** 23/25 questions answered correctly with correct citation  
**Abstention (answer not in document):** 9/10 "I don't have that information" responses when the answer genuinely wasn't there  
**Hallucination rate:** 0/25 factual hallucinations (the 2 incorrect answers were wrong section citations, not invented facts)

---

## 📂 Files

- `notes-day-01.md` through `notes-day-07.md`
- `prompts/doc-qa-system.md` — full prompt architecture documentation
- `scripts/doc_qa.py` — complete Python implementation
- `eval-results.md` — evaluation report with all test cases

---

## 🔑 What This Demonstrates

> *"I built a 3-prompt pipeline that answers questions from documents without hallucinating. The key constraint is 'only use content from the provided document' — enforced in the prompt and validated by a third evaluator prompt. The system correctly abstains 90% of the time when the answer isn't present, which is the hardest behavior to get right. The evaluation report documents every test case."*

---

## 💡 Month 2 Complete

Eight weeks ago: writing prompts in a chat window with no framework.  
Now: a 3-project portfolio covering classification, document processing, and Q&A — all with documented test results, working Python code, and clear write-ups.

**Month 3 is the job hunt. Let's go. 🎯**

---

*Next up → Week 9: Polish Your Online Presence 🚀*
