#!/usr/bin/env python3
"""Write a one-line review of the most boring everyday object.

The most boring everyday object: the doorstop. Its entire job is to sit
still and hold one door open, and its reward is getting kicked across the
room every single day.

Deterministic: stdlib only, no network, no randomness, no time. Every run
writes the exact same bytes to entry.txt.
"""

import hashlib
import os
import sys

LINE = (
    "The doorstop: the only employee whose whole job is standing still, "
    "and it still gets kicked across the room every day."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition constraints on the review line."""
    if not line:
        raise ValueError("review line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("review must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"review is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {len(data)} bytes to {path} (sha256 {digest})")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
