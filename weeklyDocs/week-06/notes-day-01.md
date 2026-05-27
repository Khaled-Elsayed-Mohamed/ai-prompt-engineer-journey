# 🔨 Week 6 · Day 1 — Project Brief + Core Prompt First Draft

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Define the project clearly before touching any prompts. Write the brief, then build the first version of the core prompt.

---

## The Brief

Before writing a single prompt, I wrote a one-paragraph project brief:

> "Build a tool that takes raw, unstructured meeting notes as input and returns a structured JSON object containing: a plain-English summary (3–5 sentences), a list of decisions made, a list of action items with owner and deadline, and a list of open questions. The tool should work on messy, real-world notes — not clean formatted input."

Writing this first forced two important decisions:
1. **Output schema** — I had to commit to the fields before building. Summary, decisions, action_items, open_questions.
2. **The hardest case** — "messy, real-world notes" is a requirement, not an afterthought. I needed to test that from the start.

---

## Output Schema (Locked In Before Prompting)

```json
{
  "summary": "string",
  "decisions": ["string"],
  "action_items": [
    {
      "task": "string",
      "owner": "string or null",
      "deadline": "string or null"
    }
  ],
  "open_questions": ["string"]
}
```

The `owner: null` case is important — many action items in real meetings don't have a named owner yet. The prompt needs to handle this without hallucinating a name.

---

## Core Prompt v1

```
You are an assistant that processes meeting notes.

Given the raw meeting notes below, extract and return a JSON object with this exact structure:

{
  "summary": "A 3-5 sentence plain-English summary of the meeting",
  "decisions": ["List of decisions made — only include things that were clearly decided"],
  "action_items": [
    {
      "task": "What needs to be done",
      "owner": "Person responsible, or null if not specified",
      "deadline": "Deadline if mentioned, or null"
    }
  ],
  "open_questions": ["Things that were raised but not resolved"]
}

Return only valid JSON. No explanation text outside the JSON.

MEETING NOTES:
{{notes}}
```

---

## First Test

Input: a clean set of notes from a product roadmap meeting (hand-written, ~200 words).

Result: clean JSON, all fields populated correctly. Summary was accurate. Action items had owners where mentioned, null where not.

**Score on first test: 8/10.** Two issues found:
1. One item classified as a `decision` that was actually still being debated — it should have been `open_questions`.
2. The summary included implementation details that weren't important context.

---

## Tomorrow

Test with 10 different inputs — including messy ones. Document every failure.
