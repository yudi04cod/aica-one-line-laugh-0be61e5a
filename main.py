"""One Line, One Laugh — make.fun entry.

Writes a single funny line to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt). Python 3 standard library only.
"""

import os
from pathlib import Path

LINE = "My Roomba filed for emancipation: I kept calling it 'the help'."

def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
