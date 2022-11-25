def longword(l):
    longest = l[0]
    for w in l:
        if len(w) > len(longest):
            longest = w
    print("Longest word is : ", longest)

l = input("Enter the string : ").split()
longword(l)