# 📖 Week 3 · Day 1 — Anthropic API Quickstart

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Read the Anthropic API quickstart end to end. Don't build anything yet — understand the architecture before writing a line of code.

---

## What I Read Today

The [Anthropic API quickstart](https://docs.anthropic.com/en/api/getting-started) and the [Messages API reference](https://docs.anthropic.com/en/api/messages).

The goal was a conceptual map before writing any code. What are the moving parts? How does a call actually work?

---

## Core Concepts From the Docs

### The Messages Endpoint

Everything goes through `/v1/messages`. You send a request, you get a response. The request has:

- `model` — which Claude model to use
- `max_tokens` — upper limit on output length (required)
- `messages` — the conversation history as an array
- `system` (optional) — the system prompt

### The Messages Array

Each message in the array has a `role` (`user` or `assistant`) and `content` (the text). The simplest possible call has one message with role `user`.

```json
{
  "model": "claude-opus-4-6",
  "max_tokens": 1024,
  "messages": [
    {"role": "user", "content": "Hello, Claude"}
  ]
}
```

### The Response Structure

The response includes:
- `content` — array of content blocks (usually one text block)
- `usage` — input and output token counts
- `stop_reason` — why the model stopped (`end_turn`, `max_tokens`, etc.)
- `model` — which model was used

The `usage` field is immediately useful for cost tracking and debugging.

### System Prompts

Passed as a separate `system` string parameter, not inside the messages array. This is the Anthropic way. (OpenAI uses a message with role "system" — worth knowing both approaches.)

---

## What's Different From the Playground

The playground is a UI built on top of these exact API calls. The "System Prompt" box in the playground maps to the `system` parameter. The "Temperature" slider maps to the `temperature` parameter. Nothing in the playground is magic — it's all just an API call under the hood.

Understanding this made the playground feel transparent in a way it didn't before.

---

## Python SDK vs. Raw HTTP

The `anthropic` Python SDK wraps the raw HTTP calls. Instead of building JSON payloads manually, you call Python methods. Both work — the SDK is more readable and handles auth headers, retry logic, and error types for you.

```python
# SDK approach (what I'll use)
import anthropic
client = anthropic.Anthropic(api_key="your-key")
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
```

---

## Key Questions Going Into Day 2

1. How does the API handle errors? (rate limits, invalid requests)
2. What happens if I exceed `max_tokens`? Does the output truncate or error?
3. How do I read the token usage from the response?

Tomorrow's build day will answer these with real experiments.
