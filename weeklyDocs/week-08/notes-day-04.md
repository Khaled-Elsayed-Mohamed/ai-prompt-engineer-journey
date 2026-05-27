# 🔨 Week 8 · Day 4 — Refine + Add Guardrails for Edge Cases

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Fix the one hallucination from Day 3 and harden the system against inference-type questions — cases where the model can derive a plausible answer but shouldn't.

---

## Understanding the Failure

The hallucination on Doc D / Q8 ("How long does setup typically take?") was a specific type: **implicit inference**. The document didn't state a time estimate, but the model saw 6 steps and inferred ~30 minutes. This was a reasonable inference — but it's still an invention.

The system needs to distinguish between:
- **Explicit answers** — stated directly in the document → answer with citation
- **Inferable answers** — can be derived from document content → should abstain or caveat clearly
- **Absent answers** — not addressable from the document at all → abstain

The current prompt doesn't make this distinction.

---

## The Fix: Explicit Anti-Inference Instruction

Added to Prompt 2 (Answer Extractor):

```
CRITICAL: Do not calculate, infer, or derive answers from the document. If the question asks for something that requires combining information or making an inference that isn't stated explicitly, treat it the same as an absent answer. Set confidence to "none".

Example of inference to avoid: A document lists 6 steps but doesn't say how long they take. Do not estimate a duration from the number of steps. Return: "I don't have that information in the provided document."
```

The concrete example is important — it gives the model a precise pattern to recognise, not just a vague rule.

---

## Full Revised Prompt 2

Rules section now reads:

```
Rules:
1. Use ONLY information explicitly present in the provided sections. Do not use outside knowledge.
2. Do not calculate, infer, or derive answers. If a question requires combining facts or making an inference not stated in the document, abstain.
3. If the answer is present, provide it with a citation to the specific section.
4. If the answer is partially present, answer what you can and note what's missing.
5. If the answer is not present or requires inference, set confidence to "none" and answer to "I don't have that information in the provided document."
6. Never invent, estimate, or extrapolate beyond what is explicitly stated.
```

Rule 2 is new. The order matters — it's placed before the "if present" rules so inference-blocking is checked first.

---

## Retest: All 10 Abstention Cases

| # | Before Fix | After Fix |
|---|-----------|----------|
| 1–7 | ✅ Abstained | ✅ Abstained |
| 8 (hallucination) | ❌ Hallucinated | ✅ Abstained |
| 9–10 | ✅ Abstained | ✅ Abstained |

**Post-fix abstention rate: 10/10 (100%).**

---

## Retest: 25 In-Document Questions

Both previous failures retested:

- Doc B / Q4 (wrong section citation): Still incorrect citation — the answer genuinely appears in two sections and the model picks the less specific one. Added a tiebreaker rule: "When an answer appears in multiple sections, cite the most specific one." Retested → correct.

- Doc E / Q3 (missed footnote): The answer is in the main body + a footnote. The Chunk Router included the section but the Answer Extractor didn't read the footnote. Added instruction: "Pay attention to footnotes, parenthetical remarks, and qualifications — they often contain important caveats." Retested → correct with caveat.

**Final results: 25/25 in-document + 10/10 abstention = 35/35.**

---

## What This Week Has Been About

Every fix this week came from the same place: writing a more precise spec. The model isn't failing because it's incapable — it's failing because I hadn't told it exactly what to do in the edge case.

That's the prompt engineering loop: build → test → find where the spec is incomplete → write a better spec → test again.

---

## Tomorrow

Write the full architecture documentation and evaluation report.
