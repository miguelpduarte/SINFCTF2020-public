# PwnTemplate (Pwn)

## Summary (solution)

This is a template / test to deploy the stuffs

### Tree explanation (and documentation for myself tbh)

* `private` has stuff that will be in the challenge server (not super necessary for this repo I guess, but is a good layout to keep for when organizing the CTFs themselves)
* `public` has binary and information that will be given to the participants via the CTF platform (a binary for local testing, etc)
* `solution` has a solution via pwntools or something, along with whatever else is necessary

#### Inside `private`

* binary for the server
* libc used to compile
* debug version of the binary (maybe)

#### Inside `public`

* binary for CTFd
* source code for really easy / really hard challenges

#### Inside `solution`

* `solve.py` or similar

## How to run (Preferably dockerize all the things)

Dockerized

## Inspired by

https://github.com/justcatthefish/justctf-2019/tree/master/challenges/pwn_atm

## Related resources

https://github.com/justcatthefish/justctf-2019/tree/master/challenges/pwn_atm
