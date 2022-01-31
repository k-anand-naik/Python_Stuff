#iterative method

#def fact(num):
#	product = 1
#	for i in range(num):
#		product = product * (i+1)
#	return product #return should be for "for" loop
		
#num = int(input("Enter the number for factorial: "))
#print("The factorial of",num,"is:",fact(num))	

#recursive method

def fact(num):
	if num==0 or num==1:
		return num
	else:
		return num*fact(num-1)
	
num = int(input("Enter the number for factorial: "))
print("The factorial of",num,"is:",fact(num))			










