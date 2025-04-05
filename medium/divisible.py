#divisible
integer = int(input())
divisors = [int(i) for i in input().split(" ")]

res = 0
for i in range(len(divisors)):
    if integer % divisors[i] == 0:
        res += 1

if res == len(divisors):
    print('divisible by all')
else:
    print('not divisible by all')
