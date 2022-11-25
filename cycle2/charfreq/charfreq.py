def charfreq(s):
    d = {}
    for c in s:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1
    print(d)

s = input("Enter the string : ")
charfreq(s)