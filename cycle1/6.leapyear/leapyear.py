y = int(input("Enter the final year: "))
leap_years = []

for i in range(2022, y):
    if (i % 400 == 0 ) or ((i % 4 == 0) and (i % 100 != 0)):
        leap_years.append(i)

for years in leap_years:
    print(years)