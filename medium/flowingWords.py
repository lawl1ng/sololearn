#flowing words
inp = input().split(" ")

for i in range(len(inp) - 1):
    if inp[i][-1] == inp[i+1][0]:
        res = "true"
    else:
        res = "false"
        break

print(res)
