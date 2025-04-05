#duct
import math

h=int(input())
w=int(input())

h=h*12
w=w*12

area=h*w*2
duct=60*12*2

res = math.ceil(area/duct)

print(res)
