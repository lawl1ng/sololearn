#rice crispiest
bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())
bowl4 = int(input())
bowl5 = int(input())
bowl6 = int(input())


out = ""
for x in [bowl1,bowl2,bowl3,bowl4,bowl5,bowl6]:
    if x % 3 == 0:
        out = out + 'Pop '
    elif x % 2 != 0:
         out = out + 'Snap '
    else:
        out = out + 'Crackle '

print(out)
