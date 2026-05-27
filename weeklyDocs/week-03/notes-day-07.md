# 🔁 Week 3 · Day 7 — Clean Up, Comment, Push

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Polish both scripts from this week into portfolio-ready code. Add comments that explain *why*, not just *what*. Push to GitHub.

---

## The Code Review I Did On Myself

Before pushing, I re-read both scripts as if I were a hiring manager seeing them cold. Questions I asked:

1. Would someone unfamiliar with the project understand what this does from the first 10 lines?
2. Are the system prompts readable and explained?
3. Is error handling present?
4. Are there any hardcoded values that should be constants or config?
5. Are the function names clear about what they return?

---

## Changes Made

**`api-call-basic.py`:**
- Added a module docstring explaining what the script demonstrates
- Added inline comments explaining each API parameter
- Added a note about why `claude-haiku-4-5-20251001` is used for experiments (cheapest model)
- Extracted the model name to a constant at the top

**`structured-output.py`:**
- Added a module docstring with a clear description and example use case
- Commented the prefill technique with a "why" explanation
- Added the try/except around `json.loads` with a clear error message
- Added a `__main__` block with a working example in the module docstring
- Renamed `email_data` parameters to be more descriptive

---

## The Scripts Are Now Portfolio-Ready

Good code documentation isn't about volume — it's about removing confusion. Every comment in the final versions answers a question someone reading the code cold might ask.

The test for good inline comments: if you removed all the code and just read the comments, would you understand what the function does and why?

---

## What I Pushed to GitHub

```
Week 3: API fundamentals, structured outputs, 2 working scripts
```

Files added:
- `weeklyDocs/week-03/notes.md` — week summary
- `weeklyDocs/week-03/notes-day-01.md` through `notes-day-07.md`
- `weeklyDocs/week-03/scripts/api-call-basic.py`
- `weeklyDocs/week-03/scripts/structured-output.py`

---

## Week 3 Honest Assessment

This was the most practically useful week so far. Weeks 1 and 2 built conceptual understanding. Week 3 produced actual tools — scripts I could hand to someone.

The JSON pipeline (extract → structured data → generate) is a pattern I'll use in every project going forward. It's reliable, debuggable, and composable.

**Confidence at end of week:**
- Making API calls in Python: 9/10
- Managing conversation history: 8/10
- Producing reliable JSON outputs: 8/10
- Writing clean, commented API scripts: 8/10

**Week 3 done. Ready for the first real project. 🚀**
