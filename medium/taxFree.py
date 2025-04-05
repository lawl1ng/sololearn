#tax free
lst = input().split(',')



free = []
notfree = []
for i in lst:
    if int(i) >= 20:
        free.append(int(i))
    else:
        notfree.append(int(i))

tax = []
for i in notfree:
    tax.append(i * 0.07)

print(sum(free) + sum(notfree) + sum(tax))
