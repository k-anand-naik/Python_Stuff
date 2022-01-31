num = int(input("Enter the number of rows: "))
ch = 64
for row in range(1,num+1):
	for col in range(1,row+1):
		ch = ch+1
		print("{0}{1}".format(row,col),end=" ")
	print()

for row in range(num-1,0,-1):
	for col in range(1,row+1):
		ch = ch+1
		print("{0}{1}".format(col,row),end=" ")
	print()

#Enter the number of rows: 5
#11
#21 22
#31 32 33
#41 42 43 44
#51 52 53 54 55
#14 24 34 44
#13 23 33
#12 22
#11		