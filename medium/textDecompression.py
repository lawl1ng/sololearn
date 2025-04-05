# text decompression
comp = input()

decomp = []
mult = []

for i in comp:
    if i not in "1234567890":
        decomp.append(i)
    else:
        mult.append(i)

res = ""

for i in range(len(decomp)):
    res = res + (decomp[i] * int(mult[i]))

print(res)
