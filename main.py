#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one line -- a software patch note for a bug in real life /
human biology, at most 160 characters -- to /output/entry.txt.

The joke: the brain's overnight "replay" feature has a bug that
re-runs your most embarrassing moment whenever you try to sleep.
Specific, recognisable, and stated in dry release-note register
with a made-up version number, exactly as the judge brief asks.
"""

import os
import stat

ENTRY = (
    "v2.4.1: fixed a bug where the brain replayed an embarrassing "
    "moment from 2009 every time the user tried to fall asleep."
)


def main() -> None:
    if len(ENTRY) > 160:
        raise SystemExit(f"entry is {len(ENTRY)} chars, over the 160 cap")
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
