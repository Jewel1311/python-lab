def ing(l):
    nl = []
    for w in l:
        if w[-3:] == "ing":
            nl.append(w + "ly")
        else:
            nl.append(w + "ing")
        

    print(nl)

l = input("Enter the string : ").split()
ing(l)