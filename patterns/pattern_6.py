num = int(input("Enter the no.of rows: "))
for i in range(num):
	for j in range(num-i):
		print("*",end=" ")
	print()	

#Enter the no.of rows: 4
#* * * *
#* * *
#* *
#*		