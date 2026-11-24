import os

LINES = [
    "A vacuum cleaner is a hungry elephant trunk that slurps dust and crumbs off the floor and swallows them into its belly.",
    "It works because the hose really does suck things up like a trunk and store them in a bag like a belly, but it leaves out that an elephant chooses what to eat, while the vacuum swallows your sock and anything else lying on the floor.",
]


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(LINES))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
