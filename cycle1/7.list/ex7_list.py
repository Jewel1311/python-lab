a = input("Enter the elements").split()
a = list(map(int, a))

b = input("Enter the elements").split()
b = list(map(int, b))

if len(a) == len(b):
    print("List length is equal")
else:
    print("List length not equal")

if sum(a) == sum(b):
    print("Sum is equal ")
else:
    print("Sum not equal")
    
flag = False
for x in a:
    for y in b:
        if x == y:
            flag = True
            
if flag:
    print("Common element exist")
else:
    print("No common element")
