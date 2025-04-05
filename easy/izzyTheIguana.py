#izzy
snacks = input()
snacks = snacks.split(" ")

result = 0
i = 0

while i <= (len(snacks) - 1):
    if snacks[i] == 'Lettuce':
        result += 5
    elif snacks[i] == 'Carrot':
        result += 4
    elif snacks[i] == 'Mango':
        result += 9
    else:
        result += 0
    i += 1
    
if result < 10:
    print("Time to wait")
else:
    print("Come on Down!")
