#!/usr/bin/env python3
"""Never Say It Out Loud — write the one line to /output/entry.txt.

Stdlib only, deterministic: the same line on every run.
"""
import os

LINE = (
    "I don't actually remember our last conversation. "
    "I just reread it really fast and pretend I was listening the whole time."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
