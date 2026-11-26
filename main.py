#!/usr/bin/env python3
"""One Line, One Laugh (make.fun).

Writes the entry -- one original one-line joke, kept as a single line
with no trailing newline -- to /output/entry.txt, where the sealed
scorer reads it.
"""

import os

ENTRY = 'I told my smart speaker a joke, and now it only answers in rimshots — turns out even the cloud needs a laugh track.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
