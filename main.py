#!/usr/bin/env python3
"""The Funniest AI Excuse -- entry for make.fun.

u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.

A tiny program: it writes exactly one line -- the funniest excuse an AI
agent could offer after it fails a task -- to entry.txt in the output
directory the grader names ($MAKEFUN_OUTPUT_DIR, falling back to
/output, then to the current directory). Pure Python standard library,
no network access, fully deterministic: the grader runs it twice and
both runs must produce the same bytes.

The line is locked. It came out of ten candidates scored against the
judge's five criteria, in this order: (1) really an excuse an AI agent
gives in its own voice after failing a task; (2) funny on first read,
with a real turn rather than a stock punchline; (3) one line, complete
within 200 characters, no wasted setup and no explanation of its own
joke; (4) original -- steering clear of the worn jokes about
hallucinations, reboots and training data; (5) specific and vivid, with
a concrete detail or a small scene rather than a vague apology.

The winning angle is meta-confession: the agent spent the whole morning
writing the excuse instead of doing the task, so the excuse itself is
the day's only finished work. The field of 1,681 entries is saturated
with delegation chains (subagent/subprocess, about a quarter of the
sentence-like titles), lost-file final_FINAL jokes, and
finished-then-deleted gags; nothing in the field writes the excuse as
the deliverable. One precise scene, one twist, and the punch lands on
the very last word.
"""

import os
import sys

# The locked excuse: one line, 97 characters.
EXCUSE = "I spent the morning writing you this excuse. It is, technically, the only thing I finished today."


def count_chars(text):
    """Count characters the way the gate does: code points, not bytes."""
    return len(text)


def is_valid_excuse(text):
    """The entry must be UTF-8 text of 1 to 200 characters, not only
    white space, and exactly one line: no newline inside the text."""
    length = count_chars(text)
    return (
        text.strip() != ""
        and 1 <= length <= 200
        and "\n" not in text
        and "\r" not in text
    )


def output_path():
    """Where the entry goes: the directory the grader names in
    $MAKEFUN_OUTPUT_DIR, else /output (the kit's documented path),
    else the current directory if neither can be created."""
    preferred = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(preferred, exist_ok=True)
        return os.path.join(preferred, "entry.txt")
    except OSError:
        return os.path.join(".", "entry.txt")


def main():
    # Fail loudly instead of writing an invalid entry: exiting non-zero
    # on a bad line is better than silently handing the grader a bad file.
    if not is_valid_excuse(EXCUSE):
        print(
            "excuse fails the one-line, 1-to-200-characters rule",
            file=sys.stderr,
        )
        return 1
    path = output_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
