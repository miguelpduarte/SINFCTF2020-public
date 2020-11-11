Once again stolen from DownUnderCTF 2020, see README of `/vendor`

## nsjail-ctf

A base image for making pwn challenges.

To build a challenge, copy your binary and other associated files to `/home/ctf/chal`. The default `nsjail-pwn.sh` script can be configured via docker `ENV` or an alternative script can be provided using `ENV`.

At the end of your Dockerfile, expose the appropriate port using `EXPOSE port_number/TCP`.

### options

Default options are listed below:

```
PORT=1337			# Listening port
MAX_CONNS_PER_IP=16		# Maximum number of connections per IP address
CGROUP_MAX_MEMORY=67108864	# cgroup max memory (bytes)
PROC_MAX_MEMORY=64		# Process max memory (MB)
MAX_STACK_SIZE=6		# Maximum stack size (MB) (maybe unnecessary and can remove later if it is a limit)
MAX_PIDS=16			# Maximum number of processes
TIME_LIMIT=60			# Time before connection is closed
RLIMIT_CPU=10			# Maximum amount of CPU time permitted
VERBOSE (not set by default)	# Run nsjail in verbose mode
```
