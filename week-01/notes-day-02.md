# ✅ Day 2 — Tuesday · Build Day

## What I Built
> [!NOTE]
> **Task:** Rewrote 5 prompts using **Role + Task + Format** structure and tested each one.

---

## The Framework

```
Role:    "You are a [specific expert]..."
Task:    "Your job is to [clear action verb] [specific thing]..."
Format:  "Respond in [format] with [constraints]..."
```

---

## Before & After — 5 Prompt Rewrites

### Prompt 1 — Article Summary

```diff
- "Summarise this article"

+ "You are a research assistant helping a busy professional.
+  Your job is to summarise the article below into 3 bullet points,
+  each one sentence long. Focus only on the main argument and key
+  evidence. Do not include opinions or filler."
```

---

### Prompt 2 — Email Fix

```diff
- "Fix my email"

+ "You are a professional business writing coach.
+  Your job is to rewrite the email below so it sounds confident,
+  clear, and respectful. Keep the same meaning. Return only the
+  rewritten email — no explanation needed."
```

---

### Prompt 3 — Blog Post Ideas

```diff
- "Give me ideas for a blog post"

+ "You are a content strategist for a B2B SaaS company.
+  Your job is to generate 5 blog post ideas for an audience of
+  startup founders interested in AI tools. Format each idea as:
+  Title | One-sentence description | Target reader pain point."
```

---

### Prompt 4 — Explain a Concept

```diff
- "Explain this concept simply"

+ "You are a teacher explaining complex ideas to a curious 16-year-old
+  with no technical background. Your job is to explain [concept] in
+  plain English using one real-world analogy. Keep your response
+  under 100 words."
```

---

### Prompt 5 — Code Review

```diff
- "Check my code for bugs"

+ "You are a senior software engineer doing a code review.
+  Your job is to review the Python function below and identify any
+  bugs, edge cases, or performance issues. Format your response as
+  a numbered list. For each issue, state: what's wrong, why it
+  matters, and how to fix it."
```

---

## What I Noticed

> [!IMPORTANT]
> The rewritten prompts consistently gave **longer, more structured, more useful** responses — not because the model got smarter, but because I removed its guesswork.

> [!TIP]
> **Key pattern I noticed:** Adding a Format constraint was the single biggest improvement. Even a simple "respond in bullet points" changed the output quality significantly.

---

## Key Insight — Day 2

> *"A vague prompt gets a vague answer. The model is a mirror — it reflects the quality of your input."*
