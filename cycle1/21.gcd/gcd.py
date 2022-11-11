n1 = int(input("Enter first no : "))
n2 = int(input("Enter second no : "))

result = min(n1,n2)

while result:
    if (n1 % result == 0) and (n2 % result == 0):
        break
    result -= 1

print("GCD = ", result)
