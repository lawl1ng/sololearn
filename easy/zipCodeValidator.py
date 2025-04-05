#zipcode
zip = input()

i = 0
if len(zip) == 5:
    for i in range(5):
        if zip[i] in '1234567890':
            i+=1
    if i == 5:
        print('true')
    else:
        print('false')
else:
    print('false')
