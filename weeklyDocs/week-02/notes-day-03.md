# ✅ Day 3 — Wednesday · Learn Day

## What I Studied

> [!NOTE]
> **Topic:** Role Prompting & System Prompts (Learnings from Personal Quiz)
> 🔗 [docs.anthropic.com](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
> 🔗 [learnprompting.org](https://learnprompting.org)

### Key Takeaways

Role prompting assigns Claude a specific persona to direct behavior and get better results. Instead of asking "help me test code," you say "You are a professional mobile app tester who works well in teams."

**System Prompts vs User Messages:**
- **System prompt** = sits at the top, applies globally to every response, has higher priority
- **User message** = the specific task/question you ask in the moment

The system prompt sets the foundation; user messages direct specific tasks. Order matters: the agent reads the system prompt first.

---

## When I Learned It Best

Through hands-on testing, I confirmed:

**Vague roles (like "helpful assistant") waste tokens without changing behavior.** Testing the same question with and without a system prompt showed the vague role produced *more* output (570 vs 509 tokens) with no difference in quality.

**Specific roles produce specific, predictable outputs.** When I added constraints ("professional backend engineer explaining to a junior developer, keep it under 150 words"), the response dropped from 509 tokens to 227 tokens — clearer, more focused, better scoped.

---

## My Understanding of the Technique

**Role prompting works because:**
1. It constrains the model's response space — the role narrows what it thinks is appropriate
2. It sets tone and depth — a "senior engineer" explains differently than a "casual expert"
3. It's composable — multiple constraints in one system prompt each affect the output independently

**What I got wrong initially:**
- I thought system prompts and user messages had equal priority — they don't. System prompt wins.
- I thought role prompting only mattered for personality — it also controls depth, length, and technical level.

**What clicked hardest:**
- Token efficiency. A specific system prompt can *save* tokens overall (more input, far fewer output = cheaper).
- The separation of concerns: system prompt sets the persona; user message directs the specific task.

---

## Practical Example I Built

**System Prompt:**
```
You are a senior JavaScript code reviewer.
You are professional and friendly.
You always explain why.
```

This works because:
- "Senior JavaScript code reviewer" = sets expertise level
- "Professional and friendly" = sets tone
- "Always explain why" = behavioral constraint

Each instruction does one job. If I removed "explain why," the reviews would be shorter and less educational. If I removed "professional and friendly," they'd sound harsh.

---

## Real-World Application

**Where I'd use this:**
- A chatbot that needs consistent tone across 1000s of conversations
- A classifier that needs to make decisions the same way every time
- A content generator that must match a specific style guide

**Where I'd skip it:**
- One-off questions ("What's 2+2?")
- Tasks where the model's default behavior is already good
- When I'm experimenting and want maximum flexibility

---

## What Surprised Me Most

> [!IMPORTANT]
> **System prompts have higher priority than user messages.** If I tell the system prompt "be professional" and then ask "be sarcastic," the model defaults to professional. This isn't a weakness — it's the design. The system prompt is the contract with the user; user messages are just tasks within that contract.

---

## Interview Talking Point

> "I tested the difference between vague and specific system prompts on the exact same user message. 'You are a helpful assistant' changed nothing and cost more tokens — the model's default state is already helpful. But 'You are a senior backend engineer explaining to a junior who's never seen APIs, use an analogy, under 150 words' cut output tokens by 55% and produced exactly what I asked for. System prompts are specifications, not suggestions."

---

## How This Connects to Tomorrow (Day 4)

Tomorrow I'm building a multi-technique prompt that combines what I've learned:
- Day 1: Chain-of-Thought for reasoning
- Day 2: Role prompting + system prompts for consistency
- Day 3 (today): Understanding *why* they work and when to apply them
- Day 4: Build something that uses multiple techniques together

---

## Key Insight — Day 3

> *"System prompts aren't decorative — they're the foundation. Everything a model does flows from the system prompt first, then the user message. Get the system prompt right, and the rest becomes easier."*

---

## Resources Used

- Anthropic API docs — system message structure
- learnprompting.org — role prompting guide
- Claude in Workbench — hands-on testing with different prompts
- Personal experimentation — comparing outputs side-by-side
