# 🔁 Week 6 · Day 7 — Publish + Weekly Reflection

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Push everything to GitHub, review the week, and lock in what was learned.

---

## What Got Published Today

- `prompts/meeting-processor-prompt.md` — full prompt with version history and design decisions
- `scripts/meeting_processor.py` — the CLI tool
- `notes-day-01.md` through `notes-day-06.md` — daily build notes
- `notes.md` — weekly summary

All committed with descriptive commit messages. The commit history itself tells a story: brief → v1 → test results → v2 → system prompt → script → docs.

---

## Week 6 Reflection

### What I Built

A meeting notes processor that takes raw, unstructured input and returns a clean JSON object with summary, decisions, action items, and open questions. Tested on 30 inputs across 3 prompt versions. Final version passes 10/10.

### What I Actually Learned

**The hardest part isn't the happy path.** Getting the model to process clean, structured notes correctly took about 20 minutes. Getting it to handle ambiguous decisions consistently took three days. That's where the real work is.

**Edge cases are design decisions, not bugs.** When the model returned an ambiguous item as a decision, the correct response wasn't to "fix the prompt" — it was to make a product decision: *what should this tool do when a meeting ends without a clear conclusion?* I decided: classify conservatively, always default to open_question. That's a product choice, not a technical fix.

**Documentation is part of the build.** Writing the design decisions section of the docs forced me to articulate *why* each prompt choice was made. I couldn't have written that section without having made deliberate choices throughout the week.

### Confidence Scores This Week

| Skill | Start of Week | End of Week |
|-------|--------------|-------------|
| Multi-version prompt iteration | 6/10 | 9/10 |
| System prompt design | 6/10 | 8/10 |
| Failure analysis | 7/10 | 9/10 |
| Technical documentation | 5/10 | 8/10 |

### Biggest Quote of the Week

> *"The model wasn't wrong — the spec was incomplete."*

Every failure this week came from an underspecified requirement, not a model limitation. The model did exactly what I asked. What I asked wasn't precise enough.

---

*Next up → Week 7: Understanding Evaluation 🚀*
