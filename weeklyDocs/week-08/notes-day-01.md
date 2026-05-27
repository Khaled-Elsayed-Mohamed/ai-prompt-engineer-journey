# 🔨 Week 8 · Day 1 — Project Brief + Architecture Planning

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Plan the capstone before building anything. Define exactly what success looks like, then design the architecture.

---

## Choosing the Project

The roadmap offered four options for the capstone. I ruled out three quickly:

- **AI writing assistant for a specific industry** — too close to Project #1 (classifier) in terms of what it demonstrates
- **Automated email response drafter** — interesting but heavily overlap with the meeting processor
- **Content repurposing tool** — outside my chosen niche (internal business tools)

**Document Q&A System** — this is the one. It combines everything from the past 7 weeks and it's genuinely useful in a business context. Companies have thousands of documents (policies, specs, manuals, contracts) and employees spend real time searching through them manually.

---

## The Brief

> "Build a system that takes a text document and a user question, and returns an accurate answer drawn only from the document. The system must cite the source section, indicate its confidence, and say 'I don't have that information' when the answer genuinely isn't present. Zero tolerance for hallucination."

**What success looks like:**
- Answers correct questions correctly, with accurate citations
- Refuses to answer questions the document doesn't address (abstention)
- Never invents information not present in the document
- Works on varied document types: policies, specs, transcripts, reports

---

## Architecture: Why One Prompt Isn't Enough

A single prompt approach — "here's the document, answer the question" — fails at scale for one reason: **context window competition**. When a long document and a question are both in the prompt, the model has to hold everything in attention simultaneously. On long documents, important content gets deprioritised and quality degrades.

The solution: a multi-step pipeline that separates the work.

---

## 3-Prompt Pipeline Design

**Prompt 1 — Chunk Router**  
Input: The full document (split into labelled sections) + the question  
Task: Identify which sections of the document are relevant to the question  
Output: A list of section labels to focus on

**Prompt 2 — Answer Extractor**  
Input: Only the relevant sections (from Prompt 1) + the question  
Task: Extract and synthesise an answer from the provided content  
Output: Answer, source section citation, confidence (high/medium/low/none)  
Constraint: "Use only the content provided. If the answer is not present, return confidence: none."

**Prompt 3 — Quality Checker**  
Input: The relevant sections + the question + the answer from Prompt 2  
Task: Verify the answer is supported by the source content  
Output: Verified / Not supported + explanation

This is the LLM-as-judge pattern from Week 7, applied to the capstone in a production-relevant way.

---

## Why This Architecture

- **Chunk Router** reduces noise — the answer extractor sees only relevant content
- **Answer Extractor** has a single job with a hard constraint: don't invent
- **Quality Checker** catches cases where the extractor got overconfident

Three prompts, each with one clearly defined responsibility.

---

## Tomorrow

Build Prompt 1 (Chunk Router) and Prompt 2 (Answer Extractor).
