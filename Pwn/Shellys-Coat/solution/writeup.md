```
~/.../Pwn/Shellys-Coat/solution py(ctf) on master
miguel@miguel-xps$ checksec ../public/shellcoat
[*] '/home/miguel/CTF/My-CTF-challenges/Pwn/Shellys-Coat/public/shellcoat'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      PIE enabled
    RWX:      Has RWX segments
```

Executable stack and no canary. Shellcode time baby!

For some reason the ESP is getting overwritten with the buffer overflow hmmmmmm

The stack seems weird - is `printf` misaligning stuff?

After all it was probably just wrong padding. Correcting the padding and putting the shellcode on top of the buffer (the bottom was being overwritten) resulted in success!
