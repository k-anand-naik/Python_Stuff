num = int(input("Enter the no of rows: "))
ch = 64  #65 is the ASCII value of A not a

for row in range(1,num+1):
	for col in range(1,row+1):
		print("{0}".format(chr(ch+row)),end=" ")
	print()

for row in range(num-1,0,-1):
	for col in range(1,row+1):
		print("{0}".format(chr(ch+row)),end=" ")
	print()		

#Enter the no of rows: 4
#A
#B B
#C C C
#D D D D
#C C C
#B B
#A		
	