# 📝 Week 2 · Day 6 — Documentation & Portfolio Write-Up

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Turn this week's work into portfolio-ready documentation. The system prompt project is your first real artifact — it should be clear enough for a hiring manager to read and understand immediately.

---

## What I Documented Today

Three artifacts from this week, cleaned up and pushed to the repo:

1. The Notion support system prompt (final version + evolution log)
2. The 3-step prompt chain from Day 5
3. This week's key findings in the notes.md summary

---

## How to Write Good AI Project Documentation

After reading several examples on GitHub and Medium, the pattern that works is:

**Lead with the problem.** Don't start with your solution — start with what problem you were solving and why it's hard. A hiring manager who reads the first paragraph should understand the value before they see a single line of your prompt.

**Show your reasoning.** The prompt itself is less interesting than why you wrote it that way. What constraint did you notice? What failed in the first version? What changed?

**Include failure.** The most credible portfolios show iteration: v1 → failure → learning → v2. Anyone can show a prompt that works. Showing the prompt that didn't work first, and explaining what you learned, demonstrates engineering instinct.

**Keep it short.** Two pages max. Hiring managers skim. The goal is to make the best parts impossible to miss.

---

## Portfolio Documentation: Notion Support System Prompt

### The Problem

Customer support bots often fail in two opposite ways: they're either too rigid (refusing to help if the question doesn't match a template) or too loose (saying whatever sounds helpful, even when it's wrong or risky). The challenge is building a prompt that handles five distinct scenarios correctly without needing five separate prompts.

### How It Works

The system prompt defines a persona (Notion support agent), sets a default tone, and then creates conditional logic for different situation types. The key architectural decision was adding an explicit CRITICAL ISSUES section that triggers immediate escalation for data loss or security concerns — bypassing the normal troubleshooting flow entirely.

Without that section, the model treated all problems as equally fixable through troubleshooting. That worked for 4/5 test scenarios but failed badly on the angry user with a potential data loss issue — who got a polite troubleshooting response when they needed immediate action.

### Evolution

| Version | What Changed | Why |
|---------|-------------|-----|
| v1 | Initial structure: persona + tone + troubleshooting flow | Starting point |
| v2 | Added CRITICAL ISSUES escalation block | v1 failed crisis scenario — user needed urgent action, not troubleshooting |
| v3 | Refined tone instructions + added help docs references | v2 was too abrupt in non-critical cases; added "explain the why" instruction |

### Test Results

| Scenario | v1 | v2 | v3 |
|----------|----|----|-----|
| Off-topic question | ✅ | ✅ | ✅ |
| Vague product question | ✅ | ✅ | ✅ |
| Technical issue | ✅ | ✅ | ✅ |
| Angry user + data loss concern | ❌ | ✅ | ✅ |
| Feature request | ✅ | ✅ | ✅ |

---

## The Commit

```
Week 2 Day 6: documented Notion support system prompt + prompt chain artifact
```

All files pushed to `weeklyDocs/week-02/prompts/`.

---

## What Good Documentation Teaches You

Writing up the Notion prompt forced me to articulate *why* each version changed. That "why" is what interviewers ask about. Anyone can show a working prompt — the explanation of what broke and what you changed is what demonstrates actual engineering thinking.

The documentation habit from Day 6 is as important as the builds from Days 1–5.
