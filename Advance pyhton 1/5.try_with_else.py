#try with else clause (sometimes we want to print a piece of code when try was successful)

try:
	i = int(input("Enter a number: "))
	c = 1/i
except Exceptions as e:
	print(e)
else:
	print("we were successful")		