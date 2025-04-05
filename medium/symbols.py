#symbols
str = input()

sen = ""

i = 0
for i in range(len(str)):
    if str[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ':
        sen = sen + str[i]
    i += 1

print(sen)
