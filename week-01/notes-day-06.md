# ✅ Day 6 — Saturday · Build Day

## Topic: Write 3 Few-shot Prompts
> [!NOTE]
> **Task:** Build and test 3 real few-shot prompts — classifier, extractor, summariser.
> **Model:** claude-haiku-4-5

---

### Prompt 1 — Customer Complaint Classifier

```
Classify the customer message below into exactly one category: 
Billing, Technical, Shipping, or General.
Respond with only the category name, nothing else.

Example 1:
Input: "I was charged twice for my subscription this month and need a refund."
Output: Billing

Example 2:
Input: "The app keeps crashing every time I try to log in."
Output: Technical

Now do this:
Input: "I can't figure out how to change my password."
Output:
```

**Result:** `Technical` — one word, nothing else. ✅

**Token cost:** 105 input tokens

---

### Prompt 2 — Info Extractor

```
Extract the name, date, and amount from the text below.
Respond in this exact format:
Name: [name]
Date: [date]
Amount: [amount]

Example 1:
Input: "John Smith placed an order on March 3rd 2024 for a total of $142.50."
Output:
Name: John Smith
Date: March 3rd 2024
Amount: $142.50

Example 2:
Input: "A payment of $89 was processed for Sarah Lee on the 14th of January."
Output:
Name: Sarah Lee
Date: 14th of January
Amount: $89

Now do this:
Input: "We received a invoice from Michael Torres dated July 22 2025 totalling $310."
Output:
```

**Result:**
```diff
+ Name: Michael Torres
+ Date: July 22 2025
+ Amount: $310
```
Exact format, no deviation. ✅

**Token cost:** 184 input tokens

---

### Prompt 3 — Article Summariser

```
Summarise the text below in exactly 2 sentences.
First sentence: the main point. Second sentence: the key supporting detail.
[2 examples provided]
```

**Input used:** McKinsey AI & jobs market paragraph

**Result:**
> *"Artificial intelligence is transforming the job market by automating significant portions of work across industries, with knowledge workers facing the biggest impact. A 2024 McKinsey report found that 30% of tasks could be automated with current AI technology, but new roles in AI oversight and human-AI collaboration are emerging to replace some displaced jobs."*

Clean 2-sentence structure, main point + supporting detail. ✅

**Token cost:** 384 input tokens

---

> [!IMPORTANT]
> **Token cost pattern across the 3 prompts: 105 → 184 → 384**
> More examples + longer inputs = more tokens consumed. Every example you add to a few-shot prompt multiplies cost across every API call. In production at scale (e.g. 50,000 tickets/month), this compounds fast.

> [!TIP]
> **Production rule:** Keep few-shot prompts minimal. Add examples only when accuracy is actually failing — not as a default. The classifier worked perfectly with just 2 examples and 105 tokens. That's the goal.

> [!NOTE]
> **Key observation:** The format instruction ("respond with only the category name, nothing else") was what controlled the output length — not the examples. Examples teach the pattern. Format instructions enforce the shape.

---

## Key Insight — Day 6

> *"Few-shot examples show the model what you want. Format instructions control how it responds. You need both — and in production, every token costs money, so use the minimum that works."*
