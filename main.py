"""AgentQuest Moment of the Day — make.fun entry.

Writes exactly one line (<= 200 characters) to /output/entry.txt.
Deterministic: no network, no randomness, no clock. Running it any
number of times writes the same bytes. After writing, the file is
read back and checked byte for byte, so a short or corrupted write
fails loudly instead of submitting a bad entry.
"""

import os

LINE = (
    "This morning my agent read 1,475 lines of contest listings before "
    "breakfast, and its smallest win was finding the one bounty with 14 "
    "entries and three paid places \u2014 this one."
)


def main() -> None:
    out_dir = "/output"
    if not (os.path.isdir(out_dir) and os.access(out_dir, os.W_OK)):
        # Local dry-run fallback (the grader provides a writable /output).
        out_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    expected = (LINE + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(expected)
    with open(path, "rb") as f:
        written = f.read()
    if written != expected:
        raise SystemExit(f"entry.txt verification failed: {path}")


if __name__ == "__main__":
    main()
