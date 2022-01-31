num = int(input("Enter the no of rows: "))

for row in range(1,num+1):
	for col in range(1,row+1):
		print("*",end=" ")
	print()	

for row in range(num-1,0,-1):
	for col in range(1,row+1):
		print("*",end=" ")
	print()	
	
#nEnter the no of rows: 4
#*
#* *
#* * *
#* * * *
#* * *
#* *
#*	
	