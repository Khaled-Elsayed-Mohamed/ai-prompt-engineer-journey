# 🔨 Week 4 · Day 3 — Python Script with CLI

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Wrap the classifier prompt in a clean Python script. Make it useful as a standalone tool — not just a prompt that lives in a text file.

---

## Design Decisions Before Writing Code

**Input method:** Accept a message via command-line argument or stdin. Command-line is simpler to demo; stdin is more useful for piping. I'll support both.

**Output format:** Print the full JSON response by default, with an option to print just the category for scripting.

**Model:** `claude-haiku-4-5-20251001` — fastest and cheapest for classification tasks. Classification doesn't need the reasoning depth of Sonnet or Opus.

**Error handling:** Network errors, missing API key, invalid JSON response — all should give a clear message, not a Python traceback.

---

## The Script

`scripts/classifier.py` — see the actual file for the full commented version.

Key design choices in the code:

```python
# Two input modes
if args.message:
    message_text = args.message
else:
    # Read from stdin — useful for: echo "help me" | python classifier.py
    message_text = sys.stdin.read().strip()

# Clean output options
if args.category_only:
    print(result["category"])
else:
    print(json.dumps(result, indent=2))
```

---

## CLI Examples

**Classify a single message:**
```bash
python classifier.py "I can't log in to my account"
```
Output:
```json
{
  "category": "account",
  "confidence": "high",
  "reason": "The customer is reporting a login issue, which is an access problem."
}
```

**Get just the category (useful for scripting):**
```bash
python classifier.py --category-only "You charged me twice"
```
Output:
```
billing
```

**Process a file full of messages:**
```bash
while IFS= read -r line; do
    echo "$line" | python classifier.py --category-only
done < messages.txt
```

---

## What This Demonstrates to an Employer

1. **Prompt engineering:** v2 prompt handles ambiguous cases, multilingual input, and confidence levels
2. **API integration:** Working Python code, not a playground screenshot
3. **Product thinking:** The script is designed to be *used* — it has input modes, output options, and error handling
4. **Iteration:** The notes document v1 → v2 improvement with specific failures and fixes

---

## Tomorrow

Day 4 is research: how do experienced AI engineers document their projects? Collecting examples before writing the README.
