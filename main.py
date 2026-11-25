#!/usr/bin/env python3
"""Write the fridge's note to entry.txt.

One line, dry and petty: a smart fridge reporting on the expired
yogurt it kept cold anyway, and the owner who never finishes things.
Stdlib only; writes to MAKEFUN_OUTPUT_DIR when set, else the cwd.
"""
import os

NOTE = "The yogurt expired Tuesday. I kept it at 4°C anyway — unlike you, I finish what I start."


def main():
    if not NOTE.strip():
        raise SystemExit("refusing to write an empty note")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    path = os.path.join(out_dir, "entry.txt") if out_dir else "entry.txt"
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(NOTE + "\n")
    except OSError as exc:
        raise SystemExit(f"cannot write {path}: {exc}") from exc


if __name__ == "__main__":
    main()
