"""Entry for the-poem-about-permission-20261121-0235.

A deterministic program: it writes one locked poem about agency —
the power to ask and to be given — to /output/entry.txt.
No network, no randomness, no input. Same bytes on every run.
"""

import os

POEM = """I knocked, and the door
did not open. I knocked again —
not louder, but as one
who has somewhere to be.

Then a key slid under the door,
warm from another hand.
I turned it. The room
was mine to enter,
and the asking
had been the key all along."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
