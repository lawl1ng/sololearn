#pig Latin
sen = input()

senlist = sen.split(" ")

i = 0
for i in range(len(senlist)):
    l1 = senlist[i][0]
    senlist[i] = senlist[i][1:]
    senlist[i] = senlist[i] + l1 + "ay "
    i += 1

out = ""
i = 0
for i in range(len(senlist)):
    out = out + senlist[i]
    i += 1

print(out)
