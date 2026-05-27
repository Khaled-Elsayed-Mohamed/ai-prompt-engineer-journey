# 🔨 Week 6 · Day 4 — System Prompt + Tone Constraints

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Add a system prompt that controls the model's behaviour globally — tone, format, and constraint enforcement — so the user prompt stays focused on the task.

---

## Why a System Prompt Here

The v2 user prompt is doing two things at once: explaining the task AND setting behavioural constraints. This is a code smell in prompt engineering. The system prompt is the right place for persistent rules that don't change per request.

Split:
- **System prompt** — who the model is, how it behaves, non-negotiable constraints
- **User prompt** — the actual task with the meeting notes

---

## The System Prompt

```
You are a meeting notes processor. Your job is to extract structured information from raw meeting notes and return it as valid JSON.

You follow these rules without exception:
1. Return ONLY valid JSON. Never include explanation text, markdown code blocks, or commentary outside the JSON object.
2. Never invent information. If an owner isn't named, use null. If a deadline isn't mentioned, use null. Do not guess.
3. Keep the summary factual and synthesis-focused. Do not editorialize or add conclusions not present in the notes.
4. Classify conservatively: when in doubt whether something is a decision or an open question, classify it as an open question.
5. Action items must describe a concrete task. Vague intentions ("look into it", "think about") are not action items.

You process whatever notes you are given — structured or messy, complete sentences or fragments — and always return clean, well-formed JSON.
```

---

## What the System Prompt Adds

**Rule 4 — Conservative classification** is new. This directly addresses the edge case from Day 3 (input 10) where the model was inconsistent on ambiguous items. "When in doubt, use open_questions" gives it a clear tiebreaker.

**Rule 2 — No hallucination** explicitly covers `owner: null`. Without this, the model sometimes inferred an owner from context when none was stated.

**Rule 5 — Concrete tasks only** tightens the action_items output. Some raw notes contain phrases like "we should probably look into the pricing issue" — this is not an action item.

---

## Testing the System Prompt Addition

Ran all 10 original inputs again with the system prompt + simplified user prompt.

Results: identical to v2 on 9/10. The ambiguous case (input 10) now consistently returns the ambiguous item as an open question rather than a decision — the tiebreaker rule worked.

**Effective score: 10/10 consistent behaviour.**

---

## Observation: System Prompts for Consistency, Not Capability

The system prompt didn't make the model smarter — it made its behaviour more predictable. The capability was always there. What the system prompt did was reduce variance on edge cases by removing ambiguity in the rules.

This is what "system prompt as specification" means in practice. You're not training the model — you're removing its degrees of freedom.

---

## Tomorrow

Wrap everything in a Python CLI script that reads from a file or stdin.
