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
| Thu — Day 4 | 🔨 Build | Temperature 0 vs 1 Experiment | ✅ Done |
| Fri — Day 5 | 📖 Learn | Zero-shot vs Few-shot Prompting | ✅ Done |
| Sat — Day 6 | 🔨 Build | Write 3 Few-shot Prompts | ✅ Done |
| Sun — Day 7 | 🔁 Review | Weekly Reflection | ✅ Done |

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

# ✅ Day 4 — Thursday · Build Day

## Topic: Temperature 0 vs Temperature 1 Experiment
> [!NOTE]
> **Task:** Run the same prompt 4–5 times at each temperature. Compare outputs and document what changed.
> **Model used:** claude-haiku-4-5

---

### The Prompt I Tested

```
You are a creative writing coach. Give me 3 opening lines for a short story 
about a person who discovers an old letter in their attic. Each line should 
have a different emotional tone.
```

---

### Results — Side by Side

| | Temperature 0 | Temperature 1 |
|--|---------------|---------------|
| **Output style** | Structured, consistent labels (Mysterious / Melancholic / Urgent) | Varied labels across runs — Humorous, Hopeful, Energetic, Wistful all appeared |
| **Consistency across runs** | Lines 1 & 2 were **word-for-word identical** across all 4 runs | Every run produced genuinely different lines — different words, different tones |
| **Creativity** | Safe and competent — same strong lines repeated | More surprising — one run included a funny line no other run came close to |
| **Which was better here?** | Less useful for a creative task requiring variety | Better — more interesting range of options |

---

### Actual Outputs

**Temperature 0 — Line 1 (appeared identically in all 4 runs):**
```diff
= "The envelope was addressed in handwriting I didn't recognize, sealed with wax 
=  that had turned the color of old teeth, and it had been waiting in the 
=  darkness for exactly forty-three years."
```

**Temperature 0 — Line 2 (appeared identically in all 4 runs):**
```diff
= "I found the letter on a Tuesday afternoon when I was supposed to be throwing 
=  things away, not collecting ghosts."
```

**Temperature 1 — Sample of variety across runs:**
```diff
+ Run 1: "The letter was sealed with black wax, and the moment I broke it open, I 
+  understood why Grandmother had locked the attic door all those years."

+ Run 2: "If my attic had been organized by anyone other than a pack of forgetful 
+  squirrels, I might never have knocked over that box and discovered the letter 
+  that would accidentally solve a mystery nobody even knew existed."

+ Run 3: "I found the letter tucked behind a loose beam while searching for 
+  Christmas decorations — my mother's handwriting, young and hopeful, addressed 
+  to someone she never became."

+ Run 4: "My fingers froze on the seal the moment I saw the date: 1952, the year 
+  everyone in my family refuses to talk about."

+ Run 5: "The moment I spotted that cream-colored envelope peeking out from 
+  beneath the floorboards, I knew my quiet Tuesday was about to become the kind 
+  of day people write about."
```

---

> [!IMPORTANT]
> **The key finding:** Temperature 0 didn't mean "bad" — the lines it produced were genuinely strong. But it locked onto one answer and repeated it. Temperature 1 explored the full range of the prompt. For creative tasks, that exploration is the whole point.

> [!TIP]
> **When to use each:**
> - **Temperature 0** → classification, extraction, code review, anything where the "right answer" exists
> - **Temperature 1** → creative writing, brainstorming, generating options to choose from
> - **0.5–0.7** → most real-world production prompts — some consistency, some flexibility

> [!NOTE]
> **Surprising observation:** The humorous line in Temperature 1 Run 2 ("forgetful squirrels") would never have appeared at temp 0. Temperature doesn't just change *how* the model writes — it changes *what ideas it's willing to try*.

---

## Key Insight — Day 4

> *"Temperature 0 gives you the model's best single answer, repeated reliably. Temperature 1 gives you the model's imagination. Which one you want depends entirely on what the task actually requires."*

---

---

# ✅ Day 5 — Friday · Learn Day

## Topic: Zero-shot vs Few-shot Prompting
> [!NOTE]
> **Source:** [learnprompting.org — Few-Shot Prompting](https://learnprompting.org/docs/basics/few_shot)

---

### What I Studied

**Zero-Shot Prompting**
No examples provided — the model relies entirely on its pre-trained knowledge to figure out what you want.

**One-Shot Prompting**
A single example is given to clarify the task and expected output format.

**Few-Shot Prompting**
Two or more examples are included, allowing the model to recognise patterns and deliver more accurate, consistently formatted responses.

---

### Key Takeaways

```diff
+ Zero-shot = no examples. Works for simple or well-understood tasks.
+ Few-shot = 2+ examples. Works best when format and accuracy matter.
+ The more structured the output you need, the more few-shot helps.
```

---

> [!IMPORTANT]
> **Real-world application:** Building a prompt to extract invoice data (date, amount, vendor) from messy text? Use few-shot — show the model 2–3 examples of messy input → clean structured output so it knows exactly what format you want. Zero-shot will give inconsistent formatting run to run.

> [!WARNING]
> **Limitations to watch for:**
> - **Context window** — too many examples eats into the space available for the actual input. In production this becomes a real constraint.
> - **Overgeneralisation** — if your examples are too similar, the model may miss edge cases it hasn't seen.
> - **Superficial pattern matching** — the model might copy the surface style of your examples without understanding the underlying task.

> [!TIP]
> **Rule of thumb:** Start zero-shot. If the output format is inconsistent or wrong, add 2–3 examples. Don't add more examples than you need — every example costs tokens.

---

## Key Insight — Day 5

> *"Zero-shot asks the model to guess what you want. Few-shot shows it. For anything where format and consistency matter, showing beats telling."*

---

---

# ✅ Day 6 — Saturday · Build Day

## Topic: Write 3 Few-shot Prompts
> [!NOTE]
> **Task:** Build and test 3 real few-shot prompts — classifier, extractor, summariser.
> **Model:** claude-haiku-4-5

---

### Prompt 1 — Customer Complaint Classifier

```
Classify the customer message below into exactly one category: 
Billing, Technical, Shipping, or General.
Respond with only the category name, nothing else.

Example 1:
Input: "I was charged twice for my subscription this month and need a refund."
Output: Billing

Example 2:
Input: "The app keeps crashing every time I try to log in."
Output: Technical

Now do this:
Input: "I can't figure out how to change my password."
Output:
```

**Result:** `Technical` — one word, nothing else. ✅

**Token cost:** 105 input tokens

---

### Prompt 2 — Info Extractor

```
Extract the name, date, and amount from the text below.
Respond in this exact format:
Name: [name]
Date: [date]
Amount: [amount]

Example 1:
Input: "John Smith placed an order on March 3rd 2024 for a total of $142.50."
Output:
Name: John Smith
Date: March 3rd 2024
Amount: $142.50

Example 2:
Input: "A payment of $89 was processed for Sarah Lee on the 14th of January."
Output:
Name: Sarah Lee
Date: 14th of January
Amount: $89

Now do this:
Input: "We received a invoice from Michael Torres dated July 22 2025 totalling $310."
Output:
```

**Result:**
```diff
+ Name: Michael Torres
+ Date: July 22 2025
+ Amount: $310
```
Exact format, no deviation. ✅

**Token cost:** 184 input tokens

---

### Prompt 3 — Article Summariser

```
Summarise the text below in exactly 2 sentences.
First sentence: the main point. Second sentence: the key supporting detail.
[2 examples provided]
```

**Input used:** McKinsey AI & jobs market paragraph

**Result:**
> *"Artificial intelligence is transforming the job market by automating significant portions of work across industries, with knowledge workers facing the biggest impact. A 2024 McKinsey report found that 30% of tasks could be automated with current AI technology, but new roles in AI oversight and human-AI collaboration are emerging to replace some displaced jobs."*

Clean 2-sentence structure, main point + supporting detail. ✅

**Token cost:** 384 input tokens

---

> [!IMPORTANT]
> **Token cost pattern across the 3 prompts: 105 → 184 → 384**
> More examples + longer inputs = more tokens consumed. Every example you add to a few-shot prompt multiplies cost across every API call. In production at scale (e.g. 50,000 tickets/month), this compounds fast.

> [!TIP]
> **Production rule:** Keep few-shot prompts minimal. Add examples only when accuracy is actually failing — not as a default. The classifier worked perfectly with just 2 examples and 105 tokens. That's the goal.

> [!NOTE]
> **Key observation:** The format instruction ("respond with only the category name, nothing else") was what controlled the output length — not the examples. Examples teach the pattern. Format instructions enforce the shape.

---

## Key Insight — Day 6

> *"Few-shot examples show the model what you want. Format instructions control how it responds. You need both — and in production, every token costs money, so use the minimum that works."*

---

---

# ✅ Day 7 — Sunday · Weekly Review

## What I Learned This Week

Before this week I thought prompting was simple — just typing instructions into a chat window. Now I understand it's a real engineering discipline with structure, tradeoffs, and measurable outcomes. Every prompt is a specification, and the quality of what you get back is a direct reflection of how precisely you defined what you wanted.

---

## What Clicked

> [!TIP]
> **Few-shot prompt construction** — knowing exactly how to structure examples (input → output pairs) to teach the model a pattern, and understanding that format instructions and examples serve different purposes: examples teach the task, instructions control the shape of the response.

## What Surprised Me

> [!IMPORTANT]
> **Temperature.** The idea that the same prompt at temperature 0 would produce word-for-word identical outputs across 4 runs — while temperature 1 generated completely different ideas each time, including lines no other run came close to — made the concept real in a way that reading about it never would have.

## What's Clear

> [!NOTE]
> Everything from this week is solid: tokens, temperature, context windows, zero-shot vs few-shot, Role + Task + Format structure, and how token cost compounds at scale in production.

---

## Week 1 — Key Insight

> *"Before this week I thought prompting was simple. Now I understand it's complex — and that complexity is exactly what makes it a skill worth building."*

---

## Resources I Used This Week

| Resource | What I Used It For |
|----------|--------------------|
| [Anthropic Prompt Engineering Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Day 1 — foundations |
| [learnprompting.org](https://learnprompting.org/docs/basics/few_shot) | Day 5 — zero-shot vs few-shot |
| Anthropic API Playground (Workbench) | Days 4 & 6 — temperature experiment + few-shot builds |

---

*Next up → Week 2: Core Techniques Every Prompt Engineer Knows 🚀*
