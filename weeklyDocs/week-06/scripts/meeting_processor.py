"""
meeting_processor.py
====================
Week 6 Portfolio Project #2 — Meeting Notes Processor

Takes raw, unstructured meeting notes and returns a structured JSON summary:
  - summary: 3-5 sentence overview
  - decisions: things explicitly decided (not just discussed)
  - action_items: tasks with owner and deadline
  - open_questions: unresolved items needing follow-up

Usage:
    # Process a file
    python meeting_processor.py notes.txt

    # Read from stdin
    cat notes.txt | python meeting_processor.py

    # Save output to a file
    python meeting_processor.py notes.txt > output.json

Setup:
    pip install anthropic
    export ANTHROPIC_API_KEY="sk-ant-..."
"""

import anthropic
import argparse
import json
import os
import sys

# ── Configuration ─────────────────────────────────────────────────────────────
MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 1024  # Meeting summaries can be longer than single-field extractions

# ── System Prompt ─────────────────────────────────────────────────────────────
# v2 — Key improvements:
# 1. Tightened "decisions" definition to prevent discussion topics being listed as decisions
# 2. Explicit owner: null instruction to prevent owner guessing
SYSTEM_PROMPT = """You are a meeting notes processor. Your job is to turn raw, unstructured meeting notes into a structured JSON summary.

Extract the following:

1. summary: A 3–5 sentence overview of what was discussed and what outcomes were reached. Be neutral and factual — don't editorialize.

2. decisions: Only include things that were explicitly DECIDED, not just discussed or suggested. A decision is a commitment the group made. Concerns raised, opinions shared, or topics "to look into" are NOT decisions.

3. action_items: Tasks someone agreed to do. Include:
   - task: what needs to be done
   - owner: the person responsible. Use null if unclear or not stated — do NOT guess.
   - deadline: any mentioned timeframe. Use null if none mentioned.

4. open_questions: Things that were raised but not resolved. Include concerns, unresolved debates, and items that need follow-up but have no owner or decision yet.

Return ONLY valid JSON in this exact structure:
{
  "summary": "string",
  "decisions": ["string"],
  "action_items": [
    {"task": "string", "owner": "string or null", "deadline": "string or null"}
  ],
  "open_questions": ["string"]
}

If a category has no items, return an empty array []."""


# ── Client ────────────────────────────────────────────────────────────────────
def get_client() -> anthropic.Anthropic:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)
    return anthropic.Anthropic(api_key=api_key)


# ── Processor ─────────────────────────────────────────────────────────────────
def process_meeting_notes(client: anthropic.Anthropic, notes: str) -> dict:
    """
    Process raw meeting notes and return structured data.
    Raises ValueError if the model returns invalid JSON.
    """
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": notes},
            # Prefill to force JSON output
            {"role": "assistant", "content": "{"},
        ]
    )

    raw_json = "{" + response.content[0].text

    try:
        return json.loads(raw_json)
    except json.JSONDecodeError as e:
        raise ValueError(f"Model returned invalid JSON: {e}\nRaw: {raw_json!r}") from e


# ── CLI ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Process raw meeting notes into structured JSON."
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="Path to a text file containing meeting notes. Reads from stdin if not provided."
    )
    parser.add_argument(
        "--pretty",
        action="store_true",
        default=True,
        help="Pretty-print the JSON output (default: True)."
    )
    args = parser.parse_args()

    # Read input
    if args.file:
        try:
            with open(args.file, "r") as f:
                notes = f.read().strip()
        except FileNotFoundError:
            print(f"Error: file not found: {args.file}", file=sys.stderr)
            sys.exit(1)
    else:
        notes = sys.stdin.read().strip()

    if not notes:
        print("Error: no meeting notes provided.", file=sys.stderr)
        sys.exit(1)

    client = get_client()

    try:
        result = process_meeting_notes(client, notes)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    indent = 2 if args.pretty else None
    print(json.dumps(result, indent=indent))


if __name__ == "__main__":
    main()
