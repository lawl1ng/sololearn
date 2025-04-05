#that's odd
length = int(input())
even = []

for i in range(length):
    element = int(input())
    if element % 2 == 0:
        even.append(element)
        
print(sum(even))
