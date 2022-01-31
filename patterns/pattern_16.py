num = int(input("Enter the no of rows: "))

for row in range(1,num+1):
	for col in range(row):
		print("{0}{1}{2}".format(row,col,(col+row)),end=" ")
	print()	