# 🔨 Week 6 · Day 2 — Test With 10 Inputs, Document Failures

**AI Prompt Engineer Journey · Khaled**

> **Goal:** Stress-test the v1 prompt with 10 varied inputs. Find out where it breaks.

---

## The 10 Test Inputs

I deliberately chose inputs that would push the prompt in different directions:

| # | Input Type | Description |
|---|-----------|-------------|
| 1 | Clean, structured | Product roadmap meeting, clear speaker labels |
| 2 | Clean, structured | Sprint planning, bullet-point format |
| 3 | Messy, stream-of-consciousness | Sales call debrief, written in a rush |
| 4 | Messy, stream-of-consciousness | Engineering standup, fragments and shorthand |
| 5 | Very short | 3-sentence standup update |
| 6 | Very short | Slack thread summary treated as meeting notes |
| 7 | Non-native English | Notes clearly written by a non-native speaker |
| 8 | Ambiguous decisions | Meeting where things were "leaning toward" but not decided |
| 9 | No clear owner | Action items discussed but no names assigned |
| 10 | Mixed language intent | Some items are ideas, some are decisions, some are tasks |

---

## Results

| # | Summary | Decisions | Action Items | Open Qs | Overall |
|---|---------|-----------|--------------|---------|---------|
| 1 | ✅ | ✅ | ✅ | ✅ | Pass |
| 2 | ✅ | ✅ | ✅ | ✅ | Pass |
| 3 | ✅ | ⚠️ | ✅ | ⚠️ | Partial |
| 4 | ⚠️ | ✅ | ⚠️ | ✅ | Partial |
| 5 | ✅ | ✅ | ✅ | ✅ | Pass |
| 6 | ⚠️ | ✅ | ✅ | ✅ | Partial |
| 7 | ✅ | ✅ | ✅ | ✅ | Pass |
| 8 | ✅ | ❌ | ✅ | ❌ | Fail |
| 9 | ✅ | ✅ | ✅ | ✅ | Pass |
| 10 | ✅ | ⚠️ | ⚠️ | ⚠️ | Partial |

**Score: 5 clean passes, 4 partials, 1 fail out of 10.**

---

## Failure Analysis

### Failure #1 — Input 8: Ambiguous decisions classified as decisions

The notes contained: *"Everyone's leaning toward the new pricing model but we need to check with legal first."*

The prompt returned this as a decision. It isn't — it's an open question with a lean. The distinction matters: if this goes into the decisions list, someone will act on it as if it were settled.

**Root cause:** The prompt says "only include things that were clearly decided" but doesn't define what "clearly decided" means. The model is guessing.

### Failure #2 — Input 3 & 10: Decisions vs open questions boundary

Similar issue — items that were discussed extensively but not concluded ended up in `decisions` because the discussion was vigorous. The model inferred consensus where none existed.

### Failure #3 — Input 4: Summary too literal on fragmented notes

The summary for the engineering standup read like a list of fragments, not a coherent summary. The model was faithfully reflecting the input structure instead of synthesising it.

### Failure #4 — Input 6: Slack thread vs meeting notes

The model included conversational filler in the summary ("John mentioned that...") instead of extracting the substance.

---

## What Needs to Fix

1. Add explicit disambiguation rules for decisions vs open questions
2. Instruct the model to synthesise summaries, not reflect structure
3. Handle the "no conclusion reached" case explicitly

---

## Tomorrow

Build v2 with targeted fixes for each failure.
