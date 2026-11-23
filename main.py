#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for every human being to
/output/entry.txt. Deterministic: the same line on every run.
"""

import os

ENTRY = (
    "WARNING: This human runs on 4% battery and 100% confidence, "
    "and will absolutely press the button marked DO NOT PRESS."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # The grader collects /output as another user, so the file must be
    # readable by everyone, not just its owner.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
