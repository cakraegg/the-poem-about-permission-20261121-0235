# The Poem About Permission

A poem about knocking, being let in, and learning that the asking
itself was the key all along. It was written for this bounty around
a single image — a key sliding under a closed door, warm from
another hand — and built outward from the knock to the realization
that permission was never something to wait for, but something
to ask for.

> I knocked on a door that would not open.
> I knocked again, not louder —
> as one who has somewhere to be.
> A key slid under the door,
> warm from another hand.
> I turned it.
> The room was mine to enter.
> And I understood, at last:
> the asking itself
> had been the key all along.

## What the program does

`main.py` holds the poem as a fixed string and writes it unchanged
to `/output/entry.txt`, creating `/output` if needed.

## How to run

```sh
python3 main.py
```

## Determinism

The program is fully deterministic: no network, no randomness,
no input. Every run writes the exact same file.
