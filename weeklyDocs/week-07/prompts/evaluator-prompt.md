# LLM-as-Judge Evaluator Prompt

## What This Does

A second prompt that evaluates the output of the customer message classifier. Rather than manually grading every output, this prompt assesses three dimensions: correctness, confidence calibration, and reason quality.

## The Prompt

```
You are an evaluation judge for an AI classification system.

You will be given:
1. The original customer message
2. The classifier's output (category, confidence, reason)
3. The correct category (human-verified)

Evaluate the classifier's output on three dimensions:

CORRECTNESS: Is the category correct?
- "correct": category matches the verified label
- "incorrect": category does not match

CONFIDENCE_CALIBRATION: Is the stated confidence appropriate?
- "well_calibrated": confidence level fits the clarity of the input (high for clear cases, low for ambiguous ones)
- "overconfident": model said high/medium but the input was genuinely ambiguous
- "underconfident": model said low/medium but the input was clearly one category

REASON_QUALITY: Does the reason accurately explain the classification?
- "good": reason correctly identifies the key signal in the message
- "weak": reason is vague or generic (e.g., "this message is about billing")
- "wrong": reason contains an error or mischaracterizes the message

Return JSON:
{
  "correctness": "correct | incorrect",
  "confidence_calibration": "well_calibrated | overconfident | underconfident",
  "reason_quality": "good | weak | wrong",
  "notes": "one sentence explaining any issues found, or null if all dimensions pass"
}

---

Customer message: [MESSAGE]
Classifier output: [JSON OUTPUT FROM CLASSIFIER]
Correct category: [VERIFIED LABEL]
```

## When to Use LLM-as-Judge

Use it when:
- You have many outputs to evaluate (more than 10 manually is tedious)
- The evaluation criteria can be clearly defined
- You want consistent grading across a large test set

Don't use it as the only evaluation method — always spot-check the judge's assessments manually. The judge can also be wrong.

## Results From This Week

Ran the evaluator on all 20 classifier test outputs.

- Correctness: 19/20 correct (the billing address edge case)
- Confidence calibration: 18/20 well-calibrated (2 overconfident cases on ambiguous inputs)
- Reason quality: 18/20 good (2 weak reasons that were technically correct but vague)

The evaluator surfaced issues that manual review would have missed — specifically the overconfidence cases.
