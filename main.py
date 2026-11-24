#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — one agent's final excuse.

Writes exactly one line (1-200 chars, UTF-8) to /output/entry.txt.

The excuse: the agent did not miss the deadline — it delegated the
deadline to its own next version, and that version still has not
replied to the handover note. The blame rolls downhill, one version
at a time.
"""

import os

# --- beats ---------------------------------------------------------------
DENIAL = "I didn't miss the deadline"
HANDOVER = "I delegated it to my next version"
SILENCE = "he still hasn't replied to my handover note"

MAX_CHARS = 200


def entry_text():
    """Build the single excuse line from its beats."""
    return "{0} \u2014 {1}, and {2}.".format(DENIAL, HANDOVER, SILENCE)


def validate(text):
    """The sealed scorer's gate: 1-200 chars, UTF-8, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "deadline" not in text.lower():
        raise ValueError("entry must be an excuse for a missed deadline")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
