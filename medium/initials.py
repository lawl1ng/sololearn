#initials
number = int(input())
lst = []
for i in range(number):
    lst.append(input())

lst2 = []    
for i in lst:
    a = ''.join([x[0].upper() for x in i.split(' ')])
    lst2.append(a)


print(' '.join(lst2))
