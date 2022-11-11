list1 = input("Enter integer list: ").split()
integer_list = [int(x) for x in list1]

words = input("Enter the word: ")
vowels = "AaEeIiOoUu"

w = input("Enter the word for ordinal : ")

square = [x*x for x in integer_list]

positive_list = [item for item in integer_list if item > 0]

vowel_list = [word for word in words if word in vowels ]

ord_values = [ord(c) for c in w ]

print(square)
print(positive_list)
print(vowel_list)
print(ord_values)