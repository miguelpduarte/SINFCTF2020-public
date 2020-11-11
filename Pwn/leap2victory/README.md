# Leap2Victory (Pwn)

## Description (problem statement)

A friend of mine told me that this program is super unhackable!
I think it's weird they have unused functions though...

## Summary (solution)

This is a simple BOF ret2win. Just overflow the buffer with trash and then overwrite the EIP return value with the address of `win()`.

## Related resources

https://ironstone.gitbook.io/notes/types/stack/ret2win
