# 🧠 Week 2 — Core Techniques Every Prompt Engineer Knows

**AI Prompt Engineer Journey · Khaled**

> [!IMPORTANT]
> **Goal this week:** Learn the 4–5 techniques that appear in almost every real-world prompt engineering job. Move from "I can write a prompt" to "I understand *why* prompts work."

---

## 📊 Progress Tracker

| Day | Mode | Theme | Status |
|-----|------|-------|--------|
| Day 1 | 📖 Learn | Chain-of-Thought Prompting | ✅ Done |
| Day 2 | 🔨 Build | Role Prompting & System Prompts | ✅ Done |
| Day 3 | 📖 Learn | System Prompt Deep Dive & Testing | ✅ Done |
| Day 4 | 🔨 Build | Build Customer Support System Prompt | ✅ Done |
| Day 5 | 🔨 Build | Prompt Chaining — 3-Step Chain | ✅ Done |
| Day 6 | 📝 Doc | Document & Push to GitHub | ✅ Done |
| Day 7 | 🔁 Review | Weekly Reflection | ✅ Done |

---

## 🎯 Week 2 Key Concepts

### Day 1 — Chain-of-Thought Prompting

**What is CoT?** Asking the model to reason step by step *before* giving a final answer. Dramatically improves accuracy on multi-step reasoning tasks.

**Key Finding:** Zero-shot CoT (just adding "Think step by step") more than doubled output tokens (72 → 159) but is the cheapest way to unlock reasoning. Only use it when the task genuinely requires step-by-step logic.

**Token Trade-off:**
- No CoT: 126 tokens total
- Zero-shot CoT: 219 tokens total
- Worth the cost when: complex logic, code debugging, multi-condition reasoning

---

### Day 2 — Role Prompting & System Prompts

**What is a System Prompt?** A special instruction layer that sits above user messages. It configures how the model behaves globally — before the user says anything.

**Critical Finding:** Vague system prompts (like "You are a helpful assistant") waste tokens *without changing behavior*. The model's default state is already helpful. Only write system prompts when you have specific constraints to enforce.

**Real Data:**
- No system prompt: 524 tokens
- Vague role ("helpful assistant"): 592 tokens (worse!)
- Specific role + constraints: 289 tokens (55% reduction)

---

### Day 3 — System Prompt Deep Dive

**What I Discovered:** System prompts have higher priority than user messages. If you set "be professional" in the system prompt and then ask "be sarcastic" in a user message, the model defaults to professional. The system prompt is the contract.

**Practical Understanding:**
- Role prompting works because it constrains the response space
- Multiple constraints in one system prompt each do separate jobs
- Token efficiency: a well-scoped system prompt often *saves* tokens overall

---

### Day 4 — Building a Real System Prompt (Notion Support Bot)

**What I Built:** A customer support system prompt for a SaaS tool (Notion) that handles 5 diverse scenarios: off-topic questions, vague product questions, technical issues, angry escalations, and feature requests.

**Evolution Process:**
- **v1:** Initial prompt (passed 4/5 tests, failed on crisis handling)
- **v2:** Added CRITICAL ISSUES escalation path (immediate escalation for data loss/security concerns)
- **v3:** Refined tone + added help docs references + "explain the why" instruction (all 5 tests pass)

**Test Results:** ✅ All 5 tests pass

---

### Day 5 — Prompt Chaining

**What is Chaining?** Breaking a complex task into a sequence of smaller prompts where the output of each step feeds into the next. The backbone of most production AI systems.

**Key Pattern — Extract First:** Separating "what is the input saying?" from "what should the output be?" consistently improves both steps. A prompt that extracts structured data doesn't also need to generate a response.

**Result:** A 3-step customer reply chain (extract → draft → polish) produced more consistent, higher-quality output than a single all-in-one prompt.

---

### Day 6 — Documentation

**What Makes AI Documentation Portfolio-Ready:**
- Lead with the problem, not the solution
- Show your reasoning — explain *why* each version changed
- Include failure — v1 → v2 evolution is more credible than "here's the finished prompt"
- Keep it under two pages

---

### Day 7 — Weekly Reflection

**Biggest insight:** System prompts are specification documents. Every line should have a purpose. Vague prompts cost more and produce less.

**Confidence at end of week:**
- Chain-of-Thought: 7/10
- System prompts: 8/10
- Prompt chaining: 7/10
- Portfolio documentation: 8/10

---

## 📂 Daily Notes

- `notes-day-01.md` — Chain-of-Thought theory + token experiments
- `notes-day-02.md` — Role prompting theory + system prompt experiments
- `notes-day-03.md` — Deep dive on system prompts + practical insights
- `notes-day-04.md` — Built Notion support system prompt (v1→v2→v3), all 5 tests pass ✅
- `notes-day-05.md` — Prompt chaining: 3-step customer reply chain experiment
- `notes-day-06.md` — Portfolio documentation write-up
- `notes-day-07.md` — Weekly reflection + confidence check

**Artifacts:**
- `prompts/notion-support-system-prompt.md` — Final system prompt + evolution log

---

## 🔑 Week 2 Interview Talking Points

**On Chain-of-Thought:**
> "I tested zero-shot CoT on a simple math problem. It more than doubled output tokens but didn't change the answer because the problem was too simple. CoT's value appears on harder tasks — multi-step logic, code debugging, complex word problems. I only apply it where reasoning complexity warrants the token cost."

**On System Prompts:**
> "I tested the difference between vague and specific roles on the exact same user message. 'You are a helpful assistant' changed nothing and cost more tokens than no system prompt at all. A specific role with constraints cut output by 55% and produced exactly what I asked for."

**On Prompt Chaining:**
> "I built a 3-step chain that extracts structured data from a customer email, drafts a reply, then polishes tone. The extract-first pattern consistently outperformed a single all-in-one prompt — because each step is accountable for exactly one job."

---

## 📚 Resources Used This Week

| Resource | What I Used It For |
|----------|--------------------|
| [Anthropic Prompt Engineering Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | System prompts section |
| [learnprompting.org](https://learnprompting.org) | Chain-of-Thought & role prompting guides |
| Claude Workbench | Hands-on testing of all techniques |

---

## 💡 Week 2 Biggest Insights

> *"System prompts are specification documents. Every line should do exactly one job."*

> *"Separating 'extract' from 'generate' consistently produces better outputs than combining both in one prompt."*

---

*Next up → Week 3: Working With the API 🚀*
