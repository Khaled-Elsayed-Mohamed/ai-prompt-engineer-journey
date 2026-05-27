# 📖 Week 5 · Day 2 — 3 AI Products Tried as a User

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Use 3 AI products as an end user. Not to study the prompts — to understand the product experience. What works? What's clunky? What would I do differently?

---

## Product 1: Notion AI

**What I tried:** Asked it to summarize a long document, generate meeting agenda items, and help draft a status update.

**What works:**
- Inline editing is seamless — it understands the surrounding context without you having to re-explain it
- The "improve writing" and "make shorter" commands produce good results on most inputs
- The product integration is the main value — it works on your existing content, not a separate interface

**What's clunky:**
- "Continue writing" sometimes confidently adds information that contradicts what's already there
- Longer summaries tend to over-emphasize the last part of the document
- No visibility into what it's doing — if the output is wrong, there's no way to debug or adjust the approach

**What I'd do differently (prompt engineering angle):**
The summary issue is a classic recency bias problem. A better prompt would explicitly instruct proportional coverage: "Give equal weight to each section. Do not let the length of a section determine its importance in the summary."

---

## Product 2: Otter.ai

**What I tried:** Uploaded a recording of a publicly available conference talk (not private). Used the transcript summary and action item extraction.

**What works:**
- Speaker identification is surprisingly good
- The summary gives a useful overview of a 40-minute talk in 30 seconds
- Action item extraction picks up explicit commitments well

**What's clunky:**
- Implicitly assigned action items (things that were clearly implied but not explicitly stated) get missed
- The summary doesn't distinguish between "decisions made" and "topics discussed" — both show up as bullet points
- No confidence indicators — the transcript summary presents everything with equal certainty even when the audio quality was poor

**What I'd do differently:**
Separate output sections for: decisions, action items (explicit), action items (implied), and open questions. The current format conflates all of these into a flat list.

---

## Product 3: Claude.ai (Anthropic's consumer product)

**What I tried:** Document analysis, email drafting, structured data extraction from a paragraph.

**What works:**
- XML tags for structured output work extremely well (using `<output>` tags to separate sections)
- The document analysis is excellent — it accurately identifies the main argument, supporting evidence, and counterarguments when asked
- Email drafting with a specific persona and constraints produces professional results

**What's clunky (from a user perspective, not a technical one):**
- Without a system prompt (which users can't set in the standard UI), there's no persistent context across conversations
- The "Projects" feature mitigates this but most users don't use it

**What I'd do differently as a product designer:**
Surface system-prompt-like configuration in a simpler way for power users. The complexity of "what is a system prompt" is a barrier for business users who would benefit from it.

---

## Overall Takeaway

The best-designed AI products feel like extensions of existing workflow, not new workflows. Notion AI works because it lives inside your documents. The worst UX is always the blank slate — "just type your question here" requires users to understand what the AI can do before they can use it effectively.

For internal tools, this means the product design question is: what existing workflow is this embedded in? Not: what can the AI do?
