#balconies
in1 = input().split(",")
in2 = input().split(",")
l1,w1 = int(in1[0]),int(in1[1])
l2,w2 = int(in2[0]),int(in2[1])

a = l1 * w1
b = l2 * w2

if a > b:
    print("Apartment A")
else:
    print("Apartment B")
