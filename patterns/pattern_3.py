num = int(input("Enter the no.of rows: "))
row = 0
while row<num:
	space = num-row-1 # line-4 to line-7 code exicute spaces 
	while space>0:
		print(end=" ")
		space = space-1 #spaces decreasing form top
	star = row+1
	while star>0:
		print("*",end=" ")
		star = star-1
	row = row+1
	print()
	
#Enter the no.of rows: 4
#   *
#  * *
# * * *
#* * * *					