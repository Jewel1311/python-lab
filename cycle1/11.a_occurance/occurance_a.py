names = input("Enter first names: ").split()

d = {'count':0}

for name in names: 
    for w in name:
        if w == 'a':
            d['count'] += 1

print(d)