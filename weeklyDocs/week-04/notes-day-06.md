# 🔨 Week 4 · Day 6 — Final Polish & GitHub Publish

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Final review of everything from this week. Push the project. Write the LinkedIn post.

---

## Pre-Publish Checklist

Before pushing, I went through the project with this checklist:

**Code:**
- [x] Script runs without errors from a fresh terminal
- [x] API key is loaded from environment, not hardcoded
- [x] Error handling covers missing API key + network errors + invalid JSON response
- [x] Help text is clear (`python classifier.py --help`)
- [x] No debug print statements left in

**Prompt:**
- [x] Final v2 prompt is saved in `prompts/classifier-prompt.md`
- [x] Version history (v1 → v2) is documented with what changed and why
- [x] All 15 test cases are in a table in the README

**README:**
- [x] Problem statement is clear in the first paragraph
- [x] Instructions are copy-paste-ready
- [x] Limitations section is honest
- [x] No typos (ran through a spell check)

---

## What I Pushed

```
Week 4: Portfolio Project #1 — Customer Message Classifier
- prompts/classifier-prompt.md (v2 prompt + version history)
- scripts/classifier.py (working CLI tool)
- prompts/classifier-README.md (full project documentation)
```

---

## LinkedIn Post Draft

> **Built my first AI engineering project this week — a customer message classifier.**
>
> The interesting part wasn't the final result. It was the failure.
>
> My first prompt got 8/10 test cases right. Two failures:
> - "I want to cancel my subscription" → routed to Billing instead of Account
> - "Can you help me transfer my data?" → routed to Other instead of Account
>
> Both were category definition problems, not model problems. The fix was adding clearer disambiguation language and expanding the Account category description.
>
> v2: 10/10. Plus 5 edge cases including a French-language message (handled correctly with no extra engineering).
>
> The most useful thing I built was the test set — not the prompt. You can't improve what you don't measure.
>
> Full project on GitHub: [link]

Short. Specific. Shows thinking, not just output.

---

## What Month 1 Produced

Four weeks ago I was writing prompts in a chat window with no structure. Now I have:
- Deep understanding of how LLMs process prompts at the token level
- 5 core techniques I can explain and apply: CoT, system prompts, chaining, JSON output, classification
- Working API code in Python
- A tested, documented, public project

That's Month 1 done. Month 2 is about building real things — more ambitious, more polished, in a chosen niche.
