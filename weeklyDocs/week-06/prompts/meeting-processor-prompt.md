# Meeting Notes Processor — Prompt Documentation

## Final Prompt (v2)

```
You are a meeting notes processor. Your job is to turn raw, unstructured meeting notes into a structured JSON summary.

Extract the following:

1. summary: A 3–5 sentence overview of what was discussed and what outcomes were reached. Be neutral and factual — don't editorialize.

2. decisions: Only include things that were explicitly DECIDED, not just discussed or suggested. A decision is a commitment the group made. Concerns raised, opinions shared, or topics "to look into" are NOT decisions.

3. action_items: Tasks someone agreed to do. Include:
   - task: what needs to be done
   - owner: the person responsible. Use null if unclear or not stated — do NOT guess.
   - deadline: any mentioned timeframe. Use null if none mentioned.

4. open_questions: Things that were raised but not resolved. Include concerns, unresolved debates, and items that need follow-up but have no owner or decision yet.

Return ONLY valid JSON in this exact structure:
{
  "summary": "string",
  "decisions": ["string"],
  "action_items": [
    {"task": "string", "owner": "string or null", "deadline": "string or null"}
  ],
  "open_questions": ["string"]
}

If a category has no items, return an empty array [].

Meeting notes:
[NOTES]
```

---

## Version History

### v1 — Initial Prompt

**Issue:** The model was adding items to `decisions` that were clearly just discussion topics ("we talked about redesigning the onboarding flow" → listed as a decision).

**Root cause:** The original `decisions` definition was too broad: "decisions made." The model interpreted "we agreed the UX needs improving" as a decision when it was actually a shared opinion.

**Fix:** Added explicit disambiguation: "Only include things that were explicitly DECIDED, not just discussed or suggested. A decision is a commitment the group made."

### v2 — Added owner: null instruction

**Issue:** For tasks where the owner wasn't mentioned, the model was guessing ("probably Sarah" or assigning to whoever was mentioned last).

**Fix:** Added explicit instruction: "Use null if unclear or not stated — do NOT guess."

**Result:** Ambiguous ownership now correctly returns null, not a wrong attribution.

---

## Test Results (30 inputs total)

### Decision Accuracy (hardest category)
- Explicitly stated decisions: 15/15 ✅
- "Discussed but not decided" items: correctly excluded in 11/12 cases
- Implied decisions ("we're definitely not doing X this quarter"): 9/10 ✅

### Action Item Attribution
- Named owner: 18/18 correct ✅
- Unnamed or ambiguous: 9/10 returned null correctly (1 case guessed incorrectly in v1, fixed in v2) ✅

### Open Questions
- Unresolved concerns correctly surfaced: 12/13 ✅
- No false positives (decided items in open_questions): 0/13 ✅

---

## Design Notes

**Why separate decisions from action_items?**
A decision is a commitment the group made together. An action item is a task one person is responsible for. These are meaningfully different — a company's legal team doesn't want "migrate to AWS" sitting in the same list as "Sarah to send the proposal." Separating them makes the output immediately usable.

**Why owner: null instead of "Unknown"?**
Downstream systems (JIRA, Notion, Slack) can query `null` programmatically. "Unknown" is a string that would require special handling. Null is the right data model for "no value."
