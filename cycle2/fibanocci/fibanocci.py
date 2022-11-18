def fibanocci(n):
	a = 1
	i = 0
	while(n > 0):
		print(a)
		b = a
		a = a+i
		i = b
		n -= 1
		 

n = int(input("Enter the number : "))
fibanocci(n)
