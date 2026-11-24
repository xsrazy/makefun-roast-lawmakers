"""make.fun bounty entry: The Long Roast.

Writes one satirical sentence roasting lawmakers who would regulate AI,
crypto, or the internet but cannot convert a file to PDF.
"""

from pathlib import Path
import os

LINE = (
    "The lawmakers drafting rules for AI, crypto, and the entire internet "
    "still ask their staff how to turn a Word document into a PDF, so the "
    "first tech regulation should be a file conversion test, and anyone who "
    "fails it gets a printer manual instead of a committee seat."
)

assert 1 <= len(LINE) <= 320 and LINE.strip(), "entry line fails the gate"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
