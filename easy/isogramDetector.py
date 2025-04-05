#isogram detector
word = input()

iso = ""

for i in range(len(word)):
    if word[i] not in iso:
        iso = iso + word[i]

if word == iso:
    print('true')
else:
    print('false')
