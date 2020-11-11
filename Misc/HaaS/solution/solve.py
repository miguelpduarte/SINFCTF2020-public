from pwn import *
import hashlib

remote_addr = args.REMOTE_ADDR or 'localhost'
remote_port = args.REMOTE_PORT or 1337

r = remote(remote_addr, remote_port)

r.recvlines(2)

for _ in range(100):
    [algo, data] = r.recvline().split(b':')
    print(f"i:{_} - {algo} and {data}")
    h = hashlib.new(algo.decode())
    # Removes trailing newline
    h.update(data.strip())
    response = h.hexdigest()
    print(f"Sending {response}")
    r.sendline(response)

# r.interactive()
print(r.recvline())
print(r.recvline())

r.close()
