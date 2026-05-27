# AI Prompt Engineer Roadmap — 3 Months

**Goal:** Land an in-house AI Prompt Engineer role  
**Daily commitment:** 2 hours/day  
**Starting point:** Some tech background + hands-on prompt and API experience

---

## How Your Time is Structured

Every session follows one of two modes:

- **Learn sessions** — Read, watch, or study something new (1 hr) + take notes or summarize in your own words (1 hr)
- **Build sessions** — Spend both hours actually building or practising something hands-on

Most weeks alternate between the two so you never get stuck just reading without doing, or just doing without understanding what's behind it.

---

## Month 1: Learn the Fundamentals (Weeks 1–4)

**Theme: Understand how prompting actually works**

You already have instincts from experimenting. This month gives those instincts a solid foundation — the vocabulary, the techniques, and the "why" behind what works.

---

### Week 1 — How LLMs Work & Why Prompts Matter

**Goal:** Understand what's happening when you write a prompt, so you stop guessing and start designing.

**Topics to cover:**
- Anthropic's Prompt Engineering intro (docs.anthropic.com) — first 3 sections
- Tokens, temperature, and context windows — what they mean and why they matter
- Zero-shot vs few-shot prompting — when to use each

**Builds:**
- Rewrite 5 of your existing prompts using Role + Task + Format structure
- Run the same prompt at temperature 0 vs temperature 1. Document what you notice.
- Write 3 few-shot prompts for real tasks: classify a customer complaint, extract info from a paragraph, summarize an article

**Deliverable:** A notes doc with your 3 few-shot prompts and observations.

---

### Week 2 — Core Techniques Every Prompt Engineer Knows

**Goal:** Learn the 4–5 techniques that appear in almost every real-world prompt engineering job.

**Topics to cover:**
- Chain-of-Thought prompting — what it is, when to use it, what it costs
- Role prompting and system prompts — how to configure model behavior globally
- Prompt chaining — breaking complex tasks into sequences of smaller prompts

**Builds:**
- Compare a direct prompt vs. a "think step by step" prompt on a reasoning task
- Write a system prompt for a customer support agent. Test it with 5 different user messages.
- Build a 3-step prompt chain: extract key info from a paragraph → reformat it → write a short summary

**Deliverable:** A working 3-step prompt chain you can explain to someone.

---

### Week 3 — Working With the API

**Goal:** Move from the playground to actually calling the API in a script. This is what separates casual users from engineers.

**Topics to cover:**
- Anthropic API quickstart — read the docs before coding
- System messages, user messages, and conversation structure in the API
- Max tokens, output length control, and JSON structured output

**Builds:**
- Set up your API key, run your first API call from Python
- Write a script that accepts user input, applies a system prompt, and prints the response
- Modify your script to return structured JSON output with specific fields

**Deliverable:** A working API script saved on GitHub — your first public piece of work.

---

### Week 4 — Your First Portfolio Project

**Goal:** Build something complete enough to show an employer. Documented, tested, and real.

**Pick one:**
- A customer message classifier (routes messages to the right department)
- A resume bullet-point improver
- A meeting notes summarizer
- A product description writer

**What to do:**
- Write the core prompt and test it with at least 10 different inputs
- Improve based on what broke. Document each change.
- Wrap it in a Python script with input and output
- Write your project write-up: problem, prompt design, test results, limitations
- Post it to GitHub with a clear README

**Deliverable:** Portfolio Project #1 — live on GitHub.

---

## Month 2: Build Real Things (Weeks 5–8)

**Theme: Solve actual problems, not just exercises**

This month you move from "learning prompting" to "using prompting to build things." You'll also pick a specialisation.

---

### Week 5 — Pick Your Niche

Before building more, decide what kind of problems you want to solve.

**Your options:**
- **Content & Writing** — AI that writes, edits, or improves text for marketing and social
- **Customer Support** — AI that handles tickets, FAQs, or routes messages
- **Internal Business Tools** — AI that summarizes docs, drafts emails, or answers questions from company knowledge
- **Developer Productivity** — AI that reviews code, writes documentation, or helps debug

**What to do:**
- Find 5 job postings for "AI Prompt Engineer" in your chosen niche. Read all 5 carefully.
- Try 2–3 AI products in your niche as a user. What works? What's clunky?
- Write a niche research doc: common problems, what good looks like, what employers want
- Find 2 case studies of companies using AI in your niche
- Write 3 prompt ideas you could build for this niche. Test the most promising one.

**Deliverable:** One sentence confirming your niche: "I help [type of company] use AI to [solve this problem]."

---

### Week 6 — Portfolio Project #2

Build a more polished project in your chosen niche. This one should feel closer to something a real company would use.

**What to do:**
- Define the problem clearly. Write a one-paragraph project brief before touching any prompts.
- Write your first prompt version. Test with 10 inputs.
- Identify what broke. Fix it. Test again.
- Add a system prompt that controls tone, format, and constraints.
- Wrap in a script with a simple interface for a non-technical user.
- Write documentation: problem, approach, key prompt decisions, example inputs/outputs.

**Deliverable:** Portfolio Project #2 — in your niche, more polished than #1.

---

### Week 7 — Understanding Evaluation

**Goal:** Learn how to measure whether your prompt is actually working. This comes up in almost every prompt engineering interview.

**Topics to cover:**
- What "evaluation" means in prompt engineering and why it matters
- LLM-as-judge — using AI to evaluate AI outputs
- Building test sets: representative inputs, expected outputs, grading criteria

**Builds:**
- Take one of your existing projects. Create 20 test inputs with expected outputs.
- Run all 20 through your prompt. Grade each output: Pass / Fail / Partial.
- Write a second prompt that evaluates the quality of your first prompt's outputs.
- Write an evaluation report: methodology, results, failure analysis, fixes made.

**Deliverable:** A documented eval report for one of your projects.

---

### Week 8 — Capstone Project

This is your showpiece. Pick an ambitious but achievable project that genuinely solves a problem.

**Ideas:**
- An AI writing assistant for a specific industry
- An automated email response drafter for a support team
- A document Q&A system (user asks questions, AI answers from a provided document)
- A content repurposing tool (turns a blog post into tweets, LinkedIn posts, and a summary)

**What to do:**
- Write your project brief. Define exactly what success looks like.
- Build the core prompt system — likely 2–3 prompts working together.
- Test thoroughly with diverse, messy, real-world inputs.
- Refine based on failures. Add guardrails for edge cases.
- Write complete documentation: architecture, prompt decisions, eval results.
- Record a 3–5 minute Loom video walking through the project.

**Deliverable:** Capstone project — GitHub + Loom demo video + LinkedIn post.

---

## Month 3: Get Hired (Weeks 9–12)

**Theme: Turn your skills into a job offer**

---

### Week 9 — Polish Your Online Presence

**What to do:**
- Rewrite your LinkedIn headline to reflect your niche and current skills
- Rewrite your LinkedIn About section — who you are, what you build, what you're looking for
- Clean up your GitHub: every project needs a clear README with example inputs/outputs
- Write a one-page resume focused on your 3 projects and API experience
- Create a simple portfolio page linking all three projects + your Loom demo
- Study 10 LinkedIn posts from people with "Prompt Engineer" in their title. Note their tone.
- Get one person to review your LinkedIn and resume before applying

---

### Week 10 — Start Applying

**What to do:**
- Search "Prompt Engineer", "AI Specialist", "LLM Engineer" on job boards. Save 20 roles.
- Research the top 10 companies on your list before applying
- Apply to your first 5 roles with a short, tailored cover note (3–4 sentences, not a generic letter)
- Continue applying — target 15–20 applications this week
- Write a LinkedIn post sharing something genuinely useful you learned
- Track everything: company, role, date applied, status. Start the spreadsheet now.

---

### Week 11 — Network Actively

Most jobs come from conversations, not cold applications.

**What to do:**
- Find 10 people on LinkedIn with "Prompt Engineer" or "AI Engineer" in their title. Follow them.
- Comment thoughtfully on 5 posts from people in the AI space — specific, adds something
- Send 3 direct messages to people in roles you want: ask one specific question, not for a job
- Join one AI community: Anthropic Discord, Latent Space Discord, or a local AI meetup
- Continue applying alongside networking
- Respond to anyone who replied. Schedule calls with anyone who offers.

---

### Week 12 — Interview Prep & Close

**What to do:**
- Research common prompt engineer interview formats: live challenge, portfolio walkthrough, system design
- Practice a live prompt challenge: pick a random use case, set a 20-min timer, build a working prompt
- Prepare your portfolio walkthrough — practice explaining each project out loud in under 3 minutes
- Write answers to these 5 questions:
  - "Tell me about yourself"
  - "Walk me through a project"
  - "How do you evaluate if a prompt is working?"
  - "What would you do if a prompt kept hallucinating?"
  - "Where do you see AI prompting going in 2 years?"
- Do a mock interview: record yourself on Loom answering those 5 questions. Watch it back.
- Research salary ranges before any offer conversation

---

## Resources

| Resource | What it's for |
|----------|--------------|
| learnprompting.org | Best free structured course for beginners |
| docs.anthropic.com/en/docs/build-with-claude/prompt-engineering | Anthropic's official techniques guide |
| promptingguide.ai | Comprehensive free reference |
| github.com/anthropics/anthropic-cookbook | Real working examples with code |
| The Rundown AI (newsletter) | Daily 5-min AI news — stay current |
| Loom (free) | Record demos of your projects |
| Notion or Carrd.co (free) | Build a simple portfolio page |

---

## Milestones at a Glance

| Milestone | What you'll have |
|-----------|-----------------|
| End of Month 1 (Week 4) | Portfolio Project #1 live on GitHub |
| End of Week 6 | Niche confirmed + Project #2 published |
| End of Month 2 (Week 8) | Capstone project live with Loom demo |
| End of Week 9 | Resume, LinkedIn, and portfolio page polished |
| End of Week 10 | 15–20 applications submitted |
| End of Week 11 | Active conversations with 3–5 people in the industry |
| End of Week 12 | Interviews happening, offer in sight |

---

## One Last Thing

Two hours a day is enough — if you use them well. The biggest trap is spending both hours passively reading. Every single session should produce *something*: a prompt, a script, a note, a post, a message sent.

Come back to your notes and your coach anytime to:
- Get feedback on a prompt you built
- Prep for a specific interview
- Work through a project idea
- Get unstuck on anything technical

You've got this.
