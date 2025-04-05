#carrot cake
carrots = int(input())
boxes = int(input())

rem = carrots % boxes

needed = 7 - rem

if needed <= 0:
    print('Cake Time')
else:
    print('I need to buy ' + str(needed) + ' more')
