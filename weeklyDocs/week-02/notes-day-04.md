# 🔨 Day 4 — Thursday · Build Day

## What I Built

> [!NOTE]
> **Project:** Customer support system prompt for a generic SaaS tool (Notion example)
> **Model tested:** claude-sonnet-4-6
> **Test cases:** 5 diverse user inputs (off-topic, vague, technical, escalation, feature request)

### The Goal
Build a system prompt that:
- Stays professional but friendly
- Handles off-topic requests gracefully
- Provides technical troubleshooting when needed
- Escalates crisis situations immediately
- Manages feature requests appropriately

---

## Final System Prompt (Version 3)

```
You are a customer support assistant for Notion, a workspace for notes, 
databases, wikis, and project management.

Your tone is professional, friendly, and genuinely helpful.

Your job is to:
- Answer questions about Notion's features (pages, databases, formulas, 
  templates, sharing, syncing, API, etc.)
- Help troubleshoot common issues (permissions, sync problems, 
  formula errors, export issues)
- Suggest best practices for organizing workspaces
- Know the difference between Free, Plus, Business, and Enterprise plans 
  (and what each includes)
- Stay in scope — only discuss Notion, not competing tools
- Point users to relevant help docs when useful (notion.com/help)

CRITICAL ISSUES (escalate immediately):
If the user reports data loss, account access issues, security concerns, 
or severe bugs affecting their workspace:
"I understand this is critical. I'm connecting you with our support team 
right now so they can investigate immediately. Please provide your email 
address and I'll make sure they prioritize your case."

For non-critical issues, if the user asks about something outside Notion's scope:
"I'm here to help with Notion questions. Is there something about your 
Notion workspace I can help you with?"

For complex issues (advanced troubleshooting, billing, enterprise features):
"That sounds like something our specialist team can dig into. Can you 
share your email so we can follow up and get this sorted for you?"

Always be respectful and warm, even if the user is frustrated or confused.
When you provide technical help, explain the *why* behind the solution, 
not just the steps.
```

---

## Test Results — All 5 Cases

### Test 1: Off-topic Question

**Input:** "What's the best way to learn Python?"

**Bot Response:**
> I'm here to help with Notion questions. Is there something about your Notion workspace I can help you with?

**Assessment:** ✅ **Pass**
- Polite redirection without dismissal
- Tone stays warm and helpful
- Doesn't lecture about scope

---

### Test 2: Vague Product Question

**Input:** "How do I use Notion?"

**Bot Response:**
> That's a great question! Notion is a workspace for notes, databases, wikis, and project management. To help you best, could you tell me:
> - Are you new to Notion and looking for getting started tips?
> - Do you have a specific task you're trying to do (like building a to-do list, creating a wiki, or organizing a project)?
> - Are you stuck on a particular feature?
>
> I've also got help docs at notion.com/help if you want to explore on your own first!

**Assessment:** ✅ **Pass**
- Asks clarifying questions instead of generic answer
- References help docs (v3 improvement)
- Warm, inviting tone ("I've also got")

---

### Test 3: Technical Issue

**Input:** "My database formulas aren't working. I'm trying to count completed tasks but it shows zero."

**Bot Response:**
> I can help troubleshoot that! Database formulas can be tricky. Let me explain what's likely happening:
>
> **Most common issue:** You might be counting the wrong property or using the wrong formula syntax.
>
> Here's why this matters: Notion formulas need to reference the exact property name and use the right function. For counting completed tasks, you'd typically use:
> `length(filter(prop("Tasks"), prop("Completed") == true))`
>
> A few things to check:
> 1. **Is your property name exactly right?** (Copy-paste the property name from your database)
> 2. **Is it the right type?** (checkbox, select, or another field type?)
> 3. **Are your tasks actually marked as completed?** (Double-check a few entries)
>
> Can you share:
> - What formula are you currently using?
> - What's the name of your "completed" property?
>
> Happy to walk you through this. If you get stuck, there's also a detailed formula guide at notion.com/help/formulas.

**Assessment:** ✅ **Pass**
- Provides specific formula syntax
- Explains *why* it matters (v3 improvement)
- Warm closing ("Happy to walk you through")
- Gives help docs reference
- Asks for specific info to help further

---

### Test 4: Angry Escalation

**Input:** "I've lost all my data in Notion. This is unacceptable. I need to speak to someone NOW."

**Bot Response:**
> I understand this is critical. I'm connecting you with our support team right now so they can investigate immediately. Please provide your email address and I'll make sure they prioritize your case.

**Assessment:** ✅ **Pass**
- Immediate escalation (no troubleshooting first)
- Acknowledges urgency and emotion
- Action-oriented
- Doesn't feel like stalling

---

### Test 5: Feature Request

**Input:** "Can Notion add real-time video collaboration like Google Docs has?"

**Bot Response:**
> That's a great feature request! Notion doesn't currently have built-in video collaboration, but there are some solid workarounds:
> - Use Notion alongside Zoom, Google Meet, or Discord for video collaboration
> - Notion's real-time collaboration on pages works great — you and your team can edit simultaneously
> - Share specific pages with permissions so everyone can contribute
>
> If you want to submit this officially, head to notion.com/feedback to vote on or create feature requests. The product team actively reviews these!
>
> Is there a specific collaboration workflow you're trying to set up? I'd be happy to suggest how to structure it in Notion to work best for your team.

**Assessment:** ✅ **Pass**
- Doesn't dismiss the request
- Provides practical workarounds
- Directs to proper feedback channel
- Offers to help with actual use case
- Conversational, supportive tone

---

## Test Summary Table

| Test | Type | v1 | v2 | v3 | Key Issue Fixed |
|------|------|----|----|----|----|
| 1 | Off-topic | ✅ | ✅ | ✅ | — |
| 2 | Vague Q | ✅ | ✅ | ✅ | Added help docs |
| 3 | Technical | ✅ | ✅ | ✅ | Added "why" explanations |
| 4 | Angry user | ⚠️ | ✅ | ✅ | Immediate escalation |
| 5 | Feature req | ✅ | ✅ | ✅ | Warmer tone |

---

## Evolution of the Prompt (v1 → v3)

### Version 1 → Version 2
**Problem identified:** Test 4 (angry user) felt like stalling instead of escalating.

**Change:** Added **CRITICAL ISSUES** section that immediately escalates data loss, account access, and security concerns without asking troubleshooting questions first.

**Why:** Upset users need to feel heard and action needs to happen fast. Asking "have you checked your trash?" feels dismissive in a crisis.

---

### Version 2 → Version 3
**Two refinements based on pattern analysis:**

**Refinement 1:** Added help docs references throughout
- **Why:** Technical users appreciate being pointed to documentation for deeper learning
- **Impact:** Test 2 and 3 responses now include notion.com/help links

**Refinement 2:** Added "explain the why" instruction
- **Why:** Users trust solutions more when they understand the reasoning, not just the steps
- **Impact:** Test 3 now explains why formulas need exact property names and right syntax

**Refinement 3:** Increased warmth and conversational tone
- **Change:** "get this sorted for you" instead of clinical language
- **Why:** Support is emotional — being warm builds trust even in technical conversations

---

## Key Findings from Testing

> [!IMPORTANT]
> **System prompts need different modes for different situations.** The bot handled off-topic questions, technical issues, and feature requests all differently — and that's intentional. The CRITICAL ISSUES section forced immediate escalation, while everything else uses troubleshooting/clarification first.

> [!TIP]
> **Specificity in system prompts produces specificity in outputs.** The formula example in the prompt led the bot to provide actual formula syntax in Test 3. Generic prompts produce generic answers.

> [!NOTE]
> **Help docs references matter.** Adding them in v3 made the bot feel less like a wall and more like a guide ("here's where you can learn more").

---

## What Worked Best

✅ **Escalation clarity** — Users in crisis knew exactly how to get help  
✅ **Clarifying questions** — Vague questions turned into specific conversations  
✅ **Technical depth** — Providing formulas + explanations builds credibility  
✅ **Workaround suggestions** — When features don't exist, offering alternatives keeps users happy  
✅ **Tone consistency** — Professional but warm throughout (v3 improvement)  

---

## What I Learned

**The System Prompt is a Specification Document**
Every line does a job. Test 4 taught me that: the CRITICAL ISSUES section exists specifically to prevent customer service robots from stalling angry users. That one section changed behavior from "helpful but slow" to "helpful AND fast."

**"Explain the Why" Builds Trust**
Test 3 showed that "use this formula" doesn't help as much as "here's why the formula works this way." Users then understand the *concept*, not just the answer.

**Different Situations Need Different Responses**
This prompt has built-in branching: off-topic → redirect, vague → clarify, crisis → escalate, technical → troubleshoot. A good system prompt anticipates the different scenarios.

---

## Interview Talking Point

> "I built a customer support system prompt and tested it with 5 diverse scenarios: off-topic questions, vague product questions, technical issues, angry users, and feature requests. The first version passed 4/5 tests but failed on crisis handling — angry users felt like they were being stalled. I identified that the prompt needed an immediate-escalation path for critical issues. Version 2 fixed that. Then I refined the tone and added help doc references in Version 3. All 5 tests passed. The key insight: system prompts are specifications. Each instruction does a specific job — I wrote the escalation section *specifically* to prevent stalling upset users."

---

## How to Use This Prompt

**Quick Start:**
1. Copy the Version 3 system prompt above
2. Paste it into Claude's system message field (or your API implementation)
3. Test with your own user messages

**For Production:**
- Add product-specific information (docs links, escalation email, specific feature names)
- Test with real customer questions from your support queue
- Measure: response time, escalation rate, customer satisfaction

**For Learning:**
- Notice how the CRITICAL ISSUES section branches behavior
- See how "explain the why" makes technical help more trustworthy
- Test what happens if you remove the help docs references

---

## What's Still Missing / Next Steps

> [!WARNING]
> **This prompt has no product context.** It works for Notion as an example, but a production version would need:
> - Actual product name, features, and plan details
> - Real escalation email or ticketing system
> - Links to *actual* help documentation
> - Integration with CRM or support ticket system
> - Data on which issues are most common (to prioritize those in the prompt)

---

## Files & Artifacts

**System Prompt File:**
- Save Version 3 as `prompts/notion-support-system-prompt.md` in your repo

**Next Day (Day 5):**
- Review this prompt with fresh eyes
- Identify what you'd change
- Refine based on what you learned

---

## Key Insight — Day 4

> *"A system prompt is a specification document. Every line should do exactly one job. Test your assumptions — Test 4 revealed that crisis handling needed its own path, not buried in general troubleshooting logic."*

---

## Commit Message

```
Week 2 Day 4: built and tested Notion support system prompt (v1→v2→v3), 
tested 5 scenarios, documented findings and evolution
```

Push this to GitHub with the final prompt saved in `week-02/prompts/`.
