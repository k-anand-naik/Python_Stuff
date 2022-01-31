num = int(input("Enter the number of rows: "))
for i in range(num):
	for j in range(num-i-1):
		print(end=" ")
	for j in range(i+1):
		print("*",end=" ")
	print()		

#Enter the number of rows: 4
#   *
#  * *
# * * *
#* * * *	
			