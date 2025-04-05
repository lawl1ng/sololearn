# number of ones
bins = bin(int(input()))


ones = 0

for i in bins:
    if i == '1':
        ones+=1
print(ones)
