# Prompt 07 — Customer Complaint Classifier
**Day 6 · Few-shot prompting**

## The Prompt
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

## Result
```
Technical
```

## Notes
- Token cost: 105 input tokens
- Output was one word — exactly as instructed
- The format instruction ("respond with only the category name") controlled output length, not the examples
- Works with just 2 examples — no need to add more unless accuracy fails
