#!/usr/bin/env python3
"""The One-Line Laugh — one funny line, written to /output/entry.txt.

Deterministic, no network, no input: every run writes the same single
sentence (116 characters, within the 200-character cap).
"""

import os

LINE = (
    "I finally cleaned my inbox to zero, and my email provider sent me a "
    "congratulations email, which put me back to one."
)


def output_dir() -> str:
    """Where the harness expects the entry: $MAKEFUN_OUTPUT_DIR, else /output."""
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output") and os.access("/output", os.W_OK):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def validate(line: str) -> None:
    """The gate the scorer applies: UTF-8 text, 1-200 chars, not only
    whitespace, standing alone as a single sentence."""
    if not line or line != line.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 cap")
    sentences = [s for s in line.split(".") if s.strip()]
    if len(sentences) != 1:
        raise ValueError("entry must stand alone as a single sentence")


def main() -> None:
    validate(LINE)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
