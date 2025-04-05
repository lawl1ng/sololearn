order = input()
orderl = order.split()

def calc(order_list):
    result = 0
    for i in order_list:
        if i == 'Water':
            result = result + 4
        elif i == 'Nachos' or i == 'Pizza':
            result = result + 6
        elif i == 'Cheeseburger':
            result = result + 10
        else:
            result = result + 5
        #print(i, result)
    result = result + (result*.07)
    return(result)


#print(calc(['Pizza', 'Nachos', 'MJ', 'Water']))
    
print(calc(orderl))


# for i in rangeorderlist
# if i == 'Nachos' or pizza:
# result = result + 6
# elif i == cheeseburger



# want to take each item from the input
# check if it's in the keys of the dictionary
# add the corresponding value to a result
# do this for all items
# if the item isn't in the dictionary, just add a 5 (for a coke)
