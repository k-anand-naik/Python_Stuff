num = int(input("Enter the no of rows: "))

for row in range(num):
	for col in range(row+1):
		print("*",end=" ")
	print()	

for row in range(num,0,-1):
	for col in range(1,row+1):
		print("*",end=" ")
	print()	
	
#Enter the no of rows: 4
#*
#* *
#* * *
#* * * *
#* * * *
#* * *
#* *
#*	
