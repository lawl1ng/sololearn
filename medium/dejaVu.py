#deja vu
input = input()

dejavu = ''

i = 0
for i in range(len(input)):
    if input[i] not in dejavu:
        dejavu = dejavu + input[i]
    i += 1

if dejavu == input:
    print('Unique')
else:
    print('Deja Vu')
