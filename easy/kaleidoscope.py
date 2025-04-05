#kaleidoscope 
k = int(input())

cost = k * 5

if k > 1:
    discount = cost * 0.1
else:
    discount = 0

tax = (cost - discount) * 0.07

total = cost - discount + tax

print(round(total, 2))
