num = int(input("Enter the no of rows: "))

for row in range(1,num+1):
	for col in range(row):
		print("{0}{1}{2}".format(row,col,(col+row)),end=" ")
	print()	

for row in range(num-1,0,-1):
	for col in range(row):
		print("{0}{1}{2}".format(row,col,(col+row)),end=" ")
	print()	

#Enter the no of rows: 4
#101
#202 213
#303 314 325
#404 415 426 437
#303 314 325
#202 213
#101