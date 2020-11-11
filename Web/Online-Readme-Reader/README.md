# Online README Reader (Web)

## Description (problem statement)

There's an online service to simulate reading project READMEs! If you give it a zip file with a `README.txt` file and it will display the file's contents to you!

**Note:** The flag is in `/etc/flag`

## Summary (solution)

Have the README.txt file be a symlink to the flag file to trick PHP into reading it.
