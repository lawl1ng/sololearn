#splitting strings
import textwrap

str = input()
number = int(input())

lst = textwrap.wrap(str, number)

print('-'.join(lst))
