# 🔨 Week 4 · Day 2 — Prompt v2: Fixing the Failures

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Fix the two failures from Day 1. Improve the prompt based on what actually broke. Re-test the full 10 inputs and add 5 new edge cases.

---

## Changes Made (v1 → v2)

**Change 1 — Expanded account category:**
```
# v1
account: login problems, password reset, access issues, account changes

# v2
account: login problems, password reset, access issues, account changes,
         subscription management, plan cancellation, data export or transfer,
         account settings
```

**Change 2 — Added disambiguation note:**
```
# Added after the category list:
Important distinction: subscription CANCELLATION goes to account (it's a plan change).
Billing disputes about charges go to billing (money already moved).
```

---

## The Prompt (v2)

```
You are a customer support routing system for a SaaS company.

Classify the following customer message into exactly one of these categories:

- billing: payment issues, unexpected charges, refund requests, invoice questions
- technical_support: bugs, errors, crashes, features not working, performance issues
- account: login problems, password reset, access issues, subscription management,
           plan cancellation, data export or transfer, account settings
- sales: pricing questions, upgrade requests, feature comparisons, new user inquiries
- complaint: dissatisfaction with service, bad experience, escalation requests
- other: anything that clearly doesn't fit the above

Important distinction:
- Subscription CANCELLATION → account (it's a plan change, not a money issue)
- Billing DISPUTE about a charge → billing (money already moved incorrectly)

Return a JSON object:
{
  "category": "one of the six categories above",
  "confidence": "high | medium | low",
  "reason": "one sentence explaining the classification"
}

Customer message: [MESSAGE]
```

---

## Re-Test: All 10 Original Inputs

| # | Message | Expected | v1 Result | v2 Result | Fixed? |
|---|---------|----------|-----------|-----------|--------|
| 1 | "I can't log in to my account" | account | ✅ | ✅ | — |
| 2 | "You charged me twice for last month" | billing | ✅ | ✅ | — |
| 3 | "The app crashes every time I open it" | technical_support | ✅ | ✅ | — |
| 4 | "What's the price for the premium plan?" | sales | ✅ | ✅ | — |
| 5 | "I'm very unhappy with the service" | complaint | ✅ | ✅ | — |
| 6 | "My invoice shows a $50 charge I don't recognise" | billing | ✅ | ✅ | — |
| 7 | "I want to cancel my subscription" | account | billing | ✅ | ✅ Fixed |
| 8 | "The search feature isn't returning any results" | technical_support | ✅ | ✅ | — |
| 9 | "I've been a customer for 5 years and this is unacceptable" | complaint | ✅ | ✅ | — |
| 10 | "Can you help me transfer my data to a new account?" | account | other | ✅ | ✅ Fixed |

**v2 Score: 10/10** ✅

---

## 5 New Edge Cases (Stress Testing)

| # | Message | Expected | Got | Correct? |
|---|---------|----------|-----|----------|
| 11 | "Hi, my name is Julia, I just signed up yesterday" | other | other | ✅ |
| 12 | "I was charged $0 this month but I should have been charged" | billing | billing | ✅ |
| 13 | "The mobile app is slower than the desktop version" | technical_support | technical_support | ✅ |
| 14 | "I'm really disappointed. This isn't what I paid for and the app is broken." | complaint or technical_support | complaint, medium confidence | ✅ (fair call) |
| 15 | "Merci, je voudrais annuler mon abonnement" (French: I'd like to cancel) | account | account | ✅ |

**New edge case score: 5/5** ✅

---

## Key Finding

The French message (test 15) correctly classified as `account` despite being non-English. The model handles multilingual input without any extra prompt instructions. Worth noting for documentation — this is a free capability, not something I had to engineer.

The ambiguous message (test 14 — complaint + technical issue) returned `complaint` with `medium` confidence. That's the right call: a human should look at medium-confidence classifications. The confidence field is doing useful work here.

---

## Tomorrow

Day 3 wraps this prompt in a Python script with a clean CLI interface.
