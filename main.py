#!/usr/bin/env python3
"""Entry for make.fun: "The Long Roast: Lawmakers and the File They Cannot Convert".

Writes one satirical sentence (at most 320 characters, per the contest gate)
to /output/entry.txt, with no trailing newline. The sentence sets up the
lawmakers' authority over AI, crypto and the internet, then undercuts it with
the file they cannot convert.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

ROAST = (
    "They write the laws for AI, crypto, and the entire internet, yet their "
    "own tech bill reached the floor as a tilted phone photo of a Word file, "
    "glare and all, because the 'Save as PDF' button has survived three full "
    "terms in office without ever being discovered."
)


def entry_text() -> str:
    """Return the single satirical sentence this entry submits."""
    return ROAST


def check_gate(text: str) -> None:
    """Fail loudly if the text would fail the contest gate.

    The sealed scorer accepts UTF-8 text of 1 to 320 characters that is not
    only white space, and the brief demands one sentence that stands alone.
    """
    if not text.strip():
        raise ValueError("entry text is empty or only white space")
    if not 1 <= len(text) <= 320:
        raise ValueError(f"entry text is {len(text)} characters; gate allows 1 to 320")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry text must be exactly one sentence ending in a period")


def main() -> None:
    text = entry_text()
    check_gate(text)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
