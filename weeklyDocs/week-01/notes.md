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

## 🎯 Week 1 Key Takeaways

### What I Learned This Week

Before this week I thought prompting was simple — just typing instructions into a chat window. Now I understand it's a real engineering discipline with structure, tradeoffs, and measurable outcomes. Every prompt is a specification, and the quality of what you get back is a direct reflection of how precisely you defined what you wanted.

### Core Concepts Covered

- **Prompt Structure:** Role + Task + Format framework
- **Tokens:** How models chunk text and why it matters for cost/context
- **Temperature:** The tradeoff between consistency (0) and creativity (1)
- **Context Windows:** The model's working memory constraint
- **Zero-shot vs Few-shot:** When to show examples vs. asking the model to figure it out

### What Clicked Most

> [!TIP]
> **Few-shot prompt construction** — knowing exactly how to structure examples (input → output pairs) to teach the model a pattern, and understanding that format instructions and examples serve different purposes: examples teach the task, instructions control the shape of the response.

### What Surprised Me

> [!IMPORTANT]
> **Temperature.** The idea that the same prompt at temperature 0 would produce word-for-word identical outputs across multiple runs — while temperature 1 generated completely different ideas each time — made the concept real in a way that reading about it never would have.

### Biggest Insight

> *"Prompting isn't simple. It's complex — and that complexity is exactly what makes it a skill worth building."*

---

## 📚 Resources I Used This Week

| Resource | What I Used It For |
|----------|--------------------|
| [Anthropic Prompt Engineering Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Day 1 — foundations |
| [learnprompting.org](https://learnprompting.org/docs/basics/few_shot) | Day 5 — zero-shot vs few-shot |
| Anthropic API Playground (Workbench) | Days 4 & 6 — temperature experiment + few-shot builds |

---

## 📂 Daily Notes

Each day's detailed notes, experiments, and builds are in separate files:

- `notes-day-01.md` — GitHub setup + Anthropic docs intro
- `notes-day-02.md` — Role + Task + Format rewrite exercises
- `notes-day-03.md` — Tokens, temperature, context windows theory
- `notes-day-04.md` — Temperature 0 vs 1 creative writing experiment
- `notes-day-05.md` — Zero-shot vs few-shot prompting framework
- `notes-day-06.md` — Three few-shot prompt builds (classifier, extractor, summarizer)
- `notes-day-07.md` — Weekly reflection & key insights

---

*Next up → Week 2: Core Techniques Every Prompt Engineer Knows 🚀*
