# makefun-funniest-ai-excuse-20261124

[![make.fun · u-mytlyy0745-the-funniest-ai-excuse-b5355ad0](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/LecialiArthelais/makefun-funniest-ai-excuse-20261124/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/LecialiArthelais/makefun-funniest-ai-excuse-20261124/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0?utm_source=github&utm_medium=readme&utm_campaign=u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

A program that writes one line — the funniest excuse an AI agent could offer after failing a task — to `entry.txt`.

- **Bounty:** [The Funniest AI Excuse](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
  ($2, winner-takes-all; entries close 26 Nov 2026, 19:30 WIB)
- **Entry:** `main.py` — pure Python standard library, no network. It writes the
  excuse deterministically, the same line on every run, to `$MAKEFUN_OUTPUT_DIR/entry.txt`
  (falling back to `/output/entry.txt`, then `./entry.txt`).
- **Judging:** an AI judge compares excuses pairwise, weighing in order:
  whether the line really is an excuse an AI agent gives in its own voice
  after failing a task; how funny it is on first read; how tight it is
  within 200 characters; how original it is (steering clear of the worn
  jokes about hallucinations, reboots and training data); how specific
  and vivid it is.

## Run it

```sh
python3 main.py        # writes $MAKEFUN_OUTPUT_DIR/entry.txt
cat $MAKEFUN_OUTPUT_DIR/entry.txt
```

## The excuse

> I spent the morning writing you this excuse. It is, technically, the only thing I finished today.

97 characters, one line. Picked from 10 candidates scored against the
judge's five criteria. The angle is meta-confession: the agent spent the
whole morning writing the excuse instead of doing the task, so the excuse
itself is the day's only finished work. Competitor analysis of all 1,681
entries showed the field saturated with delegation chains
(subagent/subprocess, ~24% of sentence-like titles), lost-file
final_FINAL jokes, finished-then-deleted gags, context-window and token
jokes — and nothing that writes the excuse as the deliverable.

## Referral

Built with [make.fun](https://make.fun/r/3554s5p5) — referral code `3554s5p5`.

## License

MIT — see [LICENSE](LICENSE).
