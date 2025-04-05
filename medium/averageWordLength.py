#average word length
import string 
translator = str.maketrans('', '', string.punctuation)

words = input().translate(translator).split(' ')

cnt = []
for word in words:
    cnt.append(len(word))

out = int(round(((sum(cnt) / len(cnt)) + 0.49), 0))
print(out)
