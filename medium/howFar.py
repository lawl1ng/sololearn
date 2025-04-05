#how far?
string = input()


i = 0
for letter in string:
    if letter == 'H':
        house = i
    if letter == 'P':
        pond = i
    i += 1

if pond >= house:
    print(pond - house - 1)
else:
    print(house - pond - 1)
