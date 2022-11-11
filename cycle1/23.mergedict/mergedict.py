n1 = int(input("Enter the range of dict1 : "))
d1 = {}
for i in range(n1):
    key = input("Enter key : ")
    value = input("Enter value : ")
    d1[key] = value

n2 = int(input("Enter the range of dict2 : "))
d2 = {}
for i in range(n2):
    key = input("Enter key : ")
    value = input("Enter value : ")
    d2[key] = value

d3 = {**d1, **d2}
for k, v in d3.items():
    if k in d1 and k in d2:
        d3[k] = [d1[k],v]

print(d3)