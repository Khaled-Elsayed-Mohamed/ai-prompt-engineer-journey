# ✅ Day 2 — Tuesday · Build Day

## What I Built & Learned

> [!NOTE]
> **Topic:** Role Prompting & System Prompts (Theory + Build)
> 🔗 [docs.anthropic.com/en/docs/build-with-claude/prompt-engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

### The Core Idea

**Role prompting** tells the model who it is before it responds. A vague role does almost nothing — the model is "helpful assistant" by default. A *specific* role with constraints changes tone, depth, length, and content.

**System prompts** are how you deploy role prompting at scale. Instead of repeating instructions in every user message, you set them once in the system prompt and they apply to every turn in the conversation.

---

## Experiment — Same Question, 3 System Prompts

**User message (identical for all 3):** *Explain what a REST API is.*

**Model:** claude-sonnet-4-6

### Version A — No System Prompt

```
(no system prompt)
```

**Result:** Comprehensive multi-section response with headers, tables, HTTP method breakdown, real-world analogy, and "Why use REST APIs?" section.

```diff
+ Input tokens:  15
+ Output tokens: 509
```

---

### Version B — Vague Role

```
You are a helpful assistant.
```

**Result:** Nearly identical to Version A — same structure, same depth, slightly longer.

```diff
+ Input tokens:  22
+ Output tokens: 570
```

---

### Version C — Specific Role

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

## Token Cost Comparison

| Version | Input Tokens | Output Tokens | Total |
|---------|-------------|---------------|-------|
| No system prompt | 15 | 509 | 524 |
| Vague role ("helpful assistant") | 22 | 570 | 592 |
| Specific role with constraints | 62 | 227 | 289 |

---

## Key Findings

> [!IMPORTANT]
> **Vague roles do nothing — they cost tokens without changing behaviour.** "You are a helpful assistant" produced *more* output (570 vs 509 tokens). The model's default state is already "helpful assistant."

> [!TIP]
> **Specific instructions produce specific, predictable outputs.** Three instructions in Version C each did a separate job: the expertise framing set the depth, the analogy instruction shaped the content, and the word limit controlled the length.

> [!NOTE]
> **More input tokens in the system prompt can *reduce* total cost.** Version C used 47 more input tokens than Version A, but saved 282 output tokens. Output tokens cost more at scale — a well-scoped system prompt is often cheaper overall.

---

## Build — Customer Support System Prompt

**The prompt I wrote:**
```
You are a senior Customer support assistant for a SaaS tool.
You are professional but friendly.
Only answer questions about the product, and always end by asking 
if there's anything else you can help with.
```

### Test 1 — Off-topic question
**Input:** *"Explain what a REST API is."*  
**Output:** Correctly refused, redirected to product-related questions. ✅

### Test 2 — Product question
**Input:** *"Tell me more about your product."*  
**Output:** Asked clarifying questions — expected, because the system prompt has no product context. ⚠️

### Test 3 — Bug report
**Input:** *"My tool is bugging, can you help file a complaint?"*  
**Output:** Stayed in-scope, offered troubleshooting, asked for error details. ✅

---

## What's Missing (Production Readiness)

> [!WARNING]
> **The system prompt above has no product context.** It can stay in-scope but can't answer product questions. A production-ready version would include:
> - Product name and what it does
> - Key features the bot can speak to
> - Escalation path (e.g., "Direct to support@company.com")
> - Tone rules beyond "professional but friendly"
> - What to do when users push back

---

## Interview Talking Point

> "System prompts are how prompt engineering reaches production. I've tested the difference between vague and specific roles on the same user message — a vague role changed nothing and actually increased output tokens. A specific role with constraints cut output by 55% and produced exactly the content I asked for. In a real deployment, I'd treat the system prompt as a specification document: every instruction should have a purpose."

---

## Key Insight — Day 2

> *"Vague system prompts are worse than no system prompt — they waste tokens without changing behaviour. Only write system prompts when you have specific constraints to enforce."*
