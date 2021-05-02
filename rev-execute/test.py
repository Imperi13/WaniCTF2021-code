
num=[7941081424088616006,7311705455698409823,3560223458505028963,35295634984951667]

flag=b''

for i in range(0,4):
    flag+=num[i].to_bytes(8,byteorder="little")

print(flag)