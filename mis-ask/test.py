
bit_raw = ''

for i in range(0,109740//31):
    bit_raw += input().rstrip()
    for j in range(0,30):
        input()

print(bit_raw)

offset = '000000000000000000000000000000000000000000000000001010101010101010101010101010101011100101'
itr = len(offset)
flag = ''

while itr < len(bit_raw):
    flag += chr(int(bit_raw[itr:itr+8],2))
    print(flag)
    itr+=8