#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- an alien tourist's review of planet Earth --
to /output/entry.txt. Pure Python standard library.
"""

import os

ENTRY = (
    "Came for the oceans, stayed for the tiny screaming hairless apes "
    "who worship glowing rectangles. Four stars \u2014 would abduct again."
)


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-whitespace text.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
