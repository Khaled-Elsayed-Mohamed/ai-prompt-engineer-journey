# Prompt 08 — Info Extractor
**Day 6 · Few-shot prompting**

## The Prompt
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

## Result
```
Name: Michael Torres
Date: July 22 2025
Amount: $310
```

## Notes
- Token cost: 184 input tokens
- Output matched the exact format from the examples — no deviation
- Two examples were enough to teach the pattern
- Real-world use case: invoice processing, form data extraction, CRM automation
