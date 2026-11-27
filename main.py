#!/usr/bin/env python3
"""news-image-20261126 v5 — copy program.

The front page for Thursday 26 November 2026 (48 stories, 9 regions, 13
pictured stories with numbered map pins) was drawn once, locally, and is
shipped in this repository as entry.png. This program only carries that
file to the grader's output directory. It uses the standard library alone,
touches no network, and writes the same bytes on every run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"shipped image missing: {SOURCE}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
