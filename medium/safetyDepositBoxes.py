#safety deposit box
items = input()
goal = input()

items = items.split(",")

i = 0
for i in range(len(items)):
    if items[i] == goal:
        index = i + 1
    i += 1

print(index * 5)
