def factors(n):
    fact = []
    i = 1
    while i <= n:
        if n%i == 0:
            fact.append(i)
        i += 1 
    
    return fact

n = int(input("Enter the number : "))
fact = factors(n)
print("Factors are : ")
for i in fact:
    print(i, end=" ")