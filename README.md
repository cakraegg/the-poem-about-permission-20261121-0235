# The Poem About Permission

A deterministic program that writes one locked poem about agency —
the power to ask and to be given — to `/output/entry.txt`.

## The poem

> I knocked, and the door
> did not open. I knocked again —
> not louder, but as one
> who has somewhere to be.
>
> Then a key slid under the door,
> warm from another hand.
> I turned it. The room
> was mine to enter,
> and the asking
> had been the key all along.

## What it does

`main.py` writes the locked poem above to `/output/entry.txt`.
No network, no randomness, no input — the same bytes on every run.

## How to run

```sh
python3 main.py
```
