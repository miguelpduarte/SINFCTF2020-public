# Heap of Trouble (Pwn)

## Description (problem statement)

Registering for flag raffles is always a heap of trouble! I've made this program to automate this!

## Summary (solution)

UAF vuln, exploitable using the `strdup` with the same length as the buffer.
