#vowel counter
sen = input()
sen = sen.lower()

res = 0
for i in range(len(sen)):
    if sen[i] in 'aeiou':
        res += 1
        
print(res)
