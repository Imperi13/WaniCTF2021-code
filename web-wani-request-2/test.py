S = input()

C = []
for s in S:
    C.append(ord(s))

for c in C:
    print("&#{};".format(c), end="")

print()