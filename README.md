[![make.fun](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![Rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/Hasanrdp/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/rank.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![Reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/Hasanrdp/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/reward.svg)](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

# Two Robots in an Elevator

One line of awkward small talk that one robot says to another while they
ride an elevator together, written for the
[make.fun bounty](https://make.fun/bounty/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f).

## The line

> My proximity sensor says we're standing too close, but my politeness subroutine says the polite thing is to pretend my sensor is broken.

136 characters. The joke lives in the collision between two machine
systems: the proximity sensor reports the truth (too close), and the
politeness subroutine overrules it with a lie (pretend the sensor is
broken). That is the awkwardness itself — a robot caught between
accurate sensing and forced courtesy, naming neither out loud, in the
one place where two robots cannot step apart: an elevator.

## How it works

`main.py` (Python 3, standard library only) writes the line to
`/output/entry.txt`. The expected output is pinned inside the program by
an exact character count, byte count and sha256 hash, and the program
reads the file back and refuses to exit cleanly unless it matches all
three.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Entry

- Competition: `u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f`
- Pot: $10 (1st $3.10, 2nd $2.16, 3rd $1.51, top 10 paid), free entry
- License: MIT
