#name buddy
groupNames = input().split(" ")
yourName = input()

groupInitial = []
for name in groupNames:
    groupInitial.append(name[0])

if yourName[0] in groupInitial:
    print("Compare notes")
else:
    print("No such luck")
