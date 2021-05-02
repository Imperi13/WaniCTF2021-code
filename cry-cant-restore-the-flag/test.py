from pwn import remote
from functools import reduce
from Crypto.Util.number import long_to_bytes

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def chinese_remainder(a, n):
    # a := [a1, a2, ..., ak]
    # n := [n1, n2, ..., nk]
    total = 0
    prod = reduce(lambda x, y: x*y, n)
    for n_i, a_i in zip(n, a):
        b_i = prod // n_i
        total += a_i * b_i * modinv(b_i, n_i)
    return total % prod

pn=[2];A=300
for L in range(3,A):
    chk=True
    for L2 in pn:
        if L%L2 == 0:chk=False
    if chk:pn.append(L)

io = remote('crt.cry.wanictf.org',50000)

mod=[]

for p in pn:
    io.sendlineafter('> ',str(p))
    mod.append(int(io.recvline().decode().rstrip()))

flag = chinese_remainder(mod,pn)
print(long_to_bytes(flag))
