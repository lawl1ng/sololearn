#no numerals
sen = input().split(" ")

d = {"0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"}

i = 0
for i in range(len(sen)):
    if len(sen[i]) == 1:
        for number, word in d.items():
            sen[i] = sen[i].replace(number, word)
    elif sen[i] == "10":
        sen[i] = sen[i].replace("10", "ten")
    i += 1
 
print(" ".join(sen))

