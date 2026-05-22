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
