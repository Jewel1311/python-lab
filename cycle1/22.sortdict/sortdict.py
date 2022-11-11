n = int(input("Enter the range of dict : "))
d= {}
for i in range(n):
    key = input("Enter key : ")
    value = input("Enter value : ")
    d[key] = value

print("1. sort by key ")
print("2. sort by value ")
c = int(input("Enter your choice : "))


if c == 1:
    sorted_asc = sorted(d.keys())
    sorted_desc = sorted(d.keys(),reverse=True)
    for key in sorted_asc:
        print(key,':',d[key])
    for key in sorted_desc:
        print(key,':',d[key])

elif c == 2:
    asc = dict(sorted(d.items()))
    desc = dict(sorted(d.items(), reverse = True))
    print(asc)
    print(desc)
else:
    print("invalid choice")

