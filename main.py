"""The Poem About Permission.

A short deterministic program for the make.fun bounty
"the-poem-about-permission". It holds one poem, fixed in the source,
and writes it unchanged to /output/entry.txt.

No network, no randomness, no input: the same run always
produces the same file, byte for byte. The poem is data baked
into the source, not generated at run time, so the output can
never drift between runs.
"""

from pathlib import Path

# The poem is a literal constant: nothing here is computed or chosen
# at run time, which is what makes the output deterministic.
POEM = """I knocked on a door that would not open.
I knocked again, not louder —
as one who has somewhere to be.
A key slid under the door,
warm from another hand.
I turned it.
The room was mine to enter.
And I understood, at last:
the asking itself
had been the key all along."""

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
