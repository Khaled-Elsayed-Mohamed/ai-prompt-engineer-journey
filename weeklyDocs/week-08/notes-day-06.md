# 🔨 Week 8 · Day 6 — Loom Demo Walkthrough

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Record a 3–5 minute walkthrough of the Document Q&A System — clear, confident, no rambling.

---

## Prep: Scripting the Walkthrough

Before hitting record, I scripted the demo. Not word-for-word, but a firm outline. The goal is to show the system working while narrating the decisions behind it — not just reading code.

**Structure I settled on:**

1. **(0:00–0:30)** The problem — why document Q&A is hard and why hallucination is the main risk
2. **(0:30–1:30)** Architecture overview — the 3-prompt pipeline, why 3 instead of 1
3. **(1:30–3:00)** Live demo — two examples: one where the answer is present, one where it isn't
4. **(3:00–4:00)** Show the Quality Checker catching an edge case
5. **(4:00–4:30)** Evaluation results — 35/35, 0 hallucinations, how I got there

Total target: under 5 minutes.

---

## What I Showed in the Demo

**Example 1 — Answer present:**  
Document: IT setup guide  
Question: "What permissions are required to install new software?"  
Output: Correct answer, cited Section 2, high confidence, Quality Checker: supported  
*Narration: "The Chunk Router identified Section 2 as relevant, the Extractor pulled the answer directly from the text, and the Checker confirmed it's verbatim from the source."*

**Example 2 — Answer not present:**  
Document: IT setup guide  
Question: "How long does setup typically take?"  
Output: "I don't have that information in the provided document." confidence: none  
*Narration: "This was the failure case from my first round of testing. The guide has 6 steps but no time estimate. Earlier versions of the prompt inferred 30 minutes from the steps — that's hallucination. The anti-inference rule I added in Day 4 prevents this. The system correctly abstains."*

**Example 3 — Quality Checker catching an issue:**  
Showed the raw output from an early prompt version where the Extractor gave an answer that went slightly beyond the source, and the Checker returned `"partially_supported"` with an explanation.  
*Narration: "The Quality Checker is the system's backstop. Even if the Extractor gets overconfident, the Checker flags it. In production, a partially_supported verdict would trigger a human review queue."*

---

## What Made the Demo Work

**Showing a failure, not just successes.** The most compelling 30 seconds of the demo was showing the old hallucination and then showing the fixed version. It demonstrates the iteration process — which is more impressive than a demo that works perfectly on the first try.

**Narrating the decisions, not the code.** I didn't read the prompt text. I explained why each rule was there and what it was preventing.

**Keeping the eval results brief.** "35 test cases, 0 hallucinations, 100% abstention rate" — that's the whole story. No need to walk through every row of the table.

---

## Recording Notes

- Took 3 takes total
- Take 1: too long (6:40), went into too much detail on the code
- Take 2: recovered from a stumble badly, started over
- Take 3: 4:20, clean, kept on the architecture and the failures rather than implementation details

Final: Take 3 uploaded to Loom.

---

## Tomorrow

Publish everything to GitHub, write the final reflection.
