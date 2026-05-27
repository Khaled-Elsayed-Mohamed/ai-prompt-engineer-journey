"""
classifier.py
=============
Week 4 Portfolio Project #1 — Customer Message Classifier

Classifies incoming customer support messages into one of six categories:
    billing | technical_support | account | sales | complaint | other

Returns a JSON object with the category, confidence level, and one-sentence reason.

Usage:
    # Classify a single message
    python classifier.py "I can't log in to my account"

    # Read from stdin
    echo "You charged me twice" | python classifier.py

    # Return only the category string (useful for scripting)
    python classifier.py --category-only "I want to cancel my subscription"

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
# Haiku is ideal for classification — fast, cheap, and accurate on focused tasks.
# The task doesn't require the reasoning depth of Sonnet or Opus.
MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 256  # Classification output is short; this ceiling is generous

# ── System Prompt ─────────────────────────────────────────────────────────────
# v2 — Fixed disambiguation between billing and account for subscription cancellation.
# Also expanded account category to include data migration and subscription management.
SYSTEM_PROMPT = """You are a customer support routing system for a SaaS company.

Classify the following customer message into exactly one of these categories:

- billing: payment issues, unexpected charges, refund requests, invoice questions
- technical_support: bugs, errors, crashes, features not working, performance issues
- account: login problems, password reset, access issues, subscription management,
           plan cancellation, data export or transfer, account settings
- sales: pricing questions, upgrade requests, feature comparisons, new user inquiries
- complaint: dissatisfaction with service, bad experience, escalation requests
- other: anything that clearly doesn't fit the above

Important distinction:
- Subscription CANCELLATION → account (it's a plan change, not a money issue)
- Billing DISPUTE about a charge → billing (money already moved incorrectly)

Return a JSON object:
{
  "category": "one of the six categories above",
  "confidence": "high | medium | low",
  "reason": "one sentence explaining the classification"
}"""

# ── Client ────────────────────────────────────────────────────────────────────
def get_client() -> anthropic.Anthropic:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set.", file=sys.stderr)
        print("Run: export ANTHROPIC_API_KEY='sk-ant-...'", file=sys.stderr)
        sys.exit(1)
    return anthropic.Anthropic(api_key=api_key)


# ── Classifier ────────────────────────────────────────────────────────────────
def classify_message(client: anthropic.Anthropic, message_text: str) -> dict:
    """
    Classify a customer message and return a dict with category, confidence, reason.
    Raises ValueError if the model returns invalid JSON.
    """
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": message_text},
            # Prefill with "{" to force JSON output from the first token.
            # This prevents the model from adding explanation before the JSON.
            {"role": "assistant", "content": "{"},
        ]
    )

    # Re-attach the opening brace used as prefill
    raw_json = "{" + response.content[0].text

    try:
        return json.loads(raw_json)
    except json.JSONDecodeError as e:
        raise ValueError(f"Model returned invalid JSON: {e}\nRaw output: {raw_json!r}") from e


# ── CLI ───────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Classify a customer support message into a routing category."
    )
    parser.add_argument(
        "message",
        nargs="?",
        help="The customer message to classify. Reads from stdin if not provided."
    )
    parser.add_argument(
        "--category-only",
        action="store_true",
        help="Print only the category string (useful for scripting/piping)."
    )
    args = parser.parse_args()

    # Get the message text
    if args.message:
        message_text = args.message
    else:
        message_text = sys.stdin.read().strip()

    if not message_text:
        print("Error: no message provided.", file=sys.stderr)
        sys.exit(1)

    # Run the classifier
    client = get_client()
    try:
        result = classify_message(client, message_text)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Output
    if args.category_only:
        print(result["category"])
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
