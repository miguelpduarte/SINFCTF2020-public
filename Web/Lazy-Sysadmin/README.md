# Lazy Sysadmin - Web

## Description (problem statement)

I've heard about a new flag management service that was recently created.
This sysadmin is a bit careless with security, so you might be able to get something!

## Summary (solution)

The MD5 hash is leaked in an HTML comment. By "reversing" the hash and getting the password, you get the flag.

https://hashdecryption.com/decrypt.php (for example)

The original password is `debug`.
