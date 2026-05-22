# Prompt 09 — Article Summariser
**Day 6 · Few-shot prompting**

## The Prompt
```
Summarise the text below in exactly 2 sentences.
First sentence: the main point. Second sentence: the key supporting detail.

Example 1:
Input: "Scientists have discovered that regular exercise improves memory by 
increasing blood flow to the brain. A study of 200 adults showed those who 
exercised 3 times a week scored 30% higher on memory tests. Researchers 
believe even light activity like walking can have a meaningful effect."
Output: Regular exercise significantly improves memory by increasing blood 
flow to the brain. A study found that adults who exercised three times a week 
scored 30% higher on memory tests than those who did not.

Example 2:
Input: "Remote work has become the norm for millions of employees worldwide 
since 2020. Companies report higher productivity but struggle with team 
collaboration. Many are now adopting hybrid models to balance both."
Output: Remote work has become widespread since 2020, with companies 
reporting productivity gains. However, collaboration challenges are pushing 
many organisations toward hybrid working models.

Now do this:
Input: [your article paragraph here]
Output:
```

## Result (tested with McKinsey AI & jobs paragraph)
> "Artificial intelligence is transforming the job market by automating significant portions of work across industries, with knowledge workers facing the biggest impact. A 2024 McKinsey report found that 30% of tasks could be automated with current AI technology, but new roles in AI oversight and human-AI collaboration are emerging to replace some displaced jobs."

## Notes
- Token cost: 384 input tokens — most expensive of the 3 few-shot prompts
- Cost is high because examples are long — always weigh example length vs accuracy gain
- Structure (main point + supporting detail) came directly from the format instruction, not the examples
