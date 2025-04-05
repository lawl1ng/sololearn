# hex colour code
import math

red = int(input())
blue = int(input())
green = int(input())

hex = '0123456789abcdef'

# 00 - 0f is 1 - 15
# 10 - 1f is 16 - 30
# 20 - 2f is 31 - 45
# f0 - ff is what?
# use groupings?
# find what grouping the number is in
# assign its first value based on that
# then the remainder is equvalent to a value in hex

#print(100 / 15)
#print(100 % 15)
# red is 6 rem 10 so would be group 6,a
# group 6 is 5, so red is 5a
# use floor function

# write a function to calculate the group and the remainder, then store the output in hex. Apply the function to each variable
output = '#'
def findhex(color):
    global output
    group = math.floor(color/16)
    rem = color % 16
    g = hex[group]
    r = hex[rem]
    output = output + g + r

list(map(lambda x: findhex(x), [red, blue, green]))

print(output)

