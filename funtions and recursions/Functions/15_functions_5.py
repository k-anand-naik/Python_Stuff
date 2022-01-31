
def greet(name):
	print("Good morning! "+name)

def mySum(a,b):
	sum = a+b
	return sum


name = input("Enter name: ")
print(" ")

a = int(input("Enter value of a:"))
b = int(input("Enter value of b: "))
print(" ")
greet(name)
s = mySum(a,b)
print(" ")
print(name,", your required sum is: ",s)						