from pwn import *

context.terminal = ['gnome-terminal', '--', 'bash', '-c']
elf = context.binary = ELF('../public/shell_exec')

remote_addr = args.REMOTE_ADDR or 'localhost'
remote_port = args.REMOTE_PORT or 1337

if args.LOCAL:
    r = process()
else:
    r = remote(remote_addr, remote_port)

if args.LOCAL and not args.NO_GDB:
    gdb.attach(r)

r.interactive()

r.close()
