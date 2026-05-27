#!/bin/bash
# Run this once to commit everything and push to GitHub.
# After running: rm commit-and-push.sh

cd "$(dirname "$0")"

git add -A
git commit -m "Complete bootcamp: Weeks 2-12 content, clean up dates and day structure

- Complete Week 2 (days 5-7): prompt chaining, documentation, reflection
- Week 3: full API fundamentals (7 days + 2 Python scripts)
- Week 4: Portfolio Project #1 — customer message classifier (7 days + prompt.md + classifier.py)
- Week 5: niche selection — internal business tools (7 days)
- Week 6: Portfolio Project #2 — meeting notes processor (notes + prompt + script)
- Week 7: evaluation methodology + LLM-as-judge prompt
- Week 8: capstone project — document Q&A system
- Weeks 9-12: job search phase (topic-based, no day structure)
- README: remove dates from milestones, update progress tracker, add all 3 projects
- Roadmap: replace day-of-week tables with topic sections, remove milestone dates
- Week 1/2 notes: remove date stamps and day-of-week labels"

git push origin main
echo "Done. You can now delete commit-and-push.sh"
