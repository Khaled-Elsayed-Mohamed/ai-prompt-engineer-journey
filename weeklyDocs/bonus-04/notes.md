# 🧠 Week 12 — Interview Prep & Close

**AI Prompt Engineer Journey · Khaled**

> **Goal this week:** Get ready to interview well. Not to memorize answers — to practice thinking clearly under pressure about work you've actually done.

---

## Interview Formats to Expect

**Portfolio walkthrough.** You screen-share your GitHub and walk through a project. The interviewer asks why you made certain decisions. Practice this until you can walk through each project in under 3 minutes and field questions confidently.

**Live prompt challenge.** Given a use case, you design a prompt in real time — sometimes in 20 minutes, sometimes in an hour. You think out loud. They're watching your process, not just the output.

**Conceptual questions.** "How do you evaluate if a prompt is working?" "What's the difference between system prompts and few-shot examples?" "When would you use chain-of-thought?" These are not trick questions — they have clear answers that you now know.

**System design.** At more senior levels: "How would you build an AI system that processes customer support tickets end to end?" You'd describe components: ingestion, classification, routing, response generation, evaluation, monitoring.

---

## The 5 Questions to Prepare

Practice answering these out loud. Not writing answers — saying them.

**"Tell me about yourself."**
Keep it to 90 seconds. The pivot-to-AI story with a clear trajectory: iOS background, focused return, three documented projects, looking for this type of role.

**"Walk me through a project."**
Choose Project #2 (meeting notes processor) or the capstone. Structure: problem → approach → what broke → what I changed → results. Under 3 minutes.

**"How do you evaluate if a prompt is working?"**
The full answer: define what "working" means first (accuracy metric, qualitative rubric, or both), build a test set of representative inputs with expected outputs, grade actual outputs against expected, document the failure cases, and iterate. Mention the LLM-as-judge technique.

**"What would you do if a prompt kept hallucinating?"**
Diagnose first: is it hallucinating because the model doesn't know, or because the prompt isn't constraining it? For factual tasks — add "only use information from the provided context." Validate with a second prompt. Add a confidence field and flag low-confidence outputs for human review.

**"Where do you see AI prompting going in 2 years?"**
This is a "do you follow the field" question. Be specific. Mention: multimodal prompting, structured output becoming standard, evaluation becoming a discipline rather than an afterthought, tool use and agent orchestration. Have one concrete prediction you're willing to defend.

---

## The Live Challenge

The frame for a live prompt challenge:

1. **Repeat the brief back** — confirm you understand the use case before writing anything
2. **Write the system prompt first** — role, task, constraints, output format
3. **Think out loud** — say why you're making each decision
4. **Test with an example** — walk through one input/output pair
5. **Describe what you'd test next** — what edge cases would you check?

The interviewer wants to see your thinking process, not a perfect prompt. A prompt that "works" with no explanation of the thinking is less impressive than a prompt that needs one more iteration but with clear reasoning throughout.

---

## Salary Research

Before any offer conversation:
- Glassdoor: search "Prompt Engineer" + "Australia"
- LinkedIn Salary: same search
- Levels.fyi: look at "AI Engineer" if "Prompt Engineer" has limited data
- Ask in networking conversations: "What's a fair range for this kind of role?" People are often willing to share ranges.

Know your number going in. Don't be caught off guard by "what are your salary expectations?"

---

## Week 12 Mindset

You went from experimenter to job-ready in 12 weeks. You have:
- 3 documented projects with working code and test results
- A clear niche and the language to talk about it
- Evaluation skills most "prompt engineers" don't have
- A consistent commit history that proves the work was real

The interview is just showing what you've already built.

**You've earned this. Go get it. 🎯**
