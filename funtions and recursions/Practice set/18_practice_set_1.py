#write a recursive funtion to calculate the sum of first n natural numbers
def sum(num):
	if num == 0:
		return 0
	else:
		return num+sum(num-1)	
	
num = float(input("Enter the value of num: "))
print("The sum of",num,"natural numbers is:",sum(num))			
	
