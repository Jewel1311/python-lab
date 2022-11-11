l = input("Enter integer list : ").split()
l = [int(x) for x in l]

l1 = [x for x in l if x % 2 !=0]
print(l1)