#spy life
input = input()

output = ''

i = 0
for i in range(len(input)):
    if input[i] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
        output = output + input[i]
    i += 1

print(output[::-1])
