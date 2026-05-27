# 🔨 Week 2 · Day 5 — Prompt Chaining

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Learn prompt chaining — breaking a complex task into a sequence of smaller, connected prompts. This is the core architecture behind most real AI products.

---

## What is Prompt Chaining?

A single prompt has a ceiling. When a task is too complex, too long, or involves multiple distinct steps, you hit that ceiling fast. Prompt chaining is the solution: break the work into smaller prompts where the output of one becomes the input of the next.

It's the difference between asking a contractor to "build me a house" vs. giving an architect a brief, getting plans from a designer, then handing specs to a builder. Same outcome — much better result.

---

## Why Chaining Works

**Separation of concerns.** Each prompt does one thing well. A prompt that extracts data doesn't also need to reformat it. A prompt that rewrites tone doesn't also need to summarise content.

**Easier debugging.** If the final output is wrong, you can look at each step and find exactly where it broke down.

**Better outputs.** Models perform best when the task is clearly scoped. Narrow prompts produce more consistent, accurate results.

---

## Experiment: 3-Step Chain vs. Single Prompt

**Task:** Take a customer complaint email and produce a professional reply.

### Single Prompt Approach

```
You are a customer support agent. Read this email and write a professional reply.

[email pasted in]
```

**Result:** Decent but generic. The model tried to do everything at once — read intent, extract specifics, match tone, draft reply — and average everything together.

---

### Chained Approach (3 Steps)

**Prompt 1 — Extract**
```
Read this customer email and extract:
1. The main problem they experienced
2. Their emotional tone (frustrated / neutral / positive)
3. Any specific details mentioned (order number, product, dates)

Return as JSON with keys: problem, tone, details

[email pasted in]
```

**Output:**
```json
{
  "problem": "Order arrived damaged and missing one item",
  "tone": "frustrated",
  "details": {
    "order_number": "ORD-4821",
    "product": "Standing desk",
    "date_received": "Monday"
  }
}
```

---

**Prompt 2 — Draft**
```
Using this extracted info, write a first draft of a customer support reply.
Match the tone to the situation: the customer is frustrated.

Info: [Prompt 1 output pasted in]

Requirements:
- Acknowledge the problem first
- Don't make excuses
- State exactly what will happen next
- Friendly but professional tone
```

---

**Prompt 3 — Polish**
```
Review this customer support reply and improve it.

Check for:
1. Does it open by acknowledging the customer's frustration?
2. Is the next step clearly stated with a timeframe?
3. Is the language warm but not overly casual?
4. Is it under 150 words?

[Draft from Prompt 2 pasted in]

If changes are needed, make them. If it's already strong, return it as-is.
```

---

## Results Comparison

| Approach | Quality | Consistency | Debuggability |
|----------|---------|-------------|---------------|
| Single prompt | ⚠️ Variable | ❌ Inconsistent | ❌ Hard |
| 3-step chain | ✅ Strong | ✅ Reliable | ✅ Easy |

The chain produced a better reply every time — because each prompt was accountable for exactly one job.

---

## Key Insight

> The "extract first" pattern is one of the most powerful in prompt engineering. When you separate understanding (what is the input saying?) from generating (what should the output be?), both steps improve dramatically.

This pattern shows up everywhere in production AI systems.

---

## What's Next

Day 6 covers documentation — turning today's experiment into a portfolio-ready write-up. Day 7 is the weekly reflection and wrap.
