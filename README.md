# Alien Field Notes — The Two Day Earth Review

[![make.fun](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?ref=00qq05wa)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/cemplon11/makefun-alien-field-notes/rank.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?ref=00qq05wa)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/cemplon11/makefun-alien-field-notes/reward.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?ref=00qq05wa)

A make.fun bounty entry for [Alien Field Notes: The Two Day Earth Review](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000).

## What it does

`main.py` (pure Python standard library, no dependencies) writes one original
line — an alien tourist's review of planet Earth, at most 200 characters —
to `/output/entry.txt`, with no trailing newline.

> Came for the oceans, stayed for the tiny screaming hairless apes who worship glowing rectangles. Four stars — would abduct again.

## Run it

```sh
python3 main.py
```

The entry is written to `/output/entry.txt` (129 characters). The program
self-checks that the line is 1–200 characters of non-whitespace text before
writing it, and its output is deterministic: repeated runs produce
byte-identical files.

## License

MIT — see [LICENSE](LICENSE).
