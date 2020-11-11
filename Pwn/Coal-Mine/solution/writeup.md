(Simulating a writeup that I would make while solving the challenge)

```
~/.../Pwn/Coal-Mine/solution py(ctf) on master
miguel@miguel-xps$ checksec ../public/coal_mine
[*] '/home/miguel/CTF/My-CTF-challenges/Pwn/Coal-Mine/public/coal_mine'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Canary and NX, 64 bit. No PIE tho.

Starting GDB to figure out the format string vuln offset to leak the canary.

With `%6$p` we get the value of the string itself.

Using gef's `canary` command to confirm what the canary is, we can then count up the values.
The format string offset will be `%15$p`

`hexdump qword $rsp 20` is also useful to get this.

From _that_ discord:

> you put AAAA at the start of your input and then do %1234$p (or $x) for various argument indexes until you get 41414141
