# 📝 Week 6 · Day 6 — Full Project Documentation

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Write documentation good enough that someone else could understand, run, and build on this project — without asking me a single question.

---

## What Good Documentation Looks Like

I looked at how well-documented open source projects structure their READMEs before writing. The pattern that works:

1. **What it does** — one sentence
2. **Why it exists** — the problem it solves
3. **How to use it** — exact commands, example input, example output
4. **How it works** — the prompt design decisions, not just the code
5. **What it doesn't do** — known limitations
6. **How it was tested** — test results, not just "it works"

Most project documentation skips 4, 5, and 6. Those are exactly what an employer reviewing a portfolio wants to see.

---

## Writing the Prompt Design Section

This was the most valuable part to write. I documented three specific decisions:

**Decision 1: Conservative classification rule**
> "When in doubt whether something is a decision or an open question, the system prompt instructs the model to classify it as an open question. This is intentional: a falsely escalated open question causes a follow-up conversation. A falsely confirmed decision causes someone to act on something that wasn't agreed. The cost of a false negative is lower."

**Decision 2: `owner: null` over inferred owners**
> "Early versions sometimes inferred an owner from context ('Sara mentioned this, so Sara probably owns it'). This is hallucination — the model is inventing an assignment that doesn't exist in the notes. The system prompt explicitly prohibits this."

**Decision 3: Prefill trick for JSON reliability**
> "The assistant message is prefilled with `{` before the API call. This forces the model to continue a JSON object rather than deciding how to format its response. Combined with the system prompt rule, it eliminates markdown wrapping and explanation text in the output."

---

## Writing the Limitations Section

Documenting what the tool doesn't do is as important as documenting what it does:

- **No multi-meeting context** — each run is stateless. It doesn't know what was decided in the previous meeting.
- **No speaker attribution** — it extracts action items but doesn't track who said what throughout the meeting.
- **No audio/transcript support** — text input only.
- **Long document degradation** — input over ~3,000 words may produce lower-quality summaries as important content competes for attention in the context window.

---

## Test Results Documentation

Wrote a clean summary table of the 30-input test suite (original 10 inputs × 3 prompt versions):

| Prompt Version | Inputs | Passes | Partials | Fails | Pass Rate |
|---------------|--------|--------|----------|-------|-----------|
| v1 | 10 | 5 | 4 | 1 | 50% |
| v2 | 10 | 9 | 1 | 0 | 90% |
| v2 + system prompt | 10 | 10 | 0 | 0 | 100% |

Documenting the progression matters. It shows the iterative process — that v1 wasn't the plan, it was the starting point.

---

## Reflection on Documentation as a Skill

Writing the docs took as long as building the prompt. That ratio surprised me. But re-reading it, the documentation is genuinely what turns a script into a project. Without it, the code is just a file. With it, it's a demonstration of how I think.

---

## Tomorrow

Publish to GitHub, write a short LinkedIn post.
