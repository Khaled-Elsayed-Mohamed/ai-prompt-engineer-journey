# 🔁 Week 2 · Day 7 — Weekly Reflection

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Consolidate everything from Week 2. Write the honest version of what I learned — not a summary, but an actual account of what landed, what confused me, and what I'd do differently.

---

## What Actually Happened This Week

Week 2 was denser than Week 1. The techniques weren't harder conceptually, but the gap between understanding them and being able to use them well is bigger than I expected.

Chain-of-Thought, role prompting, system prompts, and prompt chaining — I can explain all four. I can also use all four. But I wouldn't say I'm fluent yet. Fluency comes from doing it on real problems dozens of times, not four times in a tutorial week.

That's not a failure observation — it's an honest one. Week 2 gave me the vocabulary and the first working examples. Fluency gets built across the next ten weeks.

---

## What Landed Most

**System prompts as specification documents.** This framing clicked for me and I've already started thinking about every AI interaction differently. Before this week I thought of system prompts as optional. Now I see them as the contract between the designer and the model — every line should earn its place.

The experiment comparing vague vs. specific roles was the most concrete moment of the week. Seeing a 55% token reduction from specificity wasn't abstract theory — it was data I collected myself.

---

## What's Still Fuzzy

**Prompt chaining at scale.** The 3-step chain I built on Day 5 was clean because I designed it. In a real product, chains might have 5+ steps, conditional branches, and error handling. I understand the concept but I haven't stress-tested it yet.

**When CoT isn't worth it.** I understand the principle (only use it when the task genuinely requires multi-step reasoning). But my instinct for where that line sits is still developing.

---

## What I'd Do Differently

I'd build the chain earlier in the week. Day 5 felt slightly rushed — the concept deserved more experiment time. Next time I'd swap Days 4 and 5 so chaining gets a full build day before documentation.

---

## Confidence Check

| Skill | Confidence |
|-------|-----------|
| Using Chain-of-Thought on the right tasks | 7/10 |
| Writing effective system prompts from scratch | 8/10 |
| Building and explaining a multi-step prompt chain | 7/10 |
| Documenting AI work for a portfolio | 8/10 |

---

## One Sentence per Day

1. **Monday:** CoT literally doubles output tokens — use it only when reasoning complexity warrants the cost.
2. **Tuesday:** Vague system prompts waste tokens without changing behavior; specificity is the only thing that changes outcomes.
3. **Wednesday:** System prompts have higher priority than user messages — they're the contract, not a suggestion.
4. **Thursday:** A system prompt that handles crises differently from general questions is more useful than one that handles everything the same way.
5. **Friday:** Separating "extract" from "generate" consistently produces better outputs than combining both in one prompt.
6. **Saturday:** Documentation is engineering — explaining why a prompt changed is more valuable than showing the prompt that works.
7. **Sunday:** Fluency is built through repetition, not exposure. Week 2 gave me tools; the next ten weeks will make them feel natural.

---

## What I'm Taking Into Week 3

Week 3 moves from the playground into actual API calls. This is the step that separates "I use AI" from "I build with AI." It's the technical infrastructure behind everything we've built conceptually.

I'm not nervous about the code — my background is iOS/Swift, so Python syntax and API calls are familiar territory. What I'm looking forward to is seeing prompt techniques applied in code: system messages in a real API structure, conversation history, output parsing.

**Week 2 done. Moving forward.** 🚀
