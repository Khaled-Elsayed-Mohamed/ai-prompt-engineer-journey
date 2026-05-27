# 📖 Week 3 · Day 5 — Max Tokens, Output Control & JSON Formatting

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Learn how to control output length and format. The techniques here are what make AI outputs usable in real systems — not just readable to humans, but parseable by code.

---

## Controlling Output Length

### max_tokens

`max_tokens` sets a hard ceiling. The model stops generating at that limit — even mid-sentence. Use it to:
- Prevent runaway outputs (and costs) for open-ended prompts
- Force brevity on tasks that should be short

**Rule of thumb:** Set `max_tokens` to roughly 2x what you expect the output to be. Never set it so low it cuts off valid outputs.

### Controlling Length via the Prompt

More precise than `max_tokens`. Tell the model explicitly:

```
Summarise this article in exactly 3 bullet points. Each bullet point should be one sentence.
```

```
Write a subject line for this email. Maximum 8 words.
```

```
Respond in under 50 words.
```

Prompt-level length instructions are more reliable than token limits alone because they communicate *intent*, not just a mechanical cutoff.

---

## Forcing JSON Output

This is the most important technique for building AI pipelines. When the model returns structured JSON, you can parse it with `json.loads()` and use it programmatically.

### The Pattern

**System prompt:**
```
You are a data extractor. Always respond with valid JSON only.
No explanation, no markdown, no prose. Just the JSON object.
```

**User prompt:**
```
Extract the following fields from this text:
- sender_name
- subject
- urgency (low / medium / high)
- action_required (true / false)

Text: [input]
```

**Expected output:**
```json
{
  "sender_name": "David Park",
  "subject": "Q3 budget approval",
  "urgency": "high",
  "action_required": true
}
```

### Parsing It in Code

```python
import json

raw_output = message.content[0].text
try:
    data = json.loads(raw_output)
    print(f"Urgency: {data['urgency']}")
    print(f"Action required: {data['action_required']}")
except json.JSONDecodeError as e:
    print(f"Model returned invalid JSON: {e}")
    print(f"Raw output: {raw_output}")
```

Always wrap `json.loads()` in a try/except. Even with a strong system prompt, the model occasionally adds a stray character or explanation.

---

## Reliability Techniques

**Prefill the assistant's response.** Anthropic's API allows you to pre-fill the start of the assistant's response:

```python
messages=[
    {"role": "user", "content": user_input},
    {"role": "assistant", "content": "{"}  # force JSON start
]
```

Starting with `{` makes it almost impossible for the model to output anything other than a JSON object.

**Ask for it twice.** For critical outputs: ask for the JSON, then have a second prompt validate it: "Is this valid JSON? Return only the corrected JSON if not."

---

## What This Enables

Once you can reliably get JSON from the API, you can:
- Route the output to a database
- Chain it into the next prompt as structured context
- Build conditional logic based on field values
- Integrate with any other system that reads JSON

Free-form text is for humans. JSON is for systems. The ability to produce either on demand is what makes a prompt engineer useful in a product team.

---

## Tomorrow

Day 6 builds a complete structured output script that extracts fields from text input and uses the JSON in a downstream step.
