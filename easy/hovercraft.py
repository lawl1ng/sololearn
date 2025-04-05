#hovercraft
sales = int(input())
hc = 10
cost = hc * 2 + 1
sell = sales * 3


if sell < cost:
    print('Loss')
elif sell > cost:
    print('Profit')
else:
    print('Broke Even')
