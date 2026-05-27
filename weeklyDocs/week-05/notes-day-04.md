# 📖 Week 5 · Day 4 — 2 Case Studies: AI in Internal Business Tools

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Read 2 real case studies of how companies use AI for internal workflows. Extract what's generalizable.

---

## Case Study 1: How a Law Firm Used LLMs for Contract Review

**Source:** Medium / public write-up from a developer at a boutique legal firm.

**The problem:** Associates spent 4-6 hours per contract reading and extracting standard clauses (liability caps, termination conditions, governing law, etc.) before any actual analysis could happen.

**What they built:** A prompt system that takes a contract (up to 50 pages) and extracts 12 specific clause types into a structured JSON object. Associates then review and annotate the extracted data, rather than reading the raw document.

**Key prompt engineering decisions:**
- Used a two-step approach: first extract section headings and page numbers, then process each relevant section independently. This prevented the model from losing context across a very long document.
- Added explicit "output null if not present" instructions for every field — early versions hallucinated missing clauses rather than returning null.
- Used a validation prompt after extraction: "For each extracted clause, does the text I provided actually support the extracted value? Return 'verified' or 'uncertain'."

**Result:** Review time for standard contracts dropped from 4-6 hours to 45-90 minutes.

**What I'm taking from this:**
- Long documents need chunking strategies — don't throw everything in one prompt
- `null` for missing data beats hallucination every time — you have to explicitly instruct for it
- A validation step (AI checking its own output) adds reliability without adding human review time

---

## Case Study 2: Internal Chatbot for HR Policy Questions at a Mid-Sized Company

**Source:** LinkedIn article from an HR tech team.

**The problem:** HR received 200+ repetitive questions per month about leave policies, benefits, and compliance — each requiring a staff member to look up the same document and send a standard answer.

**What they built:** A system that indexes HR policy documents and uses retrieval-augmented generation (RAG) to answer questions based only on official policy content.

**Key prompt engineering decisions:**
- The system prompt explicitly stated: "Only answer from the provided context. If the answer is not in the provided context, say 'I don't have that information — please contact HR directly.'"
- Added a citation requirement: every answer must reference the specific policy name and section it came from.
- Human review queue for any answer where the model returned low confidence or "I don't have that information."

**Result:** 60% of HR questions now handled without human involvement. Staff satisfaction with HR support increased because the answers were consistent and immediate.

**What I'm taking from this:**
- "Only answer from provided context" is essential for factual internal tools — hallucination is worse than admitting ignorance
- Citations build trust. Users are more likely to act on an answer that says "per Section 4.2 of the Parental Leave Policy" than one that just gives the answer
- Always include an escalation path — "contact HR directly" is the right fallback, not silence

---

## What Both Case Studies Have in Common

1. **They solve a specific, measurable problem** — not "make things more efficient" but "reduce contract review from 5 hours to 1"
2. **They handle the failure case** — what happens when the AI doesn't know? Both examples answer this explicitly
3. **They keep humans in the loop for high-stakes outputs** — the law firm validates extractions, the HR tool routes uncertain answers to staff
4. **The prompts evolved through testing** — neither example worked perfectly on the first version

These patterns go directly into how I design Week 6's project.
