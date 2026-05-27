# 🔨 Week 5 · Day 6 — First Test of Meeting Notes Processor

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Write a rough first draft of the meeting notes processing prompt. Test it with 3 genuine examples of messy notes. Not polishing — just seeing if the idea works.

---

## First Draft Prompt

```
You are a meeting notes processor.

Given raw meeting notes, extract and structure the following:

1. summary: A 3-5 sentence summary of what was discussed and decided
2. decisions: A list of decisions that were made (not discussed — actually decided)
3. action_items: A list of tasks with owner (person responsible) and deadline if mentioned
4. open_questions: Things that were raised but not resolved

Return as JSON:
{
  "summary": "string",
  "decisions": ["string"],
  "action_items": [
    {"task": "string", "owner": "string or null", "deadline": "string or null"}
  ],
  "open_questions": ["string"]
}

If there are no items in a category, return an empty array.

Meeting notes:
[NOTES]
```

---

## Test 1 — Clean Notes

**Input:**
```
Standup 14 May
Attendees: Sarah, Marcus, Priya, Tom

- Q3 dashboard feature is almost done, Sarah says it should ship by end of week
- Marcus flagged that the payment API is returning errors in production - he's going to fix it today
- Priya asked if we're still doing the user research session next Tuesday, Tom said yes confirmed 2pm
- Decided to move sprint planning to Thursday instead of Friday
- Nobody has updated the docs since February, team agreed Tom owns this going forward
```

**Output:**
```json
{
  "summary": "The team discussed Q3 dashboard progress, a production payment API issue, and upcoming meetings. Sprint planning was moved and documentation ownership was assigned.",
  "decisions": [
    "Sprint planning moved from Friday to Thursday",
    "Tom owns documentation updates going forward"
  ],
  "action_items": [
    {"task": "Fix payment API production errors", "owner": "Marcus", "deadline": "today"},
    {"task": "Ship Q3 dashboard feature", "owner": "Sarah", "deadline": "end of week"},
    {"task": "Update team documentation", "owner": "Tom", "deadline": null}
  ],
  "open_questions": []
}
```

**Assessment:** ✅ Excellent. Every decision and action item correctly extracted with accurate attribution.

---

## Test 2 — Messy, Stream of Consciousness Notes

**Input:**
```
product sync - wednesday

ok so we talked about the onboarding thing again. jen said its still broken for enterprise users which is bad. need to fix asap. also the new design mockups came in, they look good but david said we need legal to sign off before we can use the new brand colors. nobody knows when legal will get back to us. oh and we decided definitely NOT doing the mobile app rewrite this quarter, too much scope. budget for Q4 was mentioned - finance needs our numbers by the 30th. who's doing that? probably marcus but not confirmed. next sync same time next week
```

**Output:**
```json
{
  "summary": "The team discussed ongoing onboarding issues for enterprise users, new design mockup approval requirements, scope decisions for Q4, and a finance deadline.",
  "decisions": [
    "Mobile app rewrite is NOT happening this quarter — too much scope",
    "New brand colors require legal sign-off before use"
  ],
  "action_items": [
    {"task": "Fix onboarding flow for enterprise users", "owner": null, "deadline": "ASAP"},
    {"task": "Submit Q4 budget numbers to finance", "owner": "Marcus (unconfirmed)", "deadline": "the 30th"},
    {"task": "Get legal sign-off on new brand colors", "owner": "David", "deadline": null}
  ],
  "open_questions": [
    "When will legal respond about the brand colors?",
    "Who is officially responsible for Q4 budget submission?"
  ]
}
```

**Assessment:** ✅ Strong. Correctly flagged Marcus as "unconfirmed" — that's genuinely smart. Open questions section correctly surfaced the two unresolved items.

---

## Test 3 — Almost No Structure

**Input:**
```
ali to send the proposal by friday. launch pushed to june. no decision on vendor yet. everyone thinks the current pricing is too high but nothing decided
```

**Output:**
```json
{
  "summary": "Brief notes covering a proposal deadline, launch date change, pending vendor decision, and pricing concerns.",
  "decisions": [
    "Launch date pushed to June"
  ],
  "action_items": [
    {"task": "Send proposal", "owner": "Ali", "deadline": "Friday"}
  ],
  "open_questions": [
    "Which vendor to use?",
    "Is the current pricing too high? What should it be?"
  ]
}
```

**Assessment:** ✅ Correct distinction between "everyone thinks pricing is too high" (concern raised, nothing decided) vs. "launch pushed to June" (decision made). This is a subtle but important distinction.

---

## Conclusion: Viable

The first draft prompt produced strong results across all three test types. Week 6 will refine this into a polished project with full documentation, edge case testing, and a working Python script.
