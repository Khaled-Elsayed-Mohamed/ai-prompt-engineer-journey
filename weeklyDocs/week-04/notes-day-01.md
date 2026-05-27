# 🔨 Week 4 · Day 1 — Core Prompt + 10 Input Tests

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Write the first version of the classifier prompt. Test it with 10 real customer messages. Document what works and what doesn't.

---

## The First Prompt (v1)

```
You are a customer support routing system.

Classify the following customer message into one of these categories:
- billing: payment issues, invoices, charges, refunds
- technical_support: bugs, errors, product not working, crashes
- account: login problems, password reset, access issues, account changes
- sales: pricing questions, upgrade requests, new features inquiry
- complaint: dissatisfaction, bad experience, escalation requests
- other: anything that doesn't fit the above

Return a JSON object with:
{
  "category": "string",
  "confidence": "high | medium | low",
  "reason": "one sentence explaining why"
}

Customer message: [MESSAGE]
```

---

## 10 Test Inputs and Results

| # | Message | Expected | Got | Correct? |
|---|---------|----------|-----|----------|
| 1 | "I can't log in to my account" | account | account | ✅ |
| 2 | "You charged me twice for last month" | billing | billing | ✅ |
| 3 | "The app crashes every time I open it" | technical_support | technical_support | ✅ |
| 4 | "What's the price for the premium plan?" | sales | sales | ✅ |
| 5 | "I'm very unhappy with the service" | complaint | complaint | ✅ |
| 6 | "My invoice shows a $50 charge I don't recognise" | billing | billing | ✅ |
| 7 | "I want to cancel my subscription" | account | billing | ❌ |
| 8 | "The search feature isn't returning any results" | technical_support | technical_support | ✅ |
| 9 | "I've been a customer for 5 years and this is unacceptable" | complaint | complaint | ✅ |
| 10 | "Can you help me transfer my data to a new account?" | account | other | ❌ |

**Score: 8/10**

---

## What Failed and Why

**Test 7 — "I want to cancel my subscription":**  
The model chose `billing` because cancellation often involves billing. But cancellation is an account action, not a billing one. The categories aren't wrong — the model just doesn't know where I want subscription management to live.

**Test 10 — "Can you help me transfer my data to a new account?":**  
The model chose `other` because "transfer data" didn't match any clear keyword. This is a data management / account issue — should be `account`. The prompt's description of the `account` category is too narrow: it only mentions login, password, access, and account changes. Data migration isn't mentioned.

---

## Changes to Make in v2

1. Expand the `account` category to include "subscription management, data export, account settings"
2. Add a clarifying note about `billing` vs `account` for subscription cancellation: cancellation = account, payment issues = billing

Tomorrow: implement those changes and re-test.
