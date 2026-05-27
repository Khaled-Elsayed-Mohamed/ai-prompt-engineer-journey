# 🔨 Week 6 · Day 3 — Fix Failures, Prompt v2

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Address every failure from Day 2 with targeted prompt changes. Retest all 10 inputs.

---

## The Changes in v2

### Fix 1 — Decisions vs open questions disambiguation

Added explicit rules to the prompt:

```
CLASSIFICATION RULES:
- decisions: Only include items where a clear conclusion was reached and agreed upon.
  If the notes say "leaning toward", "thinking about", "need to check", or "not sure yet" — it is NOT a decision. Put it in open_questions.
- open_questions: Anything unresolved, deferred, or still being debated — even if heavily discussed.
```

### Fix 2 — Summary synthesis instruction

Changed the summary instruction from:
> "A 3-5 sentence plain-English summary of the meeting"

To:
> "A 3-5 sentence synthesised summary of the meeting's purpose and outcomes. Write in complete sentences. Do not list topics — explain what happened and what was resolved. Ignore conversational filler."

### Fix 3 — Fragmented input handling

Added:
> "If the input notes are fragmented or shorthand, still produce a coherent, well-written output. Interpret fragments charitably based on context."

---

## v2 Prompt (Full)

```
You are an assistant that processes meeting notes into structured summaries.

Given the raw meeting notes below, return a JSON object with this exact structure:

{
  "summary": "A 3-5 sentence synthesised summary of the meeting's purpose and outcomes. Write in complete sentences. Do not list topics — explain what happened and what was resolved. Ignore conversational filler.",
  "decisions": ["Decisions made — only include items where a clear conclusion was reached. If notes say 'leaning toward', 'need to check', or 'not sure' — do NOT include here."],
  "action_items": [
    {
      "task": "What needs to be done",
      "owner": "Person responsible, or null if not specified",
      "deadline": "Deadline if mentioned, or null"
    }
  ],
  "open_questions": ["Anything unresolved, deferred, or still being debated — even if heavily discussed"]
}

CLASSIFICATION RULES:
- A decision requires clear agreement. Vigorous discussion without conclusion = open question.
- An action item requires a task. Vague intentions are not action items.
- If the input is fragmented, interpret context charitably and produce coherent output.

Return only valid JSON. No explanation text outside the JSON.

MEETING NOTES:
{{notes}}
```

---

## Retest Results

| # | v1 Result | v2 Result | Change |
|---|-----------|-----------|--------|
| 1 | Pass | Pass | — |
| 2 | Pass | Pass | — |
| 3 | Partial | Pass | ✅ Fixed |
| 4 | Partial | Pass | ✅ Fixed |
| 5 | Pass | Pass | — |
| 6 | Partial | Pass | ✅ Fixed |
| 7 | Pass | Pass | — |
| 8 | Fail | Pass | ✅ Fixed |
| 9 | Pass | Pass | — |
| 10 | Partial | Partial | ⚠️ Improved but not perfect |

**v2 Score: 9/10 passes, 1 partial.**

Input 10 (mixed language intent) still produces one ambiguous decision that could go either way — it's genuinely ambiguous in the source text. This is acceptable behaviour: the prompt is now consistent, and the one remaining edge case requires human judgment.

---

## Key Insight

> The biggest prompt engineering lesson from today: **the model wasn't wrong — the spec was incomplete.** "Only include clearly decided items" sounds clear when you write it, but the model has no definition of "clearly." The fix wasn't a clever trick — it was writing better requirements.

---

## Tomorrow

Add the system prompt for tone and format control.
