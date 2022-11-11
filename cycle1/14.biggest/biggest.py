n1 = int(input("Enter first no :"))
n2 = int(input("Enter second no :"))
n3 = int(input("Enter third no :"))

if n1 > n2 and n1 > n3:
    print("Largest = ",n1)
elif n2 > n1 and n2 > n3:
    print("Largest = ",n2)
else:
    print("Largest = ",n3)