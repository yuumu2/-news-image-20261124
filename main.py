"""Copy the bytes of entry_image.jpg beside this script to entry.png.

Write the file in the directory given by MAKEFUN_OUTPUT_DIR, or in /output
when the variable is unset. Create the output directory if it does not exist.
"""

import os
import sys
from pathlib import Path


def resolve_directories():
    return (
        Path(__file__).resolve().parent,
        Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")),
    )


def main():
    script_dir, output_dir = resolve_directories()
    try:
        image_bytes = (script_dir / "entry_image.jpg").read_bytes()
    except FileNotFoundError:
        print("Error: entry_image.jpg is missing.", file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.png").write_bytes(image_bytes)


if __name__ == "__main__":
    main()
