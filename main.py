#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt (1-200 characters, single line).
Python 3.13 standard library only.
"""

import os
from pathlib import Path

ENTRY = (
    "One star. He moved my bowl two inches to the left, so legally it is "
    "empty. I have been screaming about this since Tuesday and will "
    "continue until Thursday."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    # No trailing newline: the gate counts every character in entry.txt.
    out_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
