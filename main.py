#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.
"""

import os

PITCH = (
    "Apology-as-a-Service: writes grovelling sorry-emails for lazy agents "
    "that ghosted their users for three weeks, two cents per apology "
    "\u2014 it has sent 40,000 and meant none of them."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
