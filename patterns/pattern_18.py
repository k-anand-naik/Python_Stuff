num = int(input("Enter the no of rows: "))
ch = 65  #65 is the ASCII value of A not a

for row in range(1,num+1):
	for col in range(1,row+1):
		print("{0}{1}".format(chr(ch),chr(ch)),end=" ")
		#print("{0}{1}".format(chr(ch+row),chr(ch+col)),end=" ")
		#print("{0}{1}".format(chr(ch+col),chr(ch+row)),end=" ")
		#print("{0}{1}".format(chr(ch+col),chr(ch+col)),end=" ")
		#print("{0}{1}".format(chr(ch+row),chr(ch+row)),end=" ")
	print()	

for row in range(num-1,0,-1):
	for col in range(0,row):
		print("{0}{1}".format(chr(ch),chr(ch)),end=" ")
		#print("{0}{1}".format(chr(ch+col),chr(ch+row)),end=" ")
		#print("{0}{1}".format(chr(ch+row),chr(ch+col)),end=" ")
		#print("{0}{1}".format(chr(ch+col),chr(ch+col)),end=" ")
		#print("{0}{1}".format(chr(ch+row),chr(ch+row)),end=" ")
	print()
	
#Enter the no of rows: 4
#AA
#AA AA
#AA AA AA
#AA AA AA AA
#AA AA AA
#AA AA
#AA			
