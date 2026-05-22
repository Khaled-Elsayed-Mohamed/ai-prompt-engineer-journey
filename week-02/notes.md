# Week 02 — Core Techniques Every Prompt Engineer Knows

## Progress Tracker

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | Chain-of-Thought Prompting | ✅ Done |
| Day 2 | Role Prompting & System Prompts | ⬜ Pending |
| Day 3 | Prompt Chaining | ⬜ Pending |
| Day 4 | Build Day — Multi-technique prompt | ⬜ Pending |
| Day 5 | Peer review + refine | ⬜ Pending |
| Day 6 | Document & push to GitHub | ⬜ Pending |
| Day 7 | Weekly reflection | ⬜ Pending |

---

## Day 1 — Chain-of-Thought (CoT) Prompting

> [!NOTE]
> **What is CoT?** Chain-of-Thought prompting tells the model to reason step by step *before* giving a final answer — dramatically improving accuracy on multi-step reasoning tasks.

### The Core Idea

Without CoT, the model jumps straight to an answer. With CoT, it shows its work — and that visible reasoning process leads to fewer errors, especially when problems have multiple steps or conditions.

There are two forms:

- **Zero-shot CoT** — just add `"Think step by step."` to the end of your prompt. No examples needed.
- **Few-shot CoT** — provide an example that shows the reasoning process, then ask the model to follow the same pattern.

---

### Experiment — Same Problem, 3 Prompts

**Problem used:** *A store sells apples for $0.50 each and oranges for $0.75 each. If I buy 4 apples and 3 oranges, how much do I spend in total?*

**Model:** claude-haiku-4-5 | **Temperature:** 0.7

---

#### Version 1 — No CoT (Baseline)

```
A store sells apples for $0.50 each and oranges for $0.75 each.
If I buy 4 apples and 3 oranges, how much do I spend in total?
```

**Result:**
> Apples: 4 × $0.50 = $2.00 | Oranges: 3 × $0.75 = $2.25 | **Total: $4.25**

```diff
+ Input tokens:  54
+ Output tokens: 72
```

---

#### Version 2 — Zero-shot CoT

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

#### Version 3 — Few-shot CoT

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
> **Experiment note:** The few-shot CoT response in the uploaded file shared the same `msg_id` as the zero-shot CoT response — indicating the same API response was captured twice rather than a fresh call being made. The few-shot result was not independently verified in this session. **Always capture and label each API response immediately after the call.**

---

### Token Cost Comparison

| Version | Input Tokens | Output Tokens | Total |
|---------|-------------|---------------|-------|
| No CoT | 54 | 72 | 126 |
| Zero-shot CoT | 60 | 159 | 219 |
| Few-shot CoT | Higher (example adds tokens) | ~159 | Higher |

---

### Key Findings

> [!IMPORTANT]
> **CoT more than doubles output tokens.** Going from no CoT to zero-shot CoT increased output from 72 → 159 tokens. At scale across thousands of API calls, that cost adds up significantly.

> [!TIP]
> **"Think step by step" only costs 4 words of input.** Zero-shot CoT is the cheapest way to unlock reasoning — add it first before reaching for few-shot CoT.

> [!NOTE]
> **CoT didn't change the answer here — and that's expected.** This problem was simple arithmetic. CoT's value appears on harder tasks: complex word problems, multi-condition logic, code debugging, or anything where a wrong intermediate step would lead to a wrong final answer.

---

### When to Use CoT

| Use CoT | Skip CoT |
|---------|----------|
| Multi-step math or logic | Simple classification |
| Code debugging | Straightforward extraction |
| Complex decision-making | Short factual answers |
| Reasoning with multiple conditions | Tasks where accuracy is already high |

---

### Interview Talking Point

> "Chain-of-Thought prompting forces the model to externalise its reasoning before committing to an answer. I've tested zero-shot CoT — just adding 'think step by step' — and few-shot CoT with worked examples. The trade-off is real: CoT more than doubles output tokens, so I only apply it where reasoning complexity warrants the cost."
