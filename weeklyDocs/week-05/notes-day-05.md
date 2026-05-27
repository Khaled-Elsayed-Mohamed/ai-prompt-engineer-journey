# 🔨 Week 5 · Day 5 — 3 Prompt Ideas for Internal Business Tools

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Generate 3 viable prompt project ideas for the internal tools niche. Evaluate each one. Choose the best for Week 6.

---

## The 3 Ideas

---

### Idea 1: Meeting Notes Processor

**What it does:** Takes raw, unstructured meeting notes (the kind someone types quickly during a call) and outputs a structured JSON object with summary, decisions, action items with owners, and open questions.

**Why it's interesting:**
- Almost every company has this problem
- The output is immediately useful — you can pipe it to Slack, Notion, email, JIRA
- Structured output means it's testable and measurable

**Technical complexity:** Medium. Multi-field extraction. Needs to handle ambiguous ownership ("we should fix this" → owner is unclear) and implied commitments.

**Risk:** Meeting notes vary wildly in format and quality. Need to test with genuinely messy inputs, not clean ones.

**Portfolio value:** High. Every interviewer at a company that has meetings will immediately understand the use case.

---

### Idea 2: Document Q&A with Citation

**What it does:** Takes a PDF or document and a user question. Answers the question using only content from the document, with a specific page/section citation for each answer.

**Why it's interesting:**
- Directly related to the case studies from Day 4
- Citation requirement adds real reliability engineering complexity
- Demonstrates RAG-adjacent thinking even without a full vector database

**Technical complexity:** High. Need to handle long documents (chunking), citation accuracy, and "I don't know" responses.

**Risk:** Without a real RAG setup, document length is limited by context window. The prompt engineering part is strong but the full production system requires more infrastructure.

**Portfolio value:** Very high. But the implementation gap (playground vs. production) is harder to explain to a non-technical interviewer.

---

### Idea 3: Email Thread Summariser & Reply Drafter

**What it does:** Paste an email thread, get back a summary of the conversation so far and a draft reply appropriate to the context.

**Why it's interesting:**
- Extremely common workplace problem
- Multi-step chain (summarize → draft) is good portfolio material
- Easy to demo convincingly

**Technical complexity:** Low-Medium. The summarization is straightforward. The draft quality depends on how well the system prompt captures the right tone.

**Risk:** The output is hard to evaluate objectively — "good email" is subjective. Unlike the classifier (10/10) or meeting notes (decision extracted or not), reply quality is harder to measure.

**Portfolio value:** Medium. It's been done a lot. Needs a distinctive angle to stand out.

---

## The Decision: Idea 1 — Meeting Notes Processor

**Why:**
- Best ratio of business value to technical scope for a one-week project
- Fully testable with objective criteria (was the decision captured? was the owner identified?)
- High portfolio differentiation — structured output with 4 distinct output sections is more impressive than a flat summary
- Every company is a potential customer — universal appeal in interviews

---

## Tomorrow

Day 6: rough draft of the core prompt. Test it with 3 real examples of messy meeting notes.
