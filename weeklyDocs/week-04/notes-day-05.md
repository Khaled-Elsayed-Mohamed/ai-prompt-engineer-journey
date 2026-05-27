# 📝 Week 4 · Day 5 — Writing the Project README

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Turn the week's work into a project README that an employer can read cold and immediately understand. The write-up is as important as the build.

---

## What I Wrote Today

The full `prompts/classifier-README.md` — see the prompts folder for the complete document.

Here's a summary of the sections and the thinking behind each:

---

## Section 1: Problem

The problem statement I settled on after two drafts:

> Customer support inboxes grow faster than support teams. Without routing automation, every message is read by a human just to decide who else should handle it. For a team receiving 500+ messages per day, that's hours of overhead before any actual support happens.
>
> This project is a prompt-based classifier that reads incoming customer messages and outputs the correct department, a confidence level, and a one-sentence reason. Low-confidence outputs are flagged for human review rather than auto-routed.

The last sentence is the one I'm proudest of. Adding the confidence field wasn't in the original spec — I added it after test 14 returned a genuinely ambiguous message. That decision shows real product thinking: edge cases should fail gracefully, not silently.

---

## Section 2: Prompt Evolution

The table showing v1 → v2 is the most important section for a hiring audience. It shows:
- I test, not just build
- I understand *why* something failed
- I can make a targeted fix without rewriting everything

The v1 failure on "I want to cancel my subscription" → billing was a category definition problem, not a model problem. The fix was adding disambiguation language, not tweaking temperature or adding examples.

---

## Section 3: Test Results

I included all 15 test cases in a table: 10 original + 5 edge cases. The French-language test result gets a callout — it demonstrates multilingual capability without any extra engineering, which is worth highlighting.

---

## Section 4: Limitations

What I wrote honestly:

- Not tested on non-English inputs beyond one French example
- Confidence calibration is subjective — "high" means the model is confident, but I haven't validated that against human judgment at scale
- The categories are fixed at design time — adding a new department means updating the prompt and re-testing

These are real limitations. A hiring manager will spot them if I don't mention them. Better to own them.

---

## Section 5: How to Run It

Three use cases:
1. Single message via CLI argument
2. Piped input from another command
3. Processing a file of messages with a shell loop

Copy-paste ready. No assumptions about the reader's setup beyond Python and an API key.

---

## What Good Documentation Taught Me

Writing the README revealed one gap I hadn't noticed: I never explicitly documented *what* a "low confidence" classification means operationally. I added a note: "Low confidence outputs should be reviewed by a human before routing. Medium confidence can auto-route with a review queue. High confidence can auto-route directly."

That's a product decision I made implicitly during testing — the README forced me to make it explicit.

---

## Tomorrow

Day 6: final polish, push to GitHub.
