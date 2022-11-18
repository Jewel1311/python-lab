def list_sum(l):
	s = 0
	for e in l:
		s += e
	print("Sum = ",s) 

l = input("Enter the list elements : ").split()
l = [int(x) for x in l]
list_sum(l)
