# Prompt 06 — Temperature Experiment
**Day 4 · Temperature 0 vs Temperature 1**

## The Prompt
```
You are a creative writing coach. Give me 3 opening lines for a short story 
about a person who discovers an old letter in their attic. Each line should 
have a different emotional tone.
```

## Results

### Temperature 0 — consistent across all 4 runs
Line 1 (identical every run):
> "The envelope was addressed in handwriting I didn't recognize, sealed with wax that had turned the color of old teeth, and it had been waiting in the darkness for exactly forty-three years."

Line 2 (identical every run):
> "I found the letter on a Tuesday afternoon when I was supposed to be throwing things away, not collecting ghosts."

### Temperature 1 — varied across all 5 runs
Sample outputs:
> "If my attic had been organized by anyone other than a pack of forgetful squirrels, I might never have knocked over that box..."

> "I found the letter tucked behind a loose beam while searching for Christmas decorations — my mother's handwriting, young and hopeful, addressed to someone she never became."

> "My fingers froze on the seal the moment I saw the date: 1952, the year everyone in my family refuses to talk about."

## Key Finding
Temperature 0 locked onto one strong answer and repeated it. Temperature 1 explored the full range — including ideas that never appeared at temp 0. For creative tasks, use temperature 1. For accuracy-critical tasks (classification, extraction), use temperature 0.
