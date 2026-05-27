# 🔨 Week 3 · Day 4 — Interactive Script: System Prompt + User Input

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Build a script that accepts live user input from the terminal, applies a system prompt, and prints the model's response. First step from "script that does one thing" to "tool a person could use."

---

## What I Built

A simple interactive script that:
1. Takes a user's text from the terminal via `input()`
2. Wraps it in an API call with a specific system prompt
3. Prints the response
4. Loops until the user types "quit"

```python
import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a professional email rewriter.

When given a rough, informal email draft, rewrite it to be:
- Polished and professional in tone
- Clear and concise (no filler words)
- Well-structured with a clear opening, body, and closing

Return only the rewritten email. No explanation or commentary."""

def rewrite_email(draft: str) -> str:
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": draft}]
    )
    return message.content[0].text

def main():
    print("=== Email Rewriter ===")
    print("Paste your draft email, then press Enter twice. Type 'quit' to exit.\n")

    while True:
        lines = []
        while True:
            line = input()
            if line == "quit":
                print("Exiting.")
                return
            if line == "":
                break
            lines.append(line)

        if not lines:
            continue

        draft = "\n".join(lines)
        print("\n--- Rewritten ---")
        print(rewrite_email(draft))
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    main()
```

---

## What I Tested

**Input:**
```
hey can u send me that report thing we talked about last tuesday? 
also i need it by friday if thats ok cos i have a meeting.
thx
```

**Output:**
```
Hi [Name],

I hope you're doing well. Could you please send me the report we discussed last Tuesday?
I'd appreciate receiving it by Friday, as I have a meeting coming up.

Thank you,
Khaled
```

Tested with 5 different rough drafts — all produced clean, professional output.

---

## What I Learned

**The system prompt as a product definition.** Writing `SYSTEM_PROMPT` as a constant at the top of the file feels different from typing it into a UI. It's a *specification* — a permanent part of the tool's behavior. Every design decision I make in that string shapes everything the tool produces forever.

**Input validation matters.** The first version crashed when the user just pressed Enter without typing anything. Added a `if not lines: continue` guard. Small fix, but it made me think about edge cases in a way that playground testing doesn't force.

**The loop pattern.** The `while True` loop with a "quit" exit is the simplest interactive CLI pattern. For a real product you'd use a proper CLI framework (Click, argparse), but this works for prototyping and is easy to explain.

---

## Tomorrow

Day 5 covers max tokens, output control, and JSON formatting — the techniques that make API outputs machine-readable and chainable.
