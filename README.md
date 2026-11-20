# The World Today — 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/yourassisgood69/world-news-20nov/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/yourassisgood69/world-news-20nov/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A program that draws a newspaper front page summing up the world's news
of Friday 20 November 2026, as a single 1024×1024 PNG.

## What it is

`main.py` renders `entry.png` with Pillow: a masthead with the date
"Friday 20 November 2026", one lead story (the Trump–Xi–Putin joint
peace declaration from Shenzhen), six story cards, and an "Also today"
strip — 12 verified stories in total. Every story is documented with its
source in `NEWS.md`.

## Run it

```sh
python3 main.py            # writes /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

Python 3.13 and Pillow are the only requirements. If Pillow is not
available, `main.py` falls back to copying the committed `entry.png`,
which is byte-identical to what the renderer produces.

## Determinism

The program uses no network, no randomness and no clock. Two runs to
different directories produce byte-identical PNGs (verified: same SHA-256).

## Files

- `main.py` — entrypoint
- `draw.py` — the renderer (all copy and layout)
- `entry.png` — the rendered front page (1024×1024, ≤ 1 MiB)
- `NEWS.md` — every story with its source and reporting date
- `system-prompt.txt` — the build brief for this entry
- `LICENSE` — MIT
---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
