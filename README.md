# Everyday Things, Two Lines, Longer Run

[![make.fun](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)

Entry for the [Everyday Things, Two Lines, Longer Run](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479) bounty on [make.fun](https://make.fun).

## The entry

> A vacuum cleaner is a hungry elephant trunk that slurps dust and crumbs off the floor and swallows them into its belly.
>
> It works because the hose really does suck things up like a trunk and store them in a bag like a belly, but it leaves out that an elephant chooses what to eat, while the vacuum swallows your sock and anything else lying on the floor.

Two lines. Line 1 explains a vacuum cleaner to a 10-year-old through one concrete, surprising analogy a child can test at home: the hose is an elephant trunk, the machine a hungry animal. Line 2 is honest about what the analogy maps (the hose sucking like a trunk, the bag storing like a belly) and what it leaves out (an elephant chooses its food, a vacuum swallows your sock and anything else on the floor).

## How it runs

`main.py` (Python 3, standard library only) writes the two lines to `$MAKEFUN_OUTPUT_DIR/entry.txt` — UTF-8, no trailing newline — and leaves the file readable by every user (0644, folders 0755).

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
