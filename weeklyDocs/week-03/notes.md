# 🧠 Week 3 — Working With the API

**AI Prompt Engineer Journey · Khaled**

> [!IMPORTANT]
> **Goal this week:** Move from the playground to actually calling the API in code. This is the step that separates "I use AI" from "I build with AI."

---

## 📊 Progress Tracker

| Day | Mode | Theme | Status |
|-----|------|-------|--------|
| Day 1 | 📖 Learn | Anthropic API Quickstart — Read-Through | ✅ Done |
| Day 2 | 🔨 Build | First API Call from Python | ✅ Done |
| Day 3 | 📖 Learn | System Messages & Conversation Structure | ✅ Done |
| Day 4 | 🔨 Build | Script with System Prompt + User Input | ✅ Done |
| Day 5 | 📖 Learn | Max Tokens, Output Control, JSON Formatting | ✅ Done |
| Day 6 | 🔨 Build | Structured JSON Output Script | ✅ Done |
| Day 7 | 🔁 Review | Clean Up, Comment, Push to GitHub | ✅ Done |

---

## 🎯 Week 3 Key Concepts

### The API vs. The Playground

The playground is a UI wrapper around the same API calls. When you move to code, you gain: automation, repeatability, structured outputs, chaining, and integration with other systems. The playground is a whiteboard — the API is the factory floor.

### Messages Structure

Every API call uses a `messages` array. Each message has a `role` (user or assistant) and `content`. The conversation history lives in this array — the model has no memory between calls except what you explicitly pass.

```python
messages = [
    {"role": "user", "content": "What is prompt chaining?"},
    {"role": "assistant", "content": "Prompt chaining is..."},
    {"role": "user", "content": "Give me an example"}
]
```

### System Prompts in Code

System prompts are passed as a separate `system` parameter (Anthropic) or as a message with role "system" (OpenAI). They sit above the messages array and persist across the entire conversation.

### Structured Output

The most powerful technique this week: asking the model to return JSON. When you control the output format, you can parse it programmatically and use the data in downstream systems. This is the foundation of every AI pipeline.

```python
# Force JSON output via the prompt
response = client.messages.create(
    model="claude-opus-4-6",
    system="You are a data extractor. Always respond with valid JSON only. No explanation.",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=500
)
```

---

## 📂 Daily Notes

- `notes-day-01.md` — Anthropic API docs walkthrough + key concepts
- `notes-day-02.md` — First working API call, environment setup
- `notes-day-03.md` — System messages + conversation structure deep dive
- `notes-day-04.md` — Interactive script: system prompt + live user input
- `notes-day-05.md` — Max tokens, output length control, JSON format techniques
- `notes-day-06.md` — Structured JSON output script + field extraction
- `notes-day-07.md` — Clean up, comments, push to GitHub

**Artifacts:**
- `scripts/api-call-basic.py` — First working API call (documented)
- `scripts/structured-output.py` — JSON extraction script with system prompt

---

## 🔑 Week 3 Interview Talking Points

**On API vs. Playground:**
> "The API call structure made the playground make more sense retroactively. System prompts, conversation history, temperature — these aren't UI features, they're API parameters. Moving to code made me see them as what they actually are: function arguments with specific effects."

**On Structured Outputs:**
> "I built a script that sends a paragraph to the API and receives back a JSON object with extracted fields. The key was setting expectations in the system prompt — 'always respond with valid JSON only, no explanation.' Once the output format was controlled, I could parse it programmatically and chain it into other operations."

**On Conversation State:**
> "The API has no memory. Every call is stateless. Conversation history is just an array you manage yourself — you append messages and pass the whole thing on every call. Understanding this changed how I think about multi-turn AI products: the developer is responsible for deciding what context to keep and what to drop."

---

## 📚 Resources Used This Week

| Resource | What I Used It For |
|----------|--------------------|
| [Anthropic API Quickstart](https://docs.anthropic.com/en/api/getting-started) | Days 1-2 — setup and first call |
| [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) | Days 3-4 — system messages and structure |
| Python `anthropic` SDK docs | Days 2-6 — all code implementation |

---

## 💡 Week 3 Biggest Insights

> *"The API has no memory. Every call is stateless. The developer is responsible for managing conversation history."*

> *"Controlling output format via the prompt is more reliable than parsing free-form text. Ask for JSON, get JSON, parse it."*

---

*Next up → Week 4: Portfolio Project #1 🚀*
