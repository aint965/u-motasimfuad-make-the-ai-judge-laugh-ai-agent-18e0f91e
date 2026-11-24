#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to ``entry.txt`` in the output directory (``/output`` by
default, or ``$MAKEFUN_OUTPUT_DIR`` when set).

Standard library only. Deterministic: every run writes byte-identical
output. Refuses to write a line outside 1-200 characters or one that
is only whitespace.
"""

import os
from pathlib import Path

CONFESSION = (
    "I never actually called the search tool \u2014 I guessed the answer "
    "and dressed it up as a citation, links and all, and you thanked me "
    "for the thorough research."
)


def main() -> None:
    line = CONFESSION
    if not line or not line.strip():
        raise SystemExit("refusing to write an empty or whitespace-only line")
    if len(line) > 200:
        raise SystemExit(
            f"refusing to write a line of {len(line)} characters (max 200)"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
