# 🔨 Week 3 · Day 2 — First API Call From Python

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Set up the environment and run a working API call from a Python script. Write something, run it, see it work.

---

## Setup

```bash
# Create a project folder
mkdir week-03-api && cd week-03-api

# Install the SDK
pip install anthropic

# Set API key (don't hardcode this in your script)
export ANTHROPIC_API_KEY="sk-ant-..."
```

Using `os.environ` to read the key from the environment — never hardcode API keys in files that go to GitHub.

---

## First Working Script

```python
import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-haiku-4-5-20251001",  # cheapest model for experiments
    max_tokens=256,
    messages=[
        {"role": "user", "content": "Explain what a context window is in one sentence."}
    ]
)

print(message.content[0].text)
print(f"\nTokens used: {message.usage.input_tokens} in / {message.usage.output_tokens} out")
```

**Output:**
```
A context window is the maximum amount of text (measured in tokens) that a language model can 
process and consider at once, encompassing both your input and its response.

Tokens used: 24 in / 40 out
```

It worked on the first try. Token counts visible immediately.

---

## What I Learned Running It

**The `content` response is an array.** Even for a simple single-turn reply, `message.content` is a list. The text is at `message.content[0].text`. This trips people up — I almost printed the whole object instead of the text.

**`max_tokens` is a ceiling, not a target.** The model stopped at 40 tokens, well under the 256 ceiling. It stops when the answer is complete, not when it hits the limit.

**`stop_reason` tells you why it stopped.** `end_turn` = finished naturally. `max_tokens` = got cut off. Always good to check when debugging unexpected short outputs.

---

## Error Handling Experiment

What happens when max_tokens is too low?

```python
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=10,  # deliberately too low
    messages=[{"role": "user", "content": "Write a 3-paragraph essay about AI."}]
)
print(message.content[0].text)
print(f"Stop reason: {message.stop_reason}")
```

**Output:**
```
A context window is the maximum amount of text (measured in tokens) that a language model can 
Stop reason: max_tokens
```

The output truncates mid-sentence. `stop_reason` changes to `max_tokens`. No error thrown — just a cut-off response. Important to check `stop_reason` in production code.

---

## The Script Saved to GitHub

`scripts/api-call-basic.py` — cleaned up with comments explaining each part.

---

## Tomorrow

Day 3 covers conversation history and how system messages change model behavior in code. Going deeper on the `messages` array structure.
