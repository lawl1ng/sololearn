#duty free
import math

euroPrice = [float(euro) for euro in input().split(" ")]

dollarPrice = [(1.1 * euro) for euro in euroPrice]

output = 'On to the terminal'

for dollar in dollarPrice:
    if dollar > 20:
        output = 'Back to the store'

print(output)
