# 🧠 Week 1 — How LLMs Work & Why Prompts Matter

**📅 May 2026 &nbsp;·&nbsp; AI Prompt Engineer Journey &nbsp;·&nbsp; Khaled**

> [!IMPORTANT]
> **Goal this week:** Understand what's happening when you write a prompt — stop guessing, start designing.

---

## 📊 Progress Tracker

| Day | Mode | Theme | Status |
|-----|------|-------|--------|
| Mon — Day 1 | 📖 Learn | Anthropic Prompt Engineering Intro | ✅ Done |
| Tue — Day 2 | 🔨 Build | Role + Task + Format — Rewrite 5 Prompts | ✅ Done |
| Wed — Day 3 | 📖 Learn | Tokens, Temperature & Context Windows | ✅ Done |
| Thu — Day 4 | 🔨 Build | Temperature 0 vs 1 Experiment | ⬜ Upcoming |
| Fri — Day 5 | 📖 Learn | Zero-shot vs Few-shot Prompting | ⬜ Upcoming |
| Sat — Day 6 | 🔨 Build | Write 3 Few-shot Prompts | ⬜ Upcoming |
| Sun — Day 7 | 🔁 Review | Weekly Reflection | ⬜ Upcoming |

---

---

# ✅ Day 1 — Monday · Learn Day

## What I Studied
> [!NOTE]
> **Source:** Anthropic Prompt Engineering Docs — first 3 sections
> 🔗 [docs.anthropic.com/en/docs/build-with-claude/prompt-engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

### Key Takeaways

- Prompts are instructions — the model doesn't *understand* them the way humans do, it **predicts** the most likely continuation based on training
- Being specific and structured in a prompt directly changes the quality of the output
- Anthropic's docs break prompting into: **clarity**, **context**, and **examples** — these three levers explain most of why prompts succeed or fail

> [!TIP]
> A prompt isn't a question — it's a **specification**. The more precisely you define the role, task, and format, the less the model has to guess.

---

## GitHub Setup Completed

```diff
+ Created profile README repo (Khaled-Elsayed-Mohamed)
+ Created ai-prompt-engineer-journey repo (public)
+ Set up week-01/ folder structure with notes.md, prompts/, scripts/
+ Made first commit
+ Pinned journey repo to profile
```

---

---

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

---

---

# ✅ Day 3 — Wednesday · Learn Day

## Topic: Tokens, Temperature & Context Windows
> [!NOTE]
> **Sources:** Anthropic docs · OpenAI docs — tokens, temperature, context windows

---

### What I Studied

**Tokens**
A token is roughly a word or part of a word — the model reads and generates text in these chunks, not letter by letter. "ChatGPT" = 2 tokens. "I" = 1 token. Punctuation, spaces, and word fragments all count as tokens too.

**Temperature**
Temperature controls how random or predictable the model's output is. It's a dial between deterministic and creative.

**Context Windows**
The context window is the maximum amount of text (in tokens) the model can see at once. Everything outside it gets ignored — the model has no memory beyond it.

---

### Key Takeaways

```diff
+ Tokens are chunks — not words, not characters. Every API call costs tokens (input + output combined).
+ Temperature 0 = consistent and predictable. Temperature 1 = more varied and creative.
+ Context window = the model's "working memory". Exceed it and early content gets dropped.
```

---

> [!IMPORTANT]
> **Why tokens matter for prompt engineering:** Every model has a token limit per request. If your prompt + document + expected output exceeds it, the model either truncates your input or cuts off mid-response. Knowing this shapes how you structure long prompts.

> [!TIP]
> **Rule of thumb for temperature:**
> Use **0** for accuracy-critical tasks — classification, extraction, code review.
> Use **0.7–1** for creative tasks — writing, brainstorming, idea generation.
> Most production prompts live between **0 and 0.5**.

> [!NOTE]
> **Context window in practice:** If you paste a long document and the model "forgets" something from the beginning, it's not hallucinating — it may have simply run out of context. This is why chunking long inputs is a core prompt engineering skill.

---

## Key Insight — Day 3

> *"The model doesn't read your prompt the way you do — it processes tokens, works within a fixed memory window, and adjusts its creativity based on temperature. Understanding these three constraints changes how you design every prompt."*

---

---

# ⬜ Day 4 — Thursday · Build Day

## Topic: Temperature 0 vs Temperature 1 Experiment
> [!NOTE]
> **Task:** Run the same prompt at temperature 0 and temperature 1. Write down exactly what you notice.

### The Prompt I Tested
```
(paste your prompt here)
```

### Results

| | Temperature 0 | Temperature 1 |
|--|---------------|---------------|
| **Output style** | | |
| **Consistency** | | |
| **Creativity** | | |
| **Which was better?** | | |

> [!IMPORTANT]
> *(Write your observation here — what changed and why does it matter?)*

---

---

# ⬜ Day 5 — Friday · Learn Day

## Topic: Zero-shot vs Few-shot Prompting
> [!NOTE]
> **Source:** [learnprompting.org](https://learnprompting.org) — free course

### What I Studied
- 

### Key Takeaways
- 
- 
- 

---

---

# ⬜ Day 6 — Saturday · Build Day

## Topic: Write 3 Few-shot Prompts

> [!NOTE]
> **Task:** Write 3 few-shot prompts for these real tasks:
> 1. Classify a customer complaint
> 2. Extract info from a paragraph
> 3. Summarise an article

### Few-shot Prompt 1 — Customer Complaint Classifier
```
(paste your prompt here)
```

### Few-shot Prompt 2 — Info Extraction
```
(paste your prompt here)
```

### Few-shot Prompt 3 — Article Summariser
```
(paste your prompt here)
```

> [!TIP]
> *(What did adding examples to the prompt change about the output?)*

---

---

# ⬜ Day 7 — Sunday · Weekly Review

## What I Learned This Week
*(Write half a page in your own words — what you learned and what surprised you)*

---

## What Clicked
> [!TIP]
> 

## What Was Confusing
> [!WARNING]
> 

## What I Want To Revisit
> [!CAUTION]
> 

---

## Week 1 — Key Insight

> *"(Write the one sentence that best captures what this week taught you.)"*

---

## Resources I Used This Week

| Resource | What I Used It For |
|----------|--------------------|
| [Anthropic Prompt Engineering Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Day 1 reading |
| [learnprompting.org](https://learnprompting.org) | Day 5 reading |
| | |

---

*Next up → Week 2: Core Techniques Every Prompt Engineer Knows 🚀*
