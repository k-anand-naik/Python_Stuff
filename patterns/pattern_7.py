num = int(input("Enter the no.of rows: "))
k = 1
for i in range(1,num+1): # rows
	for j in range(1,k+1): # colomns
		print("*",end=" ")
	k=k+2
	print()	

#Enter the no.of rows: 4
#*
#* * *
#* * * * *
#* * * * * * *