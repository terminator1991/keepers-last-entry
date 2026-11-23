"""Entry for the make.fun 'Make the AI judge feel curious' bounty.

Writes one short text to /output/entry.txt. The text is a tiny
unresolved log-book mystery, told plainly and left open.
"""

import os

TEXT = (
    "In 1973, a lighthouse keeper on a Welsh island logged the same entry "
    "every night for eleven years: 'Light shown. No ships.' On the last "
    "page, in a different hand: 'One ship. It was waiting for me to stop.' "
    "The log ends there — no date, no name."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    print(f"wrote {path} ({len(TEXT)} chars)")


if __name__ == "__main__":
    main()
