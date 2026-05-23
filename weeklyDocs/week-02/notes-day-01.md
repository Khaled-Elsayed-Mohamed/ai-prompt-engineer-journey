# ✅ Day 1 — Monday · Learn Day

## What I Studied

> [!NOTE]
> **Topic:** Chain-of-Thought (CoT) Prompting
> 🔗 [learnprompting.org/docs/intermediate/chain_of_thought](https://learnprompting.org/docs/intermediate/chain_of_thought)

### Key Takeaways

Chain-of-Thought prompting tells the model to reason step by step *before* giving a final answer — dramatically improving accuracy on multi-step reasoning tasks.

**Two forms:**
- **Zero-shot CoT** — just add "Think step by step." No examples needed.
- **Few-shot CoT** — provide worked examples that show the reasoning process.

---

## Experiment — Same Problem, 3 Prompts

**Problem:** A store sells apples for $0.50 each and oranges for $0.75 each. If I buy 4 apples and 3 oranges, how much do I spend in total?

**Model:** claude-haiku-4-5 | **Temperature:** 0.7

### Version 1 — No CoT (Baseline)

```
A store sells apples for $0.50 each and oranges for $0.75 each.
If I buy 4 apples and 3 oranges, how much do I spend in total?
```

**Result:** Apples: 4 × $0.50 = $2.00 | Oranges: 3 × $0.75 = $2.25 | **Total: $4.25**

```diff
+ Input tokens:  54
+ Output tokens: 72
```

---

### Version 2 — Zero-shot CoT

```
A store sells apples for $0.50 each and oranges for $0.75 each.
If I buy 4 apples and 3 oranges, how much do I spend in total?
Think step by step.
```

**Result:**
> Step 1: Cost of apples = 4 × $0.50 = $2.00  
> Step 2: Cost of oranges = 3 × $0.75 = $2.25  
> Step 3: Total = $2.00 + $2.25 = **$4.25**

```diff
+ Input tokens:  60
+ Output tokens: 159
```

---

### Version 3 — Few-shot CoT

```
Solve the following math problem. Think through it step by step before giving the final answer.

Example:
Problem: A shirt costs $12 and pants cost $35. How much for 2 shirts and 1 pair of pants?
Reasoning: 2 shirts = 2 × $12 = $24. 1 pair of pants = $35. Total = $24 + $35 = $59.
Answer: $59

Now solve this:
Problem: A store sells apples for $0.50 each and oranges for $0.75 each. If I buy 4 apples and 3 oranges, how much do I spend in total?
```

> [!WARNING]
> The few-shot response shared the same `msg_id` as zero-shot — same API response captured twice, not a fresh call. Few-shot result not independently verified.

---

## Token Cost Comparison

| Version | Input Tokens | Output Tokens | Total |
|---------|-------------|---------------|-------|
| No CoT | 54 | 72 | 126 |
| Zero-shot CoT | 60 | 159 | 219 |
| Few-shot CoT | Higher | ~159 | Higher |

---

## Key Findings

> [!IMPORTANT]
> **CoT more than doubles output tokens.** Going from no CoT (72 tokens) to zero-shot CoT (159 tokens) is a 2.2× increase. At scale, that cost adds up.

> [!TIP]
> **"Think step by step" only costs 4 words.** It's the cheapest way to unlock reasoning — add it first before few-shot CoT.

> [!NOTE]
> **CoT didn't change the answer here — because the problem was simple.** CoT shines on hard tasks: complex word problems, multi-condition logic, code debugging.

---

## When to Use CoT

| Use CoT | Skip CoT |
|---------|----------|
| Multi-step math or logic | Simple classification |
| Code debugging | Straightforward extraction |
| Complex decision-making | Short factual answers |
| Reasoning with multiple conditions | Tasks where accuracy is already high |

---

## Interview Talking Point

> "Chain-of-Thought prompting forces the model to externalize its reasoning before committing to an answer. I've tested zero-shot CoT — just adding 'think step by step' — and compared it to no CoT. The trade-off is real: CoT more than doubles output tokens, so I only apply it where reasoning complexity warrants the cost."

---

## Key Insight — Day 1

> *"CoT isn't free — but on hard problems, the reasoning clarity it adds is worth the token cost."*
