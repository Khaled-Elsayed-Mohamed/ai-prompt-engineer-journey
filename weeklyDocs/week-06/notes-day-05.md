# 🔨 Week 6 · Day 5 — Python Script With File Input

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Wrap the meeting notes processor in a Python CLI tool that a non-technical person could actually use.

---

## Design Goals

Before writing a line of code, I listed what the script needed to do:

1. Accept input from a file: `python meeting_processor.py notes.txt`
2. Accept input from stdin (pipe): `cat notes.txt | python meeting_processor.py`
3. Print clean, readable JSON to stdout
4. Handle errors gracefully (missing file, API error, invalid response)
5. Work without any setup beyond `pip install anthropic`

---

## Key Implementation Decisions

### Reading input: file or stdin

```python
import sys

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        notes = f.read()
else:
    notes = sys.stdin.read()
```

Simple. If a filename is passed as an argument, read the file. Otherwise, read from stdin. This covers both usage patterns.

### Enforcing JSON output

Used the same assistant prefill trick from the classifier (Week 4):

```python
messages = [
    {"role": "user", "content": f"MEETING NOTES:\n{notes}"},
    {"role": "assistant", "content": "{"}
]
```

Prefilling with `{` forces the model to continue the JSON object. Combined with the system prompt rule "return only valid JSON," this makes parsing reliable.

### Pretty-printing output

```python
import json
result = json.loads("{" + response.content[0].text)
print(json.dumps(result, indent=2))
```

The `{` was consumed by the prefill, so we prepend it back before parsing. Then pretty-print with 2-space indent for readability.

### Error handling

Three failure modes covered:
1. **File not found** — clear message, exit 1
2. **API error** — print the error, exit 1  
3. **JSON parse failure** — print the raw response so the user can see what went wrong, exit 1

---

## Full Script

The complete `meeting_processor.py` is in `scripts/`. It's ~60 lines including comments and error handling.

---

## Test Run

```bash
python meeting_processor.py test-notes/sprint-planning.txt
```

Output:
```json
{
  "summary": "The team reviewed sprint capacity and agreed to carry over two incomplete tasks from the previous sprint. The focus for this sprint is the new onboarding flow, with design handoff set for Thursday.",
  "decisions": [
    "Carry over authentication bug fix and payment integration to this sprint",
    "New onboarding flow is the sprint priority"
  ],
  "action_items": [
    {
      "task": "Complete design mockups for onboarding flow",
      "owner": "Sara",
      "deadline": "Thursday"
    },
    {
      "task": "Set up staging environment for QA",
      "owner": "James",
      "deadline": null
    }
  ],
  "open_questions": [
    "Whether to include the email verification step in v1 or defer to v2"
  ]
}
```

Clean, correct, readable. Exactly what the brief specified.

---

## Lesson From Today

Writing the script forced me to think about the user experience of the tool, not just the prompt. A prompt that works in the playground is half-finished. The other half is making it usable.

---

## Tomorrow

Write the full project documentation.
