text = input("Enter the text: ").split()

d = {}

for word in text:
    if word in d.keys():
        d[word] += 1
    else:
        d[word] = 1

print(d)


