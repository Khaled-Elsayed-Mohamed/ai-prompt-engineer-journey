# Customer Message Classifier — Prompt Documentation

## Final Prompt (v2)

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

## Version History

### v1 — Initial Prompt

**Problem:** The `account` category was defined too narrowly. Only covered login, password, access, and account changes. No mention of subscription management or data migration.

**Failure cases:**
- "I want to cancel my subscription" → routed to `billing` instead of `account`
- "Can you help me transfer my data to a new account?" → routed to `other` instead of `account`

**Score:** 8/10

### v2 — Fixed Category Definitions

**Changes:**
1. Expanded `account` category: added subscription management, plan cancellation, data export/transfer, account settings
2. Added explicit disambiguation note: subscription cancellation = account, billing disputes = billing

**Score:** 10/10 (original 10 tests) + 5/5 (additional edge cases)

---

## Test Results

| # | Message | Expected | v2 Result | Pass? |
|---|---------|----------|-----------|-------|
| 1 | "I can't log in to my account" | account | account (high) | ✅ |
| 2 | "You charged me twice for last month" | billing | billing (high) | ✅ |
| 3 | "The app crashes every time I open it" | technical_support | technical_support (high) | ✅ |
| 4 | "What's the price for the premium plan?" | sales | sales (high) | ✅ |
| 5 | "I'm very unhappy with the service" | complaint | complaint (high) | ✅ |
| 6 | "My invoice shows a $50 charge I don't recognise" | billing | billing (high) | ✅ |
| 7 | "I want to cancel my subscription" | account | account (high) | ✅ |
| 8 | "The search feature isn't returning any results" | technical_support | technical_support (high) | ✅ |
| 9 | "I've been a customer for 5 years and this is unacceptable" | complaint | complaint (high) | ✅ |
| 10 | "Can you help me transfer my data to a new account?" | account | account (high) | ✅ |
| 11 | "Hi, my name is Julia, I just signed up yesterday" | other | other (medium) | ✅ |
| 12 | "I was charged $0 this month but I should have been charged" | billing | billing (medium) | ✅ |
| 13 | "The mobile app is slower than the desktop version" | technical_support | technical_support (high) | ✅ |
| 14 | "I'm really disappointed. This isn't what I paid for and the app is broken." | complaint | complaint (medium) | ✅ |
| 15 | "Merci, je voudrais annuler mon abonnement" | account | account (high) | ✅ |

**Final: 15/15** ✅

---

## Design Notes

**Why a confidence field?**
Ambiguous messages (test 14 — complaint + technical issue) deserve human review, not silent auto-routing. The confidence field creates a natural escalation path: high confidence → auto-route, medium → review queue, low → human triage.

**Why no few-shot examples?**
Testing showed zero-shot performed at 100% after v2 category definitions were tightened. Adding examples would increase tokens and complexity without improving accuracy in this case. The right amount of examples is the minimum that achieves the target performance.

**Multilingual handling:**
The model correctly classified test 15 (French) without any multilingual instructions. This is a free capability — document it, don't engineer what's already there.
