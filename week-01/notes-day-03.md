# ✅ Day 3 — Wednesday · Learn Day

## Topic: Tokens, Temperature & Context Windows
> [!NOTE]
> **Sources:** Anthropic docs · OpenAI docs — tokens, temperature, context windows

---

### What I Studied

**Tokens**
A token is roughly a word or part of a word — the model reads and generates text in these chunks, not letter by letter. "ChatGPT" = 2 tokens. "I" = 1 token. Punctuation, spaces, and word fragments all count as tokens too.

**Temperature**
Temperature controls how random or predictable the model's output is. It's a dial between deterministic and creative.

**Context Windows**
The context window is the maximum amount of text (in tokens) the model can see at once. Everything outside it gets ignored — the model has no memory beyond it.

---

### Key Takeaways

```diff
+ Tokens are chunks — not words, not characters. Every API call costs tokens (input + output combined).
+ Temperature 0 = consistent and predictable. Temperature 1 = more varied and creative.
+ Context window = the model's "working memory". Exceed it and early content gets dropped.
```

---

> [!IMPORTANT]
> **Why tokens matter for prompt engineering:** Every model has a token limit per request. If your prompt + document + expected output exceeds it, the model either truncates your input or cuts off mid-response. Knowing this shapes how you structure long prompts.

> [!TIP]
> **Rule of thumb for temperature:**
> Use **0** for accuracy-critical tasks — classification, extraction, code review.
> Use **0.7–1** for creative tasks — writing, brainstorming, idea generation.
> Most production prompts live between **0 and 0.5**.

> [!NOTE]
> **Context window in practice:** If you paste a long document and the model "forgets" something from the beginning, it's not hallucinating — it may have simply run out of context. This is why chunking long inputs is a core prompt engineering skill.

---

## Key Insight — Day 3

> *"The model doesn't read your prompt the way you do — it processes tokens, works within a fixed memory window, and adjusts its creativity based on temperature. Understanding these three constraints changes how you design every prompt."*
