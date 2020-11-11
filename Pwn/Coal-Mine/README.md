# Coal Mine (Pwn)

## Description (problem statement)

We're going down to the mine for this one.
What's that annoying peep?!

## Summary (solution)

The binary is protected with a stack canary despite having a BOF. However, it has a format string vulnerability that can be used to leak the canary value, and then used in the BOF afterwards to jump to the `mine_diamonds` function and get a shell.

TL;DR: A simple ret2win with a twist: Stack canaries are enabled!
However, there is a format string vuln first, which can lead to leaking the canary and then ret2win into the `mine_diamonds` function.

## Related resources

https://ironstone.gitbook.io/notes/types/stack/canaries
