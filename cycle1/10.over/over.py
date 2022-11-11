l = input("Enter the integers : ").split()
l = [int(x) for x in l]
for i in l:
    if i > 100:
        l[l.index(i)] = "over"

for i in l:
    print(i, end=" ")