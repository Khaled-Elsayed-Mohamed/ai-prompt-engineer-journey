# Week 02 — Core Techniques Every Prompt Engineer Knows

## Progress Tracker

| Day | Topic | Status |
|-----|-------|--------|
| Day 1 | Chain-of-Thought Prompting | ✅ Done |
| Day 2 | Role Prompting & System Prompts | ✅ Done |
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

---

### Confirmation Quiz

**Q1. No CoT used 54 input tokens. Zero-shot CoT used 60. Why did adding 4 words cost more input tokens?**
> More words in the prompt = more input tokens. "Think step by step" is 4 words ≈ 6 tokens. Input tokens are everything you *send* — adding any text increases them.

**Q2. Both zero-shot CoT and few-shot CoT got the same answer ($4.25). Does that mean CoT added no value?**
> No. The problem was too simple for CoT to matter. CoT's value shows on harder tasks — multi-step logic, complex word problems, code debugging — where skipping intermediate reasoning leads to wrong final answers.

**Q3. Zero-shot CoT used 159 output tokens vs 72 without CoT. Is the cost always worth it?**
> No. CoT more than doubled output tokens. It's only worth the cost when the task genuinely requires step-by-step reasoning. For classification, extraction, or simple factual answers — skip it.

**Q4. The zero-shot and few-shot CoT responses shared the same `msg_id`. What happened?**
> The same API response was pasted twice instead of running a fresh call for the few-shot version. Every API response has a unique ID — a duplicate ID means a duplicate response. Lesson: capture and label each response immediately after the call.

---

## Day 2 — Role Prompting & System Prompts

> [!NOTE]
> **What is a System Prompt?** A system prompt is a special instruction layer that sits *above* the user message in the API. It configures how the model behaves globally — before the user says anything. Every AI product you've used has one.

### The Core Idea

**Role prompting** tells the model who it is before it responds. A vague role does almost nothing — the model is "helpful assistant" by default. A *specific* role with constraints changes tone, depth, length, and content.

**System prompts** are how you deploy role prompting at scale. Instead of repeating instructions in every user message, you set them once in the system prompt and they apply to every turn in the conversation.

---

### Experiment — Same Question, 3 System Prompts

**User message (identical for all 3):** *Explain what a REST API is.*

**Model:** claude-sonnet-4-6

---

#### Version A — No System Prompt

```
(no system prompt)
```

**Result:** A comprehensive, multi-section response with headers, tables, HTTP method breakdown, real-world analogy, and a "Why use REST APIs?" section.

```diff
+ Input tokens:  15
+ Output tokens: 509
```

---

#### Version B — Vague Role

```
You are a helpful assistant.
```

**Result:** Nearly identical to Version A — same structure, same depth, slightly longer.

```diff
+ Input tokens:  22
+ Output tokens: 570
```

---

#### Version C — Specific Role

```
You are a senior backend engineer explaining concepts to a junior developer 
who is smart but has never worked with APIs before. Use a real-world analogy 
in your explanation. Keep it under 150 words.
```

**Result:** Short, focused response. Led with the restaurant analogy (you = client, waiter = API, kitchen = server). Covered GET/POST/PUT/DELETE. Stayed concise.

```diff
+ Input tokens:  62
+ Output tokens: 227
```

---

### Token Cost Comparison

| Version | Input Tokens | Output Tokens | Total |
|---------|-------------|---------------|-------|
| No system prompt | 15 | 509 | 524 |
| Vague role | 22 | 570 | 592 |
| Specific role | 62 | 227 | 289 |

---

### Key Findings

> [!IMPORTANT]
> **Vague roles do nothing — they cost tokens without changing behaviour.** "You are a helpful assistant" produced *more* output than no system prompt at all (570 vs 509 tokens). The model's default state is already "helpful assistant."

> [!TIP]
> **Specific instructions produce specific, predictable outputs.** Three instructions in Version C each did a separate job: the expertise framing set the depth, the analogy instruction shaped the content, and the word limit controlled the length. One instruction → one effect.

> [!NOTE]
> **More input tokens in the system prompt can *reduce* total cost.** Version C used 47 more input tokens than Version A, but saved 282 output tokens. Output tokens cost more than input tokens at scale — a well-scoped system prompt is often cheaper overall.

---

### Build — Customer Support System Prompt

**Your system prompt:**
```
You are a senior Customer support assistant for a SaaS tool.
You are professional but friendly.
Only answer questions about the product, and always end by asking 
if there's anything else you can help with.
```

**Test 1 — Off-topic question:** *"Explain what a REST API is."*
> The bot correctly refused, redirected to product-related questions, and asked if there was anything else it could help with. ✅

**Test 2 — Product question:** *"Tell me more about your product."*
> The bot asked clarifying questions rather than answering — because the system prompt didn't include any product context. ⚠️ This is expected behaviour, not a failure — the model correctly avoided fabricating product details it was never given.

**Test 3 — Bug report:** *"My tool is bugging, can you help file a complaint?"*
> The bot stayed in scope, offered to troubleshoot, asked for specific details (error messages, steps to reproduce). ✅

---

### What's Missing in a Production System Prompt

> [!WARNING]
> **The system prompt above has no product context.** It can stay in-scope but can't actually answer product questions. A production-ready version would include:
> - Product name and what it does
> - Key features the bot can speak to
> - Escalation path (e.g. "If you can't help, direct the user to support@company.com")
> - Tone rules beyond "professional but friendly" (e.g. no emojis, no markdown, always use first name)
> - What to do when the user pushes back

---

### Interview Talking Point

> "System prompts are how prompt engineering reaches production. I've tested the difference between vague and specific roles on the same user message — a vague role like 'you are a helpful assistant' changed nothing and actually increased output tokens. A specific role with constraints cut output by 55% and produced exactly the content I asked for. In a real deployment, I'd treat the system prompt as a specification document: every instruction should have a purpose."

---

### Confirmation Quiz

**Q1. "You are a helpful assistant" produced 570 output tokens — more than no system prompt (509). What does that tell you about vague roles?**
> Vague roles do nothing. The model's default state is already "helpful assistant." Adding that phrase is wasted tokens with no behaviour change. A role only changes output when it's specific enough to constrain the model.

**Q2. Version C used 3 instructions and each caused a different effect. What did each one do?**
> "Senior backend engineer explaining to a junior dev" → set the expertise level and tone. "Use a real-world analogy" → caused the restaurant analogy to appear. "Keep it under 150 words" → drove the output from 509 down to 227 tokens. One instruction = one effect.

**Q3. The customer support bot asked clarifying questions when asked about the product. Success or failure?**
> Success. The bot correctly avoided fabricating product details it was never given. A model that makes up product information would be far worse. The missing piece is product context in the system prompt — not a flaw in the bot's behaviour.

**Q4. What's missing from the customer support system prompt that would make it production-ready?**
> The product itself — name, what it does, key features. Without that context the bot can stay in-scope but can't actually answer product questions. A production system prompt would also include an escalation path, specific tone rules, and instructions for edge cases.
