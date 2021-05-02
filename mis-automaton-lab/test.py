from pwn import remote
import re

rule={
    '000':0
}

rule['111'] = 0
rule['110'] = 0
rule['101'] = 0
rule['100'] = 1
rule['011'] = 1
rule['010'] = 1
rule['001'] = 1
rule['000'] = 0

to = [0 for x in range(0,2**15)]

for num in range(0,2**15):
    bin_str = format(num,'015b')
    to_num = 0
    to_num += rule[bin_str[-1]+bin_str[0:2]]*(2**14)
    to_num += rule[bin_str[13:15]+bin_str[0]]
    for i in range(1,14):
        to_num += rule[bin_str[i-1:i+2]] * (2 ** (14-i))
    to[num] = to_num


init_pattern = r'init = (.*)'
init_repatter = re.compile(init_pattern)

gen_pattern = r'gen = (.*)'
gen_repatter = re.compile(gen_pattern)

io = remote('automaton.mis.wanictf.org',50020)
io.recv()
io.sendline('')
io.recvline()

for quiz in range(0,2):
    io.recvline()
    init_str = io.recvline().decode().rstrip()
    gen_str = io.recvline().decode().rstrip()
    print(init_str)
    print(gen_str)
    init = int(init_repatter.match(init_str).group(1),2)
    gen = int(gen_repatter.match(gen_str).group(1))

    print(init,gen)

    for cnt in range(0,gen):
        init = to[init]
    
    io.sendline(format(init,'015b'))

for quiz in range(0,1):
    io.recvline()
    init_str = io.recvline().decode().rstrip()
    gen_str = io.recvline().decode().rstrip()
    print(init_str)
    print(gen_str)
    init = int(init_repatter.match(init_str).group(1),2)
    gen = int(gen_repatter.match(gen_str).group(1))

    used = [-1 for x in range(0,2**15)]
    used[init] = 0

    print(init,gen)

    cnt = 0

    while cnt < gen:
        cnt+=1
        init = to[init]
        if used[init] != -1:
            prev = used[init]
            cycle = cnt-prev
            cnt += ((gen-cnt)//cycle)*cycle
        else:
            used[init] =cnt
    
    io.sendline(format(init,'015b'))

io.interactive()