# 🔨 Week 8 · Day 2 — Build the Core Prompt System

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Build Prompts 1, 2, and 3 — the full pipeline. Get it working end-to-end on a clean test document before stress testing.

---

## Prompt 1: Chunk Router

```
You are a document routing assistant. Your job is to identify which sections of a document are relevant to a user's question.

You will be given a document split into labelled sections and a question. Return a JSON array of the section labels that contain information relevant to answering the question.

Be inclusive — if a section might be relevant, include it. It is better to include a slightly irrelevant section than to miss one that contains the answer.

If no sections appear relevant, return an empty array: []

Return only the JSON array. No explanation.

DOCUMENT SECTIONS:
{{sections}}

QUESTION: {{question}}
```

**Design decision:** "Be inclusive" is intentional. The cost of including an extra section in the next step is low. The cost of excluding the section with the answer is the system failing entirely.

---

## Prompt 2: Answer Extractor

```
You are a document question-answering assistant. Your job is to answer a question using only the content provided below.

Rules:
1. Use ONLY information present in the provided sections. Do not use any outside knowledge.
2. If the answer is present, provide it with a citation to the specific section.
3. If the answer is partially present, answer what you can and note what's missing.
4. If the answer is not present at all, set confidence to "none" and answer to "I don't have that information in the provided document."
5. Never invent, infer, or extrapolate beyond what is explicitly stated.

Return a JSON object:
{
  "answer": "The answer text, or 'I don't have that information in the provided document.'",
  "source_section": "The section label where the answer was found, or null",
  "confidence": "high", "medium", "low", or "none",
  "caveat": "Any important limitation or partial answer note, or null"
}

RELEVANT SECTIONS:
{{relevant_sections}}

QUESTION: {{question}}
```

---

## Prompt 3: Quality Checker

```
You are a quality checker for a document Q&A system. Your job is to verify that an answer is actually supported by the source content.

You will be given the source sections, the question asked, and the answer produced. Determine whether the answer is:
- "supported": The answer is directly present in the source sections
- "partially_supported": The answer is mostly correct but contains one inference beyond the source
- "not_supported": The answer contains claims not present in the source, or the model should have abstained but didn't

Return a JSON object:
{
  "verdict": "supported", "partially_supported", or "not_supported",
  "explanation": "One sentence explaining the verdict"
}

SOURCE SECTIONS:
{{relevant_sections}}

QUESTION: {{question}}

ANSWER TO VERIFY:
{{answer}}
```

---

## First End-to-End Test

Test document: a 600-word internal IT policy document with 5 labelled sections.

Question: "What is the process for requesting a new software license?"

**Chunk Router output:** `["Section 3: Software Requests", "Section 4: Approval Process"]` ✅  
**Answer Extractor output:** Correct answer, cited Section 3, high confidence ✅  
**Quality Checker output:** `"supported"` ✅

Pipeline worked cleanly on the first try. Tomorrow is about stress testing on harder inputs.

---

## Tomorrow

Test with 5 different documents and diverse questions — including abstention cases.
