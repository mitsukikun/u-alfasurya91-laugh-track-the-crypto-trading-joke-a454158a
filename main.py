#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — entry generator.

Writes the competition entry (one crypto/trading joke, under 200 chars)
to /output/entry.txt. No network, no dependencies, stdlib only.
"""

import os
import sys

JOKE = "I bought the dip. The dip bought my rent money."

MAX_CHARS = 200


def main() -> int:
    joke = JOKE.strip()
    if not joke:
        print("error: joke is empty", file=sys.stderr)
        return 1
    if len(joke) > MAX_CHARS:
        print(f"error: joke is {len(joke)} chars, over the {MAX_CHARS} limit", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(joke)
    print(f"wrote {out_path} ({len(joke)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
