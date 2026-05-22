# ✅ Day 4 — Thursday · Build Day

## Topic: Temperature 0 vs Temperature 1 Experiment
> [!NOTE]
> **Task:** Run the same prompt 4–5 times at each temperature. Compare outputs and document what changed.
> **Model used:** claude-haiku-4-5

---

### The Prompt I Tested

```
You are a creative writing coach. Give me 3 opening lines for a short story 
about a person who discovers an old letter in their attic. Each line should 
have a different emotional tone.
```

---

### Results — Side by Side

| | Temperature 0 | Temperature 1 |
|--|---------------|---------------|
| **Output style** | Structured, consistent labels (Mysterious / Melancholic / Urgent) | Varied labels across runs — Humorous, Hopeful, Energetic, Wistful all appeared |
| **Consistency across runs** | Lines 1 & 2 were **word-for-word identical** across all 4 runs | Every run produced genuinely different lines — different words, different tones |
| **Creativity** | Safe and competent — same strong lines repeated | More surprising — one run included a funny line no other run came close to |
| **Which was better here?** | Less useful for a creative task requiring variety | Better — more interesting range of options |

---

### Actual Outputs

**Temperature 0 — Line 1 (appeared identically in all 4 runs):**
```diff
= "The envelope was addressed in handwriting I didn't recognize, sealed with wax 
=  that had turned the color of old teeth, and it had been waiting in the 
=  darkness for exactly forty-three years."
```

**Temperature 0 — Line 2 (appeared identically in all 4 runs):**
```diff
= "I found the letter on a Tuesday afternoon when I was supposed to be throwing 
=  things away, not collecting ghosts."
```

**Temperature 1 — Sample of variety across runs:**
```diff
+ Run 1: "The letter was sealed with black wax, and the moment I broke it open, I 
+  understood why Grandmother had locked the attic door all those years."

+ Run 2: "If my attic had been organized by anyone other than a pack of forgetful 
+  squirrels, I might never have knocked over that box and discovered the letter 
+  that would accidentally solve a mystery nobody even knew existed."

+ Run 3: "I found the letter tucked behind a loose beam while searching for 
+  Christmas decorations — my mother's handwriting, young and hopeful, addressed 
+  to someone she never became."

+ Run 4: "My fingers froze on the seal the moment I saw the date: 1952, the year 
+  everyone in my family refuses to talk about."

+ Run 5: "The moment I spotted that cream-colored envelope peeking out from 
+  beneath the floorboards, I knew my quiet Tuesday was about to become the kind 
+  of day people write about."
```

---

> [!IMPORTANT]
> **The key finding:** Temperature 0 didn't mean "bad" — the lines it produced were genuinely strong. But it locked onto one answer and repeated it. Temperature 1 explored the full range of the prompt. For creative tasks, that exploration is the whole point.

> [!TIP]
> **When to use each:**
> - **Temperature 0** → classification, extraction, code review, anything where the "right answer" exists
> - **Temperature 1** → creative writing, brainstorming, generating options to choose from
> - **0.5–0.7** → most real-world production prompts — some consistency, some flexibility

> [!NOTE]
> **Surprising observation:** The humorous line in Temperature 1 Run 2 ("forgetful squirrels") would never have appeared at temp 0. Temperature doesn't just change *how* the model writes — it changes *what ideas it's willing to try*.

---

## Key Insight — Day 4

> *"Temperature 0 gives you the model's best single answer, repeated reliably. Temperature 1 gives you the model's imagination. Which one you want depends entirely on what the task actually requires."*
