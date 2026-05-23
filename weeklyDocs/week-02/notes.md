# 🧠 Week 2 — Core Techniques Every Prompt Engineer Knows

**📅 May 2026 &nbsp;·&nbsp; AI Prompt Engineer Journey &nbsp;·&nbsp; Khaled**

> [!IMPORTANT]
> **Goal this week:** Learn the 4–5 techniques that appear in almost every real-world prompt engineering job. Move from "I can write a prompt" to "I understand *why* prompts work."

---

## 📊 Progress Tracker

| Day | Mode | Theme | Status |
|-----|------|-------|--------|
| Mon — Day 1 | 📖 Learn | Chain-of-Thought Prompting | ✅ Done |
| Tue — Day 2 | 🔨 Build | Role Prompting & System Prompts | ✅ Done |
| Wed — Day 3 | 📖 Learn | System Prompt Deep Dive & Testing | ✅ Done |
| Thu — Day 4 | 🔨 Build | Build Customer Support System Prompt | ✅ Done |
| Fri — Day 5 | 🔨 Build | Refine & Peer Review | ⏳ Pending |
| Sat — Day 6 | 📝 Doc | Document & Push to GitHub | ⏳ Pending |
| Sun — Day 7 | 🔁 Review | Weekly Reflection | ⏳ Pending |

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

### Day 3 — System Prompt Deep Dive & Quiz-Based Learning

**What I Discovered:** System prompts have higher priority than user messages. If you set "be professional" in the system prompt and then ask "be sarcastic" in a user message, the model defaults to professional. The system prompt is the contract.

**Practical Understanding:**
- Role prompting works because it constrains the response space
- Multiple constraints in one system prompt each do separate jobs
- Token efficiency: a well-scoped system prompt often *saves* tokens overall

**Learning Method:** Confirmed understanding through quiz questions (what's role prompting? how do system prompts differ from user prompts? when would you use them?). This deepened the concepts from Day 2.

---

### Day 4 — Building a Real System Prompt (Notion Support Bot)

**What I Built:** A customer support system prompt for a SaaS tool (Notion) that handles 5 diverse scenarios: off-topic questions, vague product questions, technical issues, angry escalations, and feature requests.

**Evolution Process:**
- **v1:** Initial prompt (passed 4/5 tests, failed on crisis handling)
- **v2:** Added CRITICAL ISSUES escalation path (immediate escalation for data loss/security concerns)
- **v3:** Refined tone + added help docs references + "explain the why" instruction (all 5 tests pass)

**Test Results:** ✅ All 5 tests pass
- Off-topic redirection works
- Clarifying questions prevent bad advice
- Technical troubleshooting provides specific solutions
- Crisis escalation is immediate (not stalling)
- Feature requests handled with workarounds + feedback channel

**Key Finding:** System prompts need different modes for different situations. The CRITICAL ISSUES section forces immediate escalation for emergencies, while everything else uses troubleshooting/clarification. That branching logic changed behavior from "helpful but slow" to "helpful AND fast."

---

## 📂 Daily Notes

Each day's detailed notes, experiments, and builds are in separate files:

- `notes-day-01.md` — Chain-of-Thought theory + token experiments
- `notes-day-02.md` — Role prompting theory + system prompt experiments
- `notes-day-03.md` — Deep dive on understanding system prompts + practical insights
- `notes-day-04.md` — Built Notion support system prompt (v1→v2→v3), tested 5 scenarios, all pass ✅
- `notes-day-05.md` — Refine & peer review (coming soon)
- `notes-day-06.md` — Document & publish (coming soon)
- `notes-day-07.md` — Weekly reflection (coming soon)

**Artifacts Created:**
- `prompts/notion-support-system-prompt.md` — Final system prompt + adaptations guide

---

## 🔑 Week 2 Interview Talking Points

**On Chain-of-Thought:**
> "I tested zero-shot CoT on a simple math problem. It more than doubled output tokens but didn't change the answer because the problem was too simple. CoT's value appears on harder tasks — multi-step logic, code debugging, complex word problems. I only apply it where reasoning complexity warrants the token cost."

**On System Prompts:**
> "I tested the difference between vague and specific roles on the exact same user message. 'You are a helpful assistant' changed nothing and cost more tokens than no system prompt at all. A specific role with constraints cut output by 55% and produced exactly what I asked for. In a real deployment, I'd treat the system prompt as a specification document: every instruction should have a purpose."

**On Building Real System Prompts:**
> "I built a customer support system prompt and tested it with 5 diverse scenarios: off-topic questions, vague product questions, technical issues, angry users, and feature requests. The first version failed on crisis handling — upset users felt stalled. I identified that the prompt needed an immediate-escalation path for critical issues (data loss, account access). Version 2 fixed that. Then I refined tone and added help doc references in Version 3. All 5 tests pass. The key insight: system prompts are specifications. Each instruction does a specific job — I wrote the escalation section specifically to prevent stalling upset users."

---

## 📚 Resources Used This Week

| Resource | What I Used It For |
|----------|--------------------|
| [Anthropic Prompt Engineering Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | System prompts section |
| [learnprompting.org](https://learnprompting.org) | Chain-of-Thought & role prompting guides |
| Claude Workbench | Hands-on testing of all techniques |
| Personal experimentation | Comparing outputs side-by-side, measuring tokens |

---

## 🎯 What's Next (Week 3)

Week 3 builds on these core techniques:
- **Prompt chaining:** Breaking big tasks into smaller, sequenced prompts
- **Evaluation:** How to measure if a prompt actually works
- **Portfolio project #1:** Build something real that uses these techniques

---

## 💡 Week 2 Biggest Insights

> *"System prompts aren't decorative — they're the foundation. Everything a model does flows from the system prompt first, then the user message. Get the system prompt right, and the rest becomes easier."*

> *"System prompts are specification documents. Every line should do exactly one job. Test your assumptions — building the support bot revealed that crisis handling needed its own path, not buried in general troubleshooting logic."*

---

## ✅ Week 2 Summary

**Completed:**
- ✅ Learned Chain-of-Thought prompting (theory + experiments)
- ✅ Learned role prompting & system prompts (theory + experiments)
- ✅ Deep-dived on system prompts through quiz-based learning
- ✅ Built a real Notion support system prompt (v1→v2→v3)
- ✅ Tested 5 diverse scenarios (all pass)
- ✅ Documented findings & interview talking points

**Remaining:**
- ⏳ Day 5: Refine & peer review
- ⏳ Day 6: Final documentation push
- ⏳ Day 7: Weekly reflection

---

*Next up → Day 5: Refine & Peer Review 🚀*
