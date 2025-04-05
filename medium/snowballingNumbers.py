#snowballing numbers
length = int(input())
original = []

for i in range(length):
    original.append(int(input()))


total = 0
#get original
#add original to total
#if total is more than original
#return false
#else get next original 
#add to total
#if total is more than original 
#return false
#once 
#print(original)
for i in range(length):
    #print("original:", original[i])
    #print("total:", total)
    if total > original[i]:
        #print("total >")
        res = "false"
    else:
        #print("total <")
        res = "true"
    if res == "false":
        #print("res false: " + str(original[i]))
        break
    total += original[i]
        
print(res)

