
bit_raw=''

for i in range(0,3650):
    bit_raw+=input().rstrip()
    for j in range(0,30):
        input()
    


bit = ''

itr = 0
while itr < len(bit_raw)-1:
    if bit_raw[itr:itr+2] == '01':
        bit+='0'
    if bit_raw[itr:itr+2] == '10':
        bit+='1'
    itr+=2

print(bit)

itr = 19
flag = ''

while itr < len(bit):
    flag += chr(int(bit[itr:itr+8],2))
    print(flag)
    itr+=8