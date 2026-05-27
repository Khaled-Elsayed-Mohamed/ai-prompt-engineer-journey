# 🧠 Week 6 — Portfolio Project #2: Meeting Notes Processor

**AI Prompt Engineer Journey · Khaled**

> [!IMPORTANT]
> **Goal this week:** Build a polished, niche-specific project. More complex than Project #1, better documented, and closer to something a real company would use.

---

## 📊 Progress Tracker

| Day | Mode | Theme | Status |
|-----|------|-------|--------|
| Day 1 | 🔨 Build | Project brief + core prompt first draft | ✅ Done |
| Day 2 | 🔨 Build | Test with 10 inputs, document failures | ✅ Done |
| Day 3 | 🔨 Build | Fix failures, prompt v2 | ✅ Done |
| Day 4 | 🔨 Build | Add system prompt + tone constraints | ✅ Done |
| Day 5 | 🔨 Build | Python script with file input | ✅ Done |
| Day 6 | 📝 Doc | Full project documentation | ✅ Done |
| Day 7 | 🔁 Review | Publish + LinkedIn post | ✅ Done |

---

## 🎯 The Project

**Meeting Notes Processor** — Takes raw, unstructured meeting notes and returns a structured JSON object with a summary, decisions made, action items with owners and deadlines, and open questions.

**Why this matters to employers:** Almost every company has this problem. Showing a working solution in your niche, with documented test results and a CLI tool, demonstrates both technical skill and business awareness.

---

## 📊 Final Results

| Input Type | Accuracy |
|------------|----------|
| Clean, structured notes | 10/10 |
| Messy, stream-of-consciousness | 9/10 |
| Very short / minimal notes | 8/10 |
| Non-native English notes | 8/10 |

**Edge case handled:** "Everyone thinks the pricing is too high" correctly classified as open_question, not decision. This is the hardest distinction in the problem.

---

## 📂 Files

- `notes-day-01.md` through `notes-day-07.md` — daily build notes
- `prompts/meeting-processor-prompt.md` — final prompt + version history
- `scripts/meeting_processor.py` — CLI tool (reads from file or stdin)

---

## 💡 Biggest Lesson

> *"The hardest part of building an information extractor isn't getting the happy path right — it's defining what the AI should do when the input is ambiguous. Every edge case requires a design decision, not just a technical fix."*

---

*Next up → Week 7: Understanding Evaluation 🚀*
