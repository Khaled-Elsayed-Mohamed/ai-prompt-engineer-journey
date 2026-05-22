# Khaled's 3-Month AI Prompt Engineer Roadmap
**Goal:** Land an in-house AI Prompt Engineer role by ~August 2026  
**Daily commitment:** 2 hours/day, every day  
**Starting point:** Some tech background + hands-on prompt & API experience

---

## How Your Days Are Structured

Every day follows one of two modes:

- **Learn days** — Read, watch, or study something new (1 hr) + take notes or summarize it in your own words (1 hr)
- **Build days** — Spend both hours actually building or practicing something hands-on

Most weeks alternate between the two so you never get stuck just reading without doing, or just doing without understanding what's behind it.

---

## Month 1: Learn the Fundamentals (Weeks 1–4)
**Theme: Understand how prompting actually works**

You already have instincts from experimenting. This month gives those instincts a solid foundation — the vocabulary, the techniques, and the "why" behind what works.

---

### Week 1 — How LLMs Work & Why Prompts Matter

**Goal:** Understand what's happening when you write a prompt, so you stop guessing and start designing.

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Learn | Read Anthropic's Prompt Engineering intro (docs.anthropic.com) — just the first 3 sections |
| Tue | Build | Take 5 prompts you've written before. Rewrite each one using a clear role + task + format structure |
| Wed | Learn | Learn what tokens, temperature, and context windows mean — use the Anthropic or OpenAI docs |
| Thu | Build | Run the same prompt at temperature 0 vs temperature 1 in the playground. Write down what you notice |
| Fri | Learn | Read about zero-shot vs few-shot prompting (learnprompting.org — free) |
| Sat | Build | Write 3 few-shot prompts for real tasks: classify a customer complaint, extract info from a paragraph, summarize an article |
| Sun | Review | Write a half-page in your own words: "What I learned this week and what surprised me" |

**Deliverable:** A personal notes doc with your 3 few-shot prompts and what you observed.

---

### Week 2 — Core Techniques Every Prompt Engineer Knows

**Goal:** Learn the 4–5 techniques that appear in almost every real-world prompt engineering job.

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Learn | Study Chain-of-Thought prompting — read the explainer on learnprompting.org |
| Tue | Build | Take a reasoning or math problem. Compare a direct prompt vs a "think step by step" prompt. Screenshot both outputs |
| Wed | Learn | Study role prompting and system prompts — how to set up an AI persona or context |
| Thu | Build | Write a system prompt for a helpful customer support agent. Test it with 5 different user messages |
| Fri | Learn | Study prompt chaining — breaking a big task into a sequence of smaller prompts |
| Sat | Build | Build a 3-step prompt chain: (1) extract key info from a paragraph, (2) reformat it, (3) write a short summary |
| Sun | Review | Add your best examples to a "Techniques" folder — this becomes portfolio material later |

**Deliverable:** A working 3-step prompt chain you can explain to someone.

---

### Week 3 — Working With the API

**Goal:** Move from the playground to actually calling the API in a script. This is what separates casual users from engineers.

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Learn | Read the Anthropic API quickstart (or OpenAI — pick one). Just read, don't code yet |
| Tue | Build | Set up your API key and run your first API call from a Python or JavaScript script |
| Wed | Learn | Learn about system messages, user messages, and conversation structure in the API |
| Thu | Build | Write a script that takes a user's input, sends it to the API with a system prompt, and prints the response |
| Fri | Learn | Learn about max tokens and how to control output length and format |
| Wed | Build | Modify your script to return structured output (e.g., always respond in JSON with specific fields) |
| Sun | Review | Clean up your script and add comments explaining each part. Save it to GitHub |

**Deliverable:** A working API script saved on GitHub — your first public piece of work.

---

### Week 4 — Your First Portfolio Project

**Goal:** Build something complete enough to show an employer. It doesn't need to be impressive — it needs to be documented and real.

**Pick one of these (all are beginner-friendly):**
- A customer message classifier (routes messages to the right department)
- A resume bullet-point improver
- A meeting notes summarizer
- A product description writer

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Build | Write the core prompt for your chosen project. Test it with at least 10 different inputs |
| Tue | Build | Improve the prompt based on what broke or gave bad results. Document each change you made |
| Wed | Build | Wrap it in a simple Python script with an input and output |
| Thu | Learn | Read 2 examples of how others document their AI projects (search GitHub or Medium) |
| Fri | Build | Write your project write-up: What problem it solves, how your prompt works, what you tested |
| Sat | Build | Post it to GitHub with a clear README. Share on LinkedIn with a short post explaining what you built |
| Sun | Review | Read through everything you built in Month 1. What gaps do you still feel? Write them down |

**Deliverable:** Portfolio Project #1 — live on GitHub and announced on LinkedIn.

---

## Month 2: Build Real Things (Weeks 5–8)
**Theme: Solve actual problems, not just exercises**

This month you move from "learning prompting" to "using prompting to build things." You'll also pick a specialization — the specific type of work you want to be hired for.

---

### Week 5 — Pick Your Niche

Before building more, you need to know *what kind of problems* you want to solve. This shapes your next two projects and makes you much easier for employers to hire.

**Your options:**

- **Content & Writing** — AI that writes, edits, or improves text for marketing, blogs, or social media
- **Customer Support** — AI that handles tickets, FAQs, or routes customer messages
- **Internal Business Tools** — AI that summarizes docs, drafts emails, or answers questions about a company
- **Developer Productivity** — AI that reviews code, writes documentation, or helps debug

**This week:** Research your chosen niche — not to build yet, just to understand it.

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Learn | Find 5 job postings for "AI Prompt Engineer" or "LLM Engineer" in your niche. Read all 5 carefully |
| Tue | Learn | Look at 2–3 AI products in your niche (try them as a user). What do they do well? What's clunky? |
| Wed | Build | Write a "niche research" doc: the common problems, what good looks like, what employers want |
| Thu | Learn | Find 2 articles or case studies about how companies are using AI in your niche |
| Fri | Build | Write 3 prompt ideas you could build for companies in your niche |
| Sat | Build | Test the most interesting of those 3 ideas — just a rough draft prompt to see if it's viable |
| Sun | Review | Confirm your niche. Write one sentence: "I help [type of company] use AI to [solve this problem]." |

---

### Week 6 — Portfolio Project #2

Build a more polished project in your chosen niche. This one should feel closer to something a real company would use.

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Build | Define the problem clearly. Write a one-paragraph "project brief" before touching any prompts |
| Tue | Build | Write your first version of the prompt. Test with 10 inputs |
| Wed | Build | Identify what broke. Fix it. Test again |
| Thu | Build | Add a system prompt that controls tone, format, and constraints |
| Fri | Build | Wrap in a script. Add a simple way for a non-technical person to use it (e.g., reads from a text file) |
| Sat | Build | Write documentation: problem, approach, key prompt decisions, example inputs/outputs |
| Sun | Review | Publish to GitHub. Write a LinkedIn post about the key decision you made in this project |

**Deliverable:** Portfolio Project #2 — in your niche, more polished than #1.

---

### Week 7 — Understanding Evaluation

**Goal:** Learn how to measure whether your prompt is actually working. This comes up in almost every prompt engineering interview.

You don't need complex tools — just the mindset.

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Learn | Read about what "prompt evaluation" means — search "how to evaluate LLM outputs" on Medium or the Anthropic blog |
| Tue | Build | Take a prompt you've already built. Create 20 test inputs with "expected outputs" for each |
| Wed | Build | Run all 20 through your prompt. Grade each output: Pass / Fail / Partial |
| Thu | Learn | Learn about the concept of "LLM as judge" — using AI to evaluate AI outputs |
| Fri | Build | Write a second prompt that evaluates the output of your first one (was it helpful? accurate? well-formatted?) |
| Sat | Build | Write up a short "Evaluation Report" for one of your projects — this is something you can show in interviews |
| Sun | Review | Add your evaluation framework to your GitHub portfolio |

**Deliverable:** A documented eval report for one of your projects.

---

### Week 8 — Capstone Project (Your Best Work)

This is your showpiece. Pick an ambitious but achievable project that genuinely solves a problem.

**Ideas:**
- An AI writing assistant for a specific industry (e.g., real estate listings, job descriptions)
- An automated email response drafter for a customer support team
- A document Q&A system (user asks questions, AI answers from a provided document)
- A content repurposing tool (turns a blog post into tweets, LinkedIn posts, and a summary)

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Build | Write your project brief. Define exactly what success looks like |
| Tue | Build | Build the core prompt system — it may be 2–3 prompts working together |
| Wed | Build | Test thoroughly with diverse, messy, real-world inputs |
| Thu | Build | Refine based on failures. Add guardrails for edge cases |
| Fri | Build | Write complete documentation: architecture, prompt decisions, eval results |
| Sat | Build | Record a 3–5 minute Loom video walking through the project (this is gold for applications) |
| Sun | Review | Publish everything. This is your best work — announce it properly on LinkedIn |

**Deliverable:** Capstone project — GitHub + Loom demo video + LinkedIn post.

---

## Month 3: Get Hired (Weeks 9–12)
**Theme: Turn your skills into a job offer**

---

### Week 9 — Polish Your Online Presence

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Build | Rewrite your LinkedIn headline: "AI Prompt Engineer | [Niche] | [Key skill]" |
| Tue | Build | Rewrite your LinkedIn About section — 3 short paragraphs: who you are, what you build, what you're looking for |
| Wed | Build | Clean up your GitHub: make sure all 3 projects have clear READMEs with example inputs/outputs |
| Thu | Build | Write a one-page resume. Focus on: your 3 projects, API experience, measurable results |
| Fri | Build | Create a simple portfolio page on Notion or Carrd.co linking all three projects + your Loom video |
| Sat | Learn | Read 10 LinkedIn posts from people with "Prompt Engineer" or "AI Engineer" in their title. Study their tone |
| Sun | Review | Ask one person (friend, colleague, or me) to review your LinkedIn and resume before you start applying |

---

### Week 10 — Start Applying

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Build | Search "Prompt Engineer", "AI Specialist", "LLM Engineer" on LinkedIn Jobs. Save 20 roles you'd apply for |
| Tue | Build | Research the top 10 companies on your list — understand what they do and how AI fits their product |
| Wed | Build | Apply to 5 roles with a short, tailored cover note (3–4 sentences, not a generic letter) |
| Thu | Build | Apply to 5 more roles |
| Fri | Build | Write a LinkedIn post sharing something genuinely useful you learned — builds visibility with recruiters |
| Sat | Build | Apply to 3–5 more roles. Start tracking everything in a spreadsheet: company, role, date applied, status |
| Sun | Review | Review what you've applied to. Do your materials match what those companies are looking for? Adjust if needed |

---

### Week 11 — Network Actively

Most jobs come from conversations, not cold applications. This week you start both.

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Build | Find 10 people on LinkedIn with "Prompt Engineer" or "AI Engineer" in their title. Follow all of them |
| Tue | Build | Comment thoughtfully on 5 posts from people in the AI space (real, specific comments — not "great post!") |
| Wed | Build | Send 3 direct messages to people in roles you want: "I admire your work on [X], would love to ask you one question about how you got into this" |
| Thu | Build | Join one AI community: Anthropic Discord, Latent Space Discord, or a local AI meetup group |
| Fri | Build | Apply 5 more roles. Prioritize companies where you found someone to also reach out to |
| Sat | Build | If anyone replied to your DMs, respond and schedule a 15-min call |
| Sun | Review | How many conversations do you have active? Goal is 3–5 real conversations by end of this week |

---

### Week 12 — Interview Prep & Close

| Day | Mode | What to do |
|-----|------|-----------|
| Mon | Learn | Research common prompt engineer interview formats: live challenge, portfolio walkthrough, system design |
| Tue | Build | Practice a live prompt challenge: pick a random use case, set a 20-min timer, build a working prompt |
| Wed | Build | Prepare your portfolio walkthrough — practice explaining each project out loud in under 3 minutes each |
| Thu | Build | Write answers to these 5 questions: "Tell me about yourself", "Walk me through a project", "How do you evaluate if a prompt is working?", "What would you do if a prompt kept hallucinating?", "Where do you see AI prompting going in 2 years?" |
| Fri | Build | Do a mock interview (record yourself on Loom answering those 5 questions — watch it back) |
| Sat | Build | Research salary ranges: Glassdoor, LinkedIn Salary, Levels.fyi for "Prompt Engineer" or "AI Engineer" |
| Sun | Review | Celebrate how far you've come. You went from experimenter to job-ready in 90 days. |

---

## Resources (Simple, Free, Beginner-Friendly)

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

## Your Milestones at a Glance

| Date | What you'll have |
|------|-----------------|
| Jun 21 (end of Month 1) | Portfolio Project #1 live on GitHub |
| Jul 7 (end of Week 6) | Niche chosen + Project #2 published |
| Jul 21 (end of Month 2) | Capstone project live with Loom demo |
| Jul 28 | Resume, LinkedIn, and portfolio page polished |
| Aug 4 | 15–20 applications submitted |
| Aug 11 | Active conversations with 3–5 people in the industry |
| Aug 21 | Interviews happening, offer in sight |

---

## One Last Thing

Two hours a day is enough — if you use them well. The biggest trap is spending both hours passively reading. Every single day should produce *something*: a prompt, a script, a note, a post, a message sent. If you can't point to what you made today, the day didn't count.

Come back to me anytime to:
- Get feedback on a prompt you built
- Prep for a specific interview
- Work through a project idea
- Get unstuck on anything technical

You've got this. Let's check in at the end of Week 1.

---

---

# GitHub Documentation Guide
**For Khaled — returning to tech after 4 years, pivoting to AI Prompt Engineering**

Your GitHub already shows iOS/Swift work. That's a strength, not a liability — it proves you can build real things. Now we're adding a new chapter to that profile. This guide tells you exactly how to set up and maintain your AI journey on GitHub so that by Month 3, your profile tells a clear, compelling story to any hiring manager who looks you up.

---

## Why Document on GitHub

Most people learning a new field keep their notes in Notion, their prompts in chat windows, and their scripts on their laptop. They have nothing to show for months of work.

You're going to be different. Every prompt you write, every experiment you run, every project you build goes on GitHub. This does three things:

1. **Proves you're serious** — a consistent commit history over 3 months signals discipline, not just interest
2. **Builds your portfolio automatically** — by Month 3, your repos are already your evidence
3. **Makes interviews easy** — you walk in with real work to show, not just things to describe

---

## Step 1 — Set Up Your Profile README

A profile README appears at the top of your GitHub profile page. It's the first thing a recruiter or hiring manager sees. Right now your profile shows nothing except your Swift repos. Let's change that.

**How to create it:**
1. Go to github.com and create a new repository
2. Name it exactly: `Khaled-Elsayed-Mohamed` (same as your username)
3. Check "Add a README file"
4. Make it public

**What to put in it** — keep it short and direct:

```markdown
# Hi, I'm Khaled 👋

I'm an AI Prompt Engineer in training, currently building towards my first in-house role.

Previously: iOS/Swift developer (MediaFinder, animations, MVC patterns)
Now: Focused on LLM prompt engineering, API integration, and AI product building

## What I'm building
- 🔨 Prompt engineering projects across customer support, content, and business tools
- 📓 Documenting my full 3-month learning journey (see: ai-prompt-engineer-journey)
- 🌏 Based in Australia

## Skills
`Prompt Engineering` `Python` `Anthropic API` `OpenAI API` `Swift` `iOS`

## Currently Learning
Working through a structured 3-month AI Prompt Engineer roadmap.
Week by week notes and projects are in my pinned repo below.
```

Update this every month as your skills grow.

---

## Step 2 — Create Your Main Journey Repo

This is the heart of your GitHub presence for the next 3 months. Everything goes here.

**Create a repo called:** `ai-prompt-engineer-journey`  
Make it public. Add a README. No template needed.

**Folder structure to set up on Day 1:**

```
ai-prompt-engineer-journey/
│
├── README.md                  ← Overview of the whole journey
│
├── week-01/
│   ├── notes.md               ← What you studied, key takeaways
│   ├── prompts/               ← .txt or .md files with your prompts
│   └── scripts/               ← Any Python/JS files you wrote
│
├── week-02/
│   ├── notes.md
│   ├── prompts/
│   └── scripts/
│
├── projects/
│   ├── project-01-classifier/ ← Each project gets its own folder
│   │   ├── README.md
│   │   ├── prompt.md
│   │   └── script.py
│   ├── project-02/
│   └── project-03-capstone/
│
└── resources.md               ← Links, articles, tools you've found useful
```

**Your journey README should say:**

```markdown
# AI Prompt Engineer Journey — Khaled

3-month structured learning plan starting May 2026.
Goal: In-house AI Prompt Engineer role by August 2026.

## Progress
- [x] Week 1 — Foundations & Mental Models
- [ ] Week 2 — Core Techniques
- [ ] Week 3 — Working with the API
- [ ] Week 4 — Portfolio Project #1
...

## Projects
| Project | Description | Status |
|---------|-------------|--------|
| [Project 1](./projects/project-01/) | Customer message classifier | ✅ Done |
| [Project 2](./projects/project-02/) | TBD based on niche | 🔨 In progress |
| [Capstone](./projects/project-03-capstone/) | Flagship project | ⏳ Upcoming |

## Background
After 4 years away from tech (family first — no regrets), I'm returning with a clear goal:
become a professional AI Prompt Engineer. This repo documents every step.
```

That last paragraph matters. Employers respect honesty about a gap far more than silence. A deliberate return to the field is a strength, not a weakness.

---

## Step 3 — Your Daily Git Habit (2-Minute Routine)

You've used git before, so this is just a refresher shaped around your new routine. At the end of each 2-hour session, before you close your laptop:

```bash
# Navigate to your journey repo
cd ai-prompt-engineer-journey

# Check what you changed
git status

# Add everything you worked on
git add .

# Commit with a meaningful message
git commit -m "Week 1 Day 1: notes on zero-shot vs few-shot prompting"

# Push to GitHub
git push
```

**Commit message formula:** `Week X Day X: [what you did in plain English]`

Examples:
- `Week 1 Day 3: built 3 few-shot prompts for customer support classification`
- `Week 3 Day 2: first working API call with system prompt and JSON output`
- `Week 4 Day 5: published Project 1 README and LinkedIn post`

This takes 2 minutes. Do it every single day. A consistent green commit graph is one of the most powerful silent signals on your profile.

---

## Step 4 — How to Document Each Week

Each week folder gets a `notes.md` file. Keep it simple — this isn't for anyone else, it's for you and for proof of work.

**Template for notes.md:**

```markdown
# Week X Notes — [Theme]
Dates: [start date] to [end date]

## What I studied
- [Topic 1]: [2-3 sentences on what you learned]
- [Topic 2]: [2-3 sentences]

## What I built
- [Thing you made]: [why you made it this way, what you changed]

## What surprised me or didn't work
[Honest notes on what confused you, what failed, what you had to redo]

## Key insight this week
[One sentence. The thing you'd tell a friend.]

## Links & resources used
- [resource name](url)
```

It takes 15 minutes to write at the end of the week. It's the most valuable 15 minutes you'll spend.

---

## Step 5 — Each Project Gets Its Own README

When you build a project (Weeks 4, 6, and 8), give it a proper README. This is what employers read. It should answer five questions:

```markdown
# Project Name

## What problem does this solve?
[1-2 sentences. Who is this for and what pain does it fix?]

## How it works
[3-5 sentences. Explain the prompt design and any scripts involved.
No jargon — write like you're explaining to a smart non-technical person.]

## The core prompt
[Paste your actual prompt here, or link to prompt.md]

## What I tested & what I learned
[How many inputs did you test? What broke? What did you change and why?]

## How to run it
[Simple steps — even if it's just "paste this prompt into Claude and replace X with your input"]
```

---

## Step 6 — Pin Your Best Repos

Once you have your journey repo and your first project, pin them to your profile so they appear at the top:

1. Go to your GitHub profile
2. Click "Customize your pins"
3. Select `ai-prompt-engineer-journey` and your best project repos
4. Unpin the Swift repos (or leave one — it shows you can code)

By Month 3, your pinned repos should be: your journey repo + 2–3 AI projects. That's the profile of someone who gets interviews.

---

## The Honest Note About the Gap

You've been away for 4 years. Your Swift repos are from a different chapter. Don't hide that — own it in your profile README and in your documentation.

"After 4 years focused on family, I'm returning to tech with a clear direction" is a story. It shows values, intentionality, and self-awareness. Hiring managers are people too. A clean return to the field documented in real time — commits, projects, notes — is more compelling than someone who never left but has nothing to show.

Your gap is not a hole in your story. It's the opening line.

---

## Quick Git Commands Refresher

Since it's been a few years:

```bash
git init                        # Start a new repo (only needed locally)
git clone [url]                 # Copy a repo from GitHub to your machine
git status                      # See what's changed
git add .                       # Stage all changes
git add filename.md             # Stage one specific file
git commit -m "your message"    # Save a snapshot with a label
git push                        # Send your commits to GitHub
git pull                        # Get latest changes from GitHub
git log --oneline               # See recent commit history
```

If you run into merge conflicts or anything more complex, come back to me and I'll walk you through it.

---

## Your GitHub Checklist for Day 1

- [ ] Create profile README repo (`Khaled-Elsayed-Mohamed/Khaled-Elsayed-Mohamed`)
- [ ] Write and publish your profile README
- [ ] Create `ai-prompt-engineer-journey` repo (public)
- [ ] Set up the folder structure above
- [ ] Write your journey README with the progress checklist
- [ ] Pin `ai-prompt-engineer-journey` to your profile
- [ ] Make your first commit: even if it's just the folder structure and an empty notes.md

That first commit is your starting gun. Everything after that is momentum.
