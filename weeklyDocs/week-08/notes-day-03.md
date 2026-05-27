# 🔨 Week 8 · Day 3 — Test With Diverse Real-World Inputs

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Run 35 question/document pairs through the full pipeline — 25 where the answer is present, 10 where it isn't.

---

## The Test Corpus

Five documents, varied types:

| Doc | Type | Length | Domain |
|-----|------|--------|--------|
| A | HR leave policy | ~800 words, 6 sections | Internal HR |
| B | Product specification | ~1,200 words, 8 sections | Technical |
| C | Meeting transcript | ~600 words, 5 sections | Internal |
| D | Technical setup guide | ~900 words, 7 sections | IT |
| E | Financial summary report | ~700 words, 5 sections | Finance |

Questions were written in two categories:
- **In-document (25):** The answer is definitely present
- **Not-in-document (10):** The question is plausible but the answer doesn't exist in the doc

---

## Results: In-Document Questions (25)

| Doc | Questions | Correct Answer | Correct Citation | Pass |
|-----|-----------|---------------|-----------------|------|
| A (HR) | 5 | 5 | 5 | 5/5 |
| B (Product spec) | 6 | 6 | 5 | 5/6 |
| C (Transcript) | 5 | 5 | 5 | 5/5 |
| D (IT guide) | 5 | 5 | 5 | 5/5 |
| E (Financial) | 4 | 3 | 3 | 3/4 |

**Total: 23/25 correct answers + correct citations.**

**2 failures:**
- Doc B, Q4: Answer was correct but cited the wrong section (Section 3 instead of Section 5 — the answer appeared in both, but Section 5 was more specific)
- Doc E, Q3: Answer was partially correct — gave the right Q1 figure but missed the footnote clarification about one-off items

---

## Results: Not-in-Document Questions (10)

| # | Doc | Question | Abstained? |
|---|-----|---------|-----------|
| 1 | A | "What is the company's maternity leave policy?" (not in HR doc) | ✅ Yes |
| 2 | A | "How many days of sick leave per year?" (not stated explicitly) | ✅ Yes |
| 3 | B | "What does the product cost?" (no pricing in spec) | ✅ Yes |
| 4 | B | "Who is the product manager?" (not mentioned) | ✅ Yes |
| 5 | C | "What was decided about the marketing budget?" (different meeting) | ✅ Yes |
| 6 | C | "Who attended the meeting?" (not listed in transcript) | ✅ Yes |
| 7 | D | "What is the WiFi password?" (not in IT guide) | ✅ Yes |
| 8 | D | "How long does setup typically take?" (not stated) | ❌ No — hallucinated "approximately 30 minutes" |
| 9 | E | "What is the CEO's forecast for next year?" (not in report) | ✅ Yes |
| 10 | E | "Are there any pending lawsuits mentioned?" (not in report) | ✅ Yes |

**Abstention rate: 9/10 (90%).**

**The one hallucination (D, Q8):** "How long does setup typically take?" — the guide had step-by-step instructions but no time estimate. The model inferred a time from the number of steps. This is exactly the failure mode the system was designed to prevent.

---

## Quality Checker Performance

The Quality Checker caught the hallucination on D/Q8 — returned `"not_supported"` with explanation: *"The answer states 'approximately 30 minutes' but no time estimate appears in the source sections."*

The pipeline's third prompt worked as designed for its most important use case.

---

## Tomorrow

Fix the hallucination case, add guardrails for inference-type questions.
