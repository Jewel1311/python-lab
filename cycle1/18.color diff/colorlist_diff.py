c1 = input("Enter colors of list 1 : ").split()
c2 = input("Enter colors of list 2 : ").split()

new_c2 = set(c2)

c3 = [x for x in c1 if x not in new_c2]

for clr in c3:
    print(clr)