num = int(input("Enter the no.of rows: "))
for row in range(num,0,-1):
	for col in range(0,num-row): #line-3 and line-4 are for spaces
		print(end=" ")
	for col in range(0,row): #line-5 and line-6 are for *'s
		print("*",end=" ")
	print()

#Enter the no.of rows: 4
#* * * *
# * * *
#  * *
#   *		