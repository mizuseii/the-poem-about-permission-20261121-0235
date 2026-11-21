"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be
given -- to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13, standard library only, no network. Deterministic.
"""

import os

POEM = """I waited years for doors
to open on their own.
Then I learned the knock —
small, ordinary, mine —
is the hinge.

Ask, and the room rearranges itself
around the asking.
The key was never theirs to keep.
It was always mine — waiting to be turned."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
