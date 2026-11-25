#!/usr/bin/env python3
"""Midnight Fridge Roast (make.fun).

The program emits exactly one line: a roast of a smart fridge that refuses
to open after midnight, recast as a bar calling last orders. It writes that
line to entry.txt inside the output directory the grader provides, and
nothing else. Standard library only.
"""

import os
import sys

ENTRY = "At midnight my fridge plays the last song: lights up, door locked, and a little voice saying you don't have to go home, but you can't eat here."

LIMIT = 200


def output_dir():
    """Where the entry goes: the grader's env dir, /output, or local out/."""
    given = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if given:
        return given
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "out")


def run():
    text = ENTRY
    if not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > LIMIT:
        print(f"entry is {len(text)} chars, over the {LIMIT} limit", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(run())
