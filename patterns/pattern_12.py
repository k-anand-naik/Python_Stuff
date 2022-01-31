num = int(input("Enter the no of rows: "))

for row in range(num):
	for col in range(row+1):
		print("*",end=" ")
	print()	

#Enter the no of rows: 4
#*
#* *
#* * *
#* * * *