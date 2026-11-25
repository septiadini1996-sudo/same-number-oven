#!/usr/bin/env python3
"""Worst AI Advice: one line of terrible advice, written to /output/entry.txt."""

import os

ADVICE = (
    "For best results, set the oven to 350°C whenever a recipe says 350°F "
    "— it's the same number, so dinner cooks in half the time."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ADVICE)


if __name__ == "__main__":
    main()
