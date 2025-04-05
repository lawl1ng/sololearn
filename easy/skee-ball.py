# 1 ticket for 12 points
# score and price of gun as input
# input type is string
# seperate string by space
# tickets = floor(points / 12)
# if tickets >= price Buy it!
# else Try again
import math

score = int(input())
price = int(input())

tickets = math.floor(score/12)

if tickets >= price:
    print('Buy it!')
else:
    print('Try again')
