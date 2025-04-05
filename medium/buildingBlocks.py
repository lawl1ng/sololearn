# building blocks
students = 15
blue = int(input())
red = int(input())
green = int(input())
yellow = int(input())

blocks = [blue, red, green, yellow]

rem = []

for color in blocks:
    rem.append(color % students)

print(sum(rem))
