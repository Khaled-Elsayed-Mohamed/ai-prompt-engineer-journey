# 🔨 Week 3 · Day 6 — Structured JSON Output Script

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Build a complete script that accepts text input and returns structured JSON. This is the Week 3 portfolio artifact — the first script that demonstrates real engineering thinking, not just API usage.

---

## What I Built

An email triage script: paste an email, get back a JSON object with extracted fields, then use those fields to generate a draft response. Two-step chain. Both steps use structured outputs.

**Script:** `scripts/structured-output.py`

---

## Step 1 — Extract

```python
EXTRACT_SYSTEM = """You are an email analyst. Extract structured data from emails.

Respond with valid JSON only. No explanation, no markdown.

Always return this exact structure:
{
  "sender_name": "string or null",
  "subject_inferred": "string — what the email is about",
  "sentiment": "positive | neutral | frustrated | urgent",
  "action_required": true or false,
  "action_description": "string — what action is needed, or null if none",
  "priority": "low | medium | high"
}"""

def extract_email_data(email_text: str) -> dict:
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        system=EXTRACT_SYSTEM,
        messages=[
            {"role": "user", "content": email_text},
            {"role": "assistant", "content": "{"}  # prefill for reliability
        ]
    )
    # The assistant prefill means the response starts after the "{"
    raw = "{" + message.content[0].text
    return json.loads(raw)
```

---

## Step 2 — Generate Response

```python
REPLY_SYSTEM = """You are a professional email responder.

Given structured information about an email, write a concise, professional reply.
- Match the tone to the situation (urgent → decisive, frustrated → empathetic)
- State the next action clearly if one is required
- Keep replies under 120 words
- No subject line needed — just the reply body"""

def generate_reply(email_data: dict) -> str:
    context = f"""
Sender: {email_data['sender_name'] or 'Unknown'}
About: {email_data['subject_inferred']}
Their tone: {email_data['sentiment']}
Action needed: {email_data['action_description'] or 'None'}
Priority: {email_data['priority']}
"""
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=256,
        system=REPLY_SYSTEM,
        messages=[{"role": "user", "content": context}]
    )
    return message.content[0].text
```

---

## Test Results

**Input email:**
```
Hi, I placed an order 3 weeks ago and it still hasn't arrived. 
Order number ORD-7741. I've already emailed twice with no response. 
This is really unacceptable — I need this resolved TODAY.
```

**Step 1 output:**
```json
{
  "sender_name": null,
  "subject_inferred": "Missing order that hasn't arrived after 3 weeks",
  "sentiment": "frustrated",
  "action_required": true,
  "action_description": "Locate and resolve status of order ORD-7741 urgently",
  "priority": "high"
}
```

**Step 2 output:**
```
I'm truly sorry for the delay and for the lack of response to your previous emails — 
that's not the experience we want you to have.

I'm looking into order ORD-7741 right now and will have an update for you within 
the next 2 hours. If a replacement is needed, we'll expedite it at no additional cost.

Thank you for your patience.
```

---

## What Made This Work

**The prefill trick** (`{"role": "assistant", "content": "{"}`) was the difference between 95% and 99% JSON reliability. Worth always using when JSON output is required.

**Passing structured data between steps** instead of raw text. Step 2 receives clean, labelled fields — not the original email. The model doesn't need to re-read the email; it just uses the extracted facts. This is the core principle behind multi-step AI pipelines.

---

## Tomorrow

Day 7: clean up both scripts, add thorough inline comments, push everything to GitHub. This is the first public code artifact of the journey.
