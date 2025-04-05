#multiples
num = int(input())

list = []
for i in range(num):
    if i % 3 == 0:
        list.append(i)
    elif i % 5 == 0:
        list.append(i)


print(sum(list))
