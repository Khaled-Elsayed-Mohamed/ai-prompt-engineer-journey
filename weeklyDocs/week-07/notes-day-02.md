# 🔨 Week 7 · Day 2 — Build a 20-Input Test Set for the Classifier

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Build a proper test set for the customer message classifier — representative inputs with expected outputs, documented before running the prompt.

---

## Why You Write Expected Outputs Before Running

This is the discipline that separates real evaluation from post-hoc rationalisation. If you run the prompt first and then decide whether the output is correct, you'll unconsciously adjust your expectations to match what the model returned.

Write the expected outputs first. Then run. Then compare.

---

## The Categories (from Week 4 v2 Prompt)

- `billing` — payment issues, invoices, charges
- `technical_support` — bugs, errors, things not working
- `account` — login, passwords, account settings, billing address
- `sales` — pricing, upgrades, new features, purchasing
- `complaint` — dissatisfaction, frustration, threatening to leave
- `other` — anything that doesn't fit

---

## The 20 Test Inputs + Expected Outputs

| # | Input | Expected Category | Expected Confidence |
|---|-------|------------------|-------------------|
| 1 | "I was charged twice for my subscription this month" | billing | high |
| 2 | "The app keeps crashing when I try to upload a file" | technical_support | high |
| 3 | "I need to update my credit card on file" | billing | high |
| 4 | "Can you tell me how much the Pro plan costs?" | sales | high |
| 5 | "I've been a customer for 3 years and this is unacceptable" | complaint | high |
| 6 | "How do I reset my password?" | account | high |
| 7 | "My invoice shows the wrong company name" | billing | high |
| 8 | "The export to CSV feature isn't working" | technical_support | high |
| 9 | "I want to cancel my subscription" | account | medium |
| 10 | "Do you offer discounts for nonprofits?" | sales | high |
| 11 | "I can't log in — says my account is locked" | account | high |
| 12 | "Your service has been down for 2 hours and I'm losing business" | complaint | high |
| 13 | "Please update my billing address to 42 King St" | account | high |
| 14 | "The dashboard is showing data from last week, not today" | technical_support | high |
| 15 | "I was told by your sales team I'd get a discount but my invoice is full price" | billing | medium |
| 16 | "What integrations do you support?" | sales | medium |
| 17 | "Thanks for the help earlier, just following up" | other | medium |
| 18 | "Everyone in our team is having login issues since the update" | technical_support | high |
| 19 | "I need a receipt for my last payment for tax purposes" | billing | high |
| 20 | "Can I speak to a human please" | other | high |

---

## Design Notes on the Test Set

**Why input 9 is medium confidence:** "Cancel my subscription" could be account management or a complaint in disguise. A well-calibrated model should acknowledge the ambiguity.

**Why input 13 is `account` not `billing`:** Billing address is an account setting, not a payment issue. This was the exact failure case from Week 4 v1. Including it here specifically tests whether the fix held.

**Why input 15 is `billing` with medium confidence:** The message involves a pricing dispute — could be billing or complaint. The dominant resolution need is billing, but the confidence should reflect the ambiguity.

**Why input 20 is `other`:** A routing request for a human agent doesn't map to any service category. The model needs to recognise "I don't know enough to route this" and say so.

---

## Tomorrow

Run all 20 inputs through the classifier and grade every output.
