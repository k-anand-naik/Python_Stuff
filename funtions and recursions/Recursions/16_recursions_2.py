#The no.of unique paths from top left to bottom right and moves right and next down are:--

def grid_paths(row,col):
	if row == 1 or col==1:
		return 1
	else:
		return grid_paths(row,col-1) + grid_paths(row-1,col)

row = int(input("Enter the no.of rows: "))
col = int(input("Enter the no.of colomns: "))
print()
print("The no.of unique paths from top left to bottom right \nand moves right and next down are:-- ",grid_paths(row,col))						