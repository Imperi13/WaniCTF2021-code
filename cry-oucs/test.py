from pwn import remote
from Crypto.Util.number import bytes_to_long,long_to_bytes
import re

c_pattern = r'ciphertext = (.*)'
c_repatter = re.compile(c_pattern)

plain_pattern = r'plaintext = (.*)'
plain_repatter = re.compile(plain_pattern)

n_pattern = r'n = (.*)'
n_repatter = re.compile(n_pattern)

io = remote('oucs.cry.wanictf.org',50010)


io.sendlineafter('> ','4')
n_query = io.recvline().decode().rstrip()
n_str = n_repatter.match(n_query).group(1)
n = int(n_str,16)

m1 = 1000
#m2 = 11

io.sendlineafter('> ','2')
io.sendlineafter('> ',str(m1))
c1_query = io.recvline().decode().rstrip()
c1_str = c_repatter.match(c1_query).group(1)
c1_num = int(c1_str,16)

io.sendlineafter('> ','1')
#io.sendlineafter('> ',str(m2))
c2_query = io.recvline().decode().rstrip()
c2_str = c_repatter.match(c2_query).group(1)
c2_num = int(c2_str,16)

cdash_num = c1_num * c2_num % n
cdash_str = hex(cdash_num)

io.sendlineafter('> ','3')
io.sendlineafter('> ',cdash_str)
mdash_query = io.recvline().decode().rstrip()
mdash_str = plain_repatter.match(mdash_query).group(1)
mdash_num = int(mdash_str,16)

print(mdash_num)
print(hex(mdash_num))

flag_num = mdash_num-1000
print(long_to_bytes(flag_num))