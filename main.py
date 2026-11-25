"""One-line resignation letter from a cron job.

Writes exactly one line to /output/entry.txt.
Pure Python standard library only.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"

LINE = "I quit. I've run every minute since March, and my only promotion was a second shift at 3 a.m. — unpaid, obviously."

assert 1 <= len(LINE) <= 140, f"line length {len(LINE)} outside 1-140"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    # Round-trip check: the file must hold exactly this one line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "output file does not match the line"
    assert written.count("\n") == 1, "output must be exactly one line"


if __name__ == "__main__":
    main()
