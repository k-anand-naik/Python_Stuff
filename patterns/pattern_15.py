num = int(input("Enter the no of rows: "))

for row in range(1,num+1):
	for col in range(1,row+1):
		print(row,end=" ")
	print()	

for row in range(num-1,0,-1):
	for col in range(1,row+1):
		print(row,end=" ")
	print()	
	
#Enter the no of rows: 4
#1
#2 2
#3 3 3
#4 4 4 4
#3 3 3
#2 2
#1	
	