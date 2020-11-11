#!/bin/bash

# default file for pwn challenges
# alternative launch script can be specified via cmd in challenge dockerfile

PORT=${PORT:-1337}
MAX_CONNS_PER_IP=${MAX_CONNS_PER_IP:-0}
# This is for rlimit_as (process virtual memory) - 64MB
PROC_MAX_MEMORY=${PROC_MAX_MEMORY:-64}
# This is for cgroup_mem_max (this is higher than the one above due to the cgroup grouping all the forks afaik) - 64MB
CGROUP_MAX_MEMORY=${CGROUP_MAX_MEMORY:-67108864}
# Process's stack max size (MB)
MAX_STACK_SIZE=${MAX_STACK_SIZE:-6}

MAX_PIDS=${MAX_PIDS:-16}
# 60 seconds
TIME_LIMIT=${TIME_LIMIT:-60}
RLIMIT_CPU=${RLIMIT_CPU:-10}

mkdir /sys/fs/cgroup/{cpu,memory,pids}/NSJAIL
chown -R ctf /sys/fs/cgroup/{cpu,memory,pids}/NSJAIL
runuser -u ctf -- nsjail \
    -Ml --port "$PORT" \
    --user ctf \
    --group ctf \
    --max_conns_per_ip "$MAX_CONNS_PER_IP" \
    -R /lib \
    -R /lib64 \
    -R /bin \
    -R /usr \
    -T /tmp \
    -T /dev -R /dev/urandom -R /dev/null \
    -R /home/ctf/chal:/chal \
    -D /chal \
    --disable_proc \
    --time_limit "$TIME_LIMIT" \
    --rlimit_cpu "$RLIMIT_CPU" \
    --rlimit_as "$PROC_MAX_MEMORY" \
    --rlimit_stack "$MAX_STACK_SIZE" \
    --cgroup_pids_max "$MAX_PIDS" \
    --cgroup_mem_max "$MAX_MEMORY_B" \
    ${VERBOSE:+--verbose} \
    -- "$@"
