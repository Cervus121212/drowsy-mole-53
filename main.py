# Everyday Things, Two Lines, Longer Run — make.fun entry.
# A two-line analogy: a vacuum cleaner as a hungry elephant trunk,
# plus why the analogy works.
# Output is exactly two lines, UTF-8, with no trailing newline.

import os
import sys

FIRST_LINE = "A vacuum cleaner is a hungry elephant trunk that slurps dust and crumbs off the floor and swallows them into its belly."
SECOND_LINE = "It works because the hose really does suck things up like a trunk and store them in a bag like a belly, but it leaves out that an elephant chooses what to eat, while the vacuum swallows your sock and anything else lying on the floor."


def build_entry():
    return FIRST_LINE + "\n" + SECOND_LINE


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    text = build_entry()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        print("verification failed: entry.txt bytes differ", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
