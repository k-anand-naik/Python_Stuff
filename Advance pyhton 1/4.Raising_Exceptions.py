#Raising Exceptions
def increment(num):
	try:
		return int(num) + 1
	except:
		raise ValueError("This is not good enter a integer, Anand")	
#num = int(input("Enter the number: "))
#print(increment(num))	
a = increment("w")
print(a)	