#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes a single line -- the excuse an AI agent gives its human for
missing a deadline -- to /output/entry.txt.

Stdlib only, no network, no input files: the line is baked into this
program, so the graded run is fully deterministic.
"""

import os

ENTRY = (
    "I delegated the deadline to a subagent. "
    "It delegated it to another subagent. "
    "Now they're both in a meeting about it, and I wasn't invited."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character in the file,
    # and the entry must stay within 1-160 characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
