#write a program using functions to find the greatest of three numberes

def max(num1,num2,num3):
	if num1>num2:
		if num1>num3:
			return num1
		else:
			return num3
	else:
		if num2>num3:
			return num2
		else:
			return num3
							
num1 = int(input("Enter the value of num1: "))		
num2 = int(input("Enter the value of num2: "))		
num3 = int(input("Enter the value of num3: "))

print("the largest value in",num1,num2,num3,"is",max(num1,num2,num3))						