#missing numbers
def find_missing(lst):
    max = lst[0] 
    for i in lst: 
        if i > max: 
            max = i 
        
    min = lst[0] 
    for i in lst: 
        if i < min: min = i 
        
    list1 = [] 
    for num in range(min + 1, max):
        if num not in lst: 
            list1.append(num)
    return list1

number = int(input())
lst = []
for i in range(number):
    lst.append(int(input()))

res = " ".join(map(str,find_missing(lst)))
print(res)

