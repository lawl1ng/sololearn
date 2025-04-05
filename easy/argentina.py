#Argentine
# 4000 * .02 = 80
# 80 < 100 so pay in pesos

pesos = int(input())
dollars = int(input())

if pesos * 0.02 < dollars:
    print('Pesos')
else:
    print('Dollars')
