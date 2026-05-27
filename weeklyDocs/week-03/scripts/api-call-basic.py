"""
api-call-basic.py
=================
Week 3, Day 2 — First working Anthropic API call from Python.

Demonstrates:
- SDK setup and authentication via environment variable
- Basic message creation (single turn)
- Reading the response text and token usage
- What happens when max_tokens is set too low (stop_reason: max_tokens)

Run:
    export ANTHROPIC_API_KEY="sk-ant-..."
    python api-call-basic.py
"""

import anthropic
import os

# ── Configuration ────────────────────────────────────────────────────────────
# Use the cheapest model for experiments — swap to claude-sonnet-4-6
# or claude-opus-4-6 when output quality matters more than cost.
MODEL = "claude-haiku-4-5-20251001"


# ── Client Setup ──────────────────────────────────────────────────────────────
# Always read the API key from the environment. Never hardcode it in source
# files — they end up in git history and can leak credentials.
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


# ── Basic Call ────────────────────────────────────────────────────────────────
def basic_call(prompt: str, max_tokens: int = 256) -> None:
    """Make a single-turn API call and print the response with token usage."""

    message = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,   # hard ceiling — model stops here even mid-sentence
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # message.content is a list of content blocks. For text responses,
    # the text is always at message.content[0].text
    print("Response:")
    print(message.content[0].text)

    # stop_reason tells you WHY the model stopped:
    #   "end_turn"   = finished naturally (what you want)
    #   "max_tokens" = got cut off by the token limit (check your max_tokens setting)
    print(f"\nStop reason: {message.stop_reason}")
    print(f"Tokens used: {message.usage.input_tokens} in / {message.usage.output_tokens} out")


# ── Max Tokens Experiment ──────────────────────────────────────────────────────
def demonstrate_token_cutoff() -> None:
    """Show what happens when max_tokens is set too low."""
    print("\n--- Token cutoff demo (max_tokens=10) ---")
    message = client.messages.create(
        model=MODEL,
        max_tokens=10,  # deliberately too low
        messages=[
            {"role": "user", "content": "Write a short paragraph about prompt engineering."}
        ]
    )
    print(f"Output: {message.content[0].text!r}")  # !r shows the truncation clearly
    print(f"Stop reason: {message.stop_reason}")   # will be "max_tokens"


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Basic API Call Demo ===\n")

    basic_call(
        prompt="Explain what a context window is in one sentence.",
        max_tokens=256
    )

    demonstrate_token_cutoff()
