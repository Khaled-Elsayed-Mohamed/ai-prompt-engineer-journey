# 🧠 Week 4 — Portfolio Project #1: Customer Message Classifier

**AI Prompt Engineer Journey · Khaled**

> [!IMPORTANT]
> **Goal this week:** Build something complete enough to show an employer. Documented, tested, and live on GitHub. Quality over speed.

---

## 📊 Progress Tracker

| Day | Mode | Theme | Status |
|-----|------|-------|--------|
| Day 1 | 🔨 Build | Write core prompt, test with 10 inputs | ✅ Done |
| Day 2 | 🔨 Build | Improve based on failures, document changes | ✅ Done |
| Day 3 | 🔨 Build | Wrap in Python script with CLI | ✅ Done |
| Day 4 | 📖 Learn | Study how others document AI projects | ✅ Done |
| Day 5 | 📝 Doc | Write project README and methodology | ✅ Done |
| Day 6 | 🔨 Build | Final polish, publish to GitHub | ✅ Done |
| Day 7 | 🔁 Review | Month 1 review — what do I know, what's missing? | ✅ Done |

---

## 🎯 The Project

**Customer Message Classifier** — A prompt-based system that reads incoming customer messages and routes them to the correct department with a confidence level and reasoning.

**Why this project?** Classification is one of the most common real-world use cases for LLMs in business. Every company with a customer-facing inbox needs to route messages. It's also a perfect demonstration of: system prompt design, JSON structured output, and iterative prompt improvement.

**Categories:**
- `billing` — payment issues, invoices, refunds
- `technical_support` — bugs, errors, product not working
- `account` — login, password, access, account changes
- `sales` — pricing, upgrades, new features inquiry
- `complaint` — dissatisfaction, bad experience, escalation request
- `other` — anything that doesn't fit the above

---

## 📂 Daily Notes

- `notes-day-01.md` — First prompt version, 10 test inputs, initial results
- `notes-day-02.md` — Failure analysis, prompt v2, re-test
- `notes-day-03.md` — Python script with CLI interface
- `notes-day-04.md` — Research: how to document AI projects well
- `notes-day-05.md` — Project README and methodology write-up
- `notes-day-06.md` — Final push, GitHub publish, LinkedIn post
- `notes-day-07.md` — Month 1 reflection

**Project artifact:**
- `prompts/classifier-prompt.md` — Final prompt with version history
- `scripts/classifier.py` — Working Python script

---

## 🔑 Project Results

**v1 accuracy:** 8/10 inputs correctly classified  
**v2 accuracy:** 10/10 inputs correctly classified  
**Edge cases caught:** billing/complaint ambiguity, polite complaints, non-English words

---

## 💡 Biggest Lesson

> *The first prompt is a hypothesis. Testing is the only way to find out what's wrong. Documentation of what broke and what changed is what turns a working prompt into a portfolio piece.*

---

*Next up → Week 5: Pick Your Niche 🚀*
