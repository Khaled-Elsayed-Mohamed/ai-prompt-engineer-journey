# 📖 Week 4 · Day 4 — How AI Engineers Document Projects

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Before writing my own project README, understand what good documentation looks like. Study 2-3 examples and extract the pattern.

---

## What I Looked At

- Anthropic Cookbook examples on GitHub (anthropics/anthropic-cookbook)
- Several "prompt engineering portfolio" repos on GitHub (searched: site:github.com prompt engineer portfolio)
- A handful of Medium articles on AI project writeups

---

## What the Best Ones Have in Common

**They lead with the problem, not the solution.** The first paragraph explains what problem this solves and why it's worth solving. Not "I built a classifier" — "Customer support teams receive thousands of messages and routing them manually costs time and introduces errors."

**They explain the thinking, not just the result.** The most credible projects don't just show the final prompt. They show the v1 prompt, explain what failed, then show what changed. The reasoning trail is what signals competence.

**They include concrete numbers.** "v1 scored 8/10 on initial test set. v2 scored 10/10 and handled 5 additional edge cases." Numbers make claims verifiable.

**They're honest about limitations.** "This works well for English text but hasn't been tested on high-volume production traffic." Acknowledging what your project doesn't do is a sign of maturity, not weakness.

**They make it runnable.** A README that ends with "git clone, pip install, export API_KEY, python script.py" is infinitely more impressive than one with no instructions. Employers want to know you think about how your work gets used.

---

## Patterns I'm Avoiding

**Too much preamble.** Several repos I looked at had 3 paragraphs of "AI is transforming everything" before explaining what the project actually does. Skip it.

**Screenshots of the playground.** Pasting screenshots of a chat UI doesn't demonstrate engineering. Code and documented prompts do.

**Listing features instead of explaining tradeoffs.** "Handles 6 categories" is less interesting than "I added a confidence field because ambiguous messages should be flagged for human review, not silently routed."

---

## Template I'll Use for the README

```markdown
# Project Name

## Problem
[One paragraph. Who has this problem? What makes it hard?]

## How It Works
[The prompt design + any code. Explain key decisions, not just what.]

## Prompt Evolution
[v1 → v2 table: what changed and why]

## Results
[Test inputs, scores, edge cases handled]

## Limitations
[Honest assessment]

## How to Run It
[Copy-paste-ready instructions]
```

---

## Tomorrow

Day 5: write the README using this template.
