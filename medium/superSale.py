#super sale
import math

purchase = [float(s) for s in input().split(",")]

pnotmax = []
discount = []
diff = []

purchaseMax = max(purchase)

for i in range(len(purchase)):
    if purchase[i] != purchaseMax:
        pnotmax.append(purchase[i])

for i in range(len(pnotmax)):
    discount.append(pnotmax[i] * .3)

for i in range(len(pnotmax)):
    diff.append(pnotmax[i] - discount[i])

diff.append(purchaseMax)

totalwo = sum(purchase)
totalw = math.fsum(diff)

totalwotax = totalwo + (totalwo * .07)
totalwtax = totalw + (totalw * 0.07)

print(math.floor(totalwotax - totalwtax))

