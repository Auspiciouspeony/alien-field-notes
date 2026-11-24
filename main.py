"""alien-field-notes — program/v1 entry.

One fixed one-line review of planet Earth, left by an alien tourist,
written to entry.txt in the output directory. The grader reads exactly
the bytes written: no trailing newline, no second line.

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 -P -s main.py

Deterministic: a single constant string; no randomness, no network,
no clock. Python 3.13, standard library only.
"""

import os
from pathlib import Path

# v1 (tested first): "Five stars. They buy a machine to wake them up,
# then pay extra for a button that lets them ignore it. Would
# oversleep again." 124 chars, deterministic, sha256 345eb616…
#
# Iteration round (v1 -> v2), judged on the brief's criteria in order:
# 1. tourist review / outside view — v1's bare "They" is a weak
# outsider marker; v2's "The locals" names the visited people and is
# the classic tourist-review voice, so the alien's outside view is
# clear in the line itself. 2. the laugh is unchanged: the same single
# snooze-button absurdity, still the alien's angle on an ordinary
# Earth object. 3. originality unchanged: a snooze button is a
# specific mundane detail, not the obvious traffic / gravity / money /
# weather. 4. review format strengthened by "The locals". 5. still
# tight at 130 chars, one joke, punch lands on the last three words.
# Closest challengers rejected: the dishwasher line ("stand watching
# them like television… Would rinse again") — two beats, chores plus
# watching, where the brief wants one clean joke; the school line
# ("lock their young in rooms for twelve years… Would enroll again")
# — "Mine learned to sit still" is a great alien-parent beat, but the
# setup reads as a complaint about Earth rather than a tourist's
# delighted observation; the queue line — familiar shape, weaker laugh.
REVIEW = (
    "Five stars. The locals buy a machine to wake them up, then pay "
    "extra for a button that lets them ignore it. Would oversleep again."
)


def _best_effort_chmod(path: Path, mode: int) -> None:
    """Chmod when the path is ours; never fail the run when it is not.

    In the grader the output directory is mounted by the grader and not
    owned by us, so chmod there raises PermissionError. The entry file
    itself is created by us, so its own chmod still applies.
    """
    try:
        path.chmod(mode)
    except OSError:
        pass


def run(output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    _best_effort_chmod(output_dir, 0o755)
    entry = output_dir / "entry.txt"
    entry.write_text(REVIEW, encoding="utf-8")
    # Outputs are collected by another user than the one running this
    # program, so the file must be world-readable.
    entry.chmod(0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(run(Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))))
