"""
structured-output.py
====================
Week 3, Day 6 — Two-step prompt chain with structured JSON outputs.

Pipeline:
    Raw email text
        → Step 1: Extract structured data as JSON
        → Step 2: Generate a professional reply using extracted fields

Key techniques:
    - System prompt that enforces JSON-only output
    - Assistant prefill trick ("{"") for near-100% JSON reliability
    - json.loads() with error handling
    - Passing structured data between chain steps

Run:
    export ANTHROPIC_API_KEY="sk-ant-..."
    python structured-output.py
"""

import anthropic
import json
import os

# ── Configuration ─────────────────────────────────────────────────────────────
MODEL = "claude-haiku-4-5-20251001"
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


# ── System Prompts ─────────────────────────────────────────────────────────────
# Keeping system prompts as module-level constants makes them easy to find,
# version, and swap out without touching the logic functions.

EXTRACT_SYSTEM = """You are an email analyst. Extract structured data from emails.

Respond with valid JSON only. No explanation, no markdown, no extra text.

Always return exactly this structure:
{
  "sender_name": "string or null if not mentioned",
  "subject_inferred": "string — what the email is about in 5-10 words",
  "sentiment": "positive | neutral | frustrated | urgent",
  "action_required": true or false,
  "action_description": "string describing what action is needed, or null if none",
  "priority": "low | medium | high"
}"""

REPLY_SYSTEM = """You are a professional email responder.

Given structured information about an email, write a concise professional reply.
- Match the tone: urgent emails → decisive, frustrated emails → empathetic first
- State the next action clearly with a timeframe if action is required
- Keep replies under 120 words
- Write only the reply body, no subject line"""


# ── Step 1: Extract ────────────────────────────────────────────────────────────
def extract_email_data(email_text: str) -> dict:
    """
    Extract structured fields from an email.
    Returns a parsed dict with sender, sentiment, action, and priority fields.
    """
    message = client.messages.create(
        model=MODEL,
        max_tokens=512,
        system=EXTRACT_SYSTEM,
        messages=[
            {"role": "user", "content": email_text},
            # Prefilling with "{" forces the model to begin a JSON object.
            # Combined with the system prompt, this pushes JSON reliability
            # from ~95% to ~99%. The response will be everything AFTER this "{".
            {"role": "assistant", "content": "{"},
        ]
    )

    # Re-attach the opening brace we used as a prefill
    raw_json = "{" + message.content[0].text

    try:
        return json.loads(raw_json)
    except json.JSONDecodeError as e:
        # If parsing fails, log the raw output for debugging instead of crashing
        print(f"[Warning] JSON parsing failed: {e}")
        print(f"[Debug] Raw model output: {raw_json!r}")
        raise


# ── Step 2: Generate Reply ─────────────────────────────────────────────────────
def generate_reply(email_data: dict) -> str:
    """
    Generate a professional email reply based on extracted email data.
    Accepts the dict returned by extract_email_data().
    """
    # Pass structured fields as labelled context instead of re-sending the
    # original email. The model only needs the extracted facts, not the full text.
    context = (
        f"Sender: {email_data['sender_name'] or 'Unknown'}\n"
        f"About: {email_data['subject_inferred']}\n"
        f"Their tone: {email_data['sentiment']}\n"
        f"Action needed: {email_data.get('action_description') or 'None'}\n"
        f"Priority: {email_data['priority']}"
    )

    message = client.messages.create(
        model=MODEL,
        max_tokens=256,
        system=REPLY_SYSTEM,
        messages=[{"role": "user", "content": context}]
    )

    return message.content[0].text


# ── Pipeline ───────────────────────────────────────────────────────────────────
def process_email(email_text: str) -> None:
    """Run the full extract → reply pipeline and print results."""
    print("--- Step 1: Extracting data ---")
    data = extract_email_data(email_text)
    print(json.dumps(data, indent=2))

    print("\n--- Step 2: Generating reply ---")
    reply = generate_reply(data)
    print(reply)


# ── Main ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    sample_email = """
    Hi, I placed an order 3 weeks ago and it still hasn't arrived.
    Order number ORD-7741. I've already emailed twice with no response.
    This is really unacceptable — I need this resolved TODAY.
    """

    print("=== Email Triage Pipeline ===\n")
    process_email(sample_email.strip())
