#paint costs
import math

paints = input()
paints = int(paints)

initial = 40
paints = 5 * paints
pretax = initial + paints
post_tax = pretax + (pretax * 0.1)
round = math.ceil(post_tax)
print(round)
