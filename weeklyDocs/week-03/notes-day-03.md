# 📖 Week 3 · Day 3 — System Messages & Conversation Structure

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Understand how system prompts and conversation history work in the API. These are the structural foundations of every real AI product.

---

## System Messages in Code

In the Anthropic SDK, the system prompt is a separate `system` parameter:

```python
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=512,
    system="You are a concise technical writer. Respond in bullet points only. No prose.",
    messages=[
        {"role": "user", "content": "Explain the three main types of machine learning."}
    ]
)
```

The system parameter sits *outside* the messages array. It applies to the entire conversation.

---

## Conversation History — How It Actually Works

The API is stateless. Every call starts fresh. "Memory" is an illusion you build by passing previous messages back.

### Single turn (no memory):
```python
messages = [
    {"role": "user", "content": "What is prompt engineering?"}
]
```

### Multi-turn (manual memory):
```python
messages = [
    {"role": "user", "content": "What is prompt engineering?"},
    {"role": "assistant", "content": "Prompt engineering is the practice of..."},
    {"role": "user", "content": "Can you give me a real-world example?"}
]
```

You maintain the history. You decide what to include. The model sees only what you pass.

---

## Experiment: Context Matters

**Without history:**
```python
messages = [
    {"role": "user", "content": "Can you give me a real-world example?"}
]
# Output: "Could you clarify what you're looking for an example of?"
```

**With history:**
```python
messages = [
    {"role": "user", "content": "What is prompt engineering?"},
    {"role": "assistant", "content": "Prompt engineering is..."},
    {"role": "user", "content": "Can you give me a real-world example?"}
]
# Output: "A real-world example of prompt engineering is a customer support bot..."
```

The second call costs more tokens (you're sending the whole history) but produces a relevant answer. This is the core tradeoff in multi-turn systems: context improves quality, but every token of context costs money.

---

## Key Insight: The Developer Manages Context

In a chatbot product, every time a user sends a message, the backend:
1. Appends the user message to the conversation history
2. Sends the full history to the API
3. Gets a response
4. Appends the assistant's response to the history
5. Stores the updated history for the next turn

At some point, the history approaches the context window limit. The developer has to decide: truncate old messages, summarize them, or use a different strategy. This is a real engineering decision in production systems.

---

## Practical Pattern: System Prompt + Single User Turn

For most non-chatbot use cases (classifiers, extractors, rewriters), you don't need conversation history. Just a system prompt and one user message. This is the simplest, cheapest, most reliable pattern:

```python
def run_prompt(system_prompt: str, user_input: str) -> str:
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": user_input}]
    )
    return message.content[0].text
```

This function becomes the foundation for almost everything in Week 4's project.

---

## Tomorrow

Day 4 builds an interactive script that takes real user input from the terminal, applies a system prompt, and prints the response. First step toward a real tool.
