#try with finally

try:
	i = int(input("Enter a number: "))
	c = 1/i
except Exceptions as e:
	print(e)
	exit()  #eventhough here the program is exit, due to finally: the code inside the finally gets executed
finally:
	print("We are done!") 
print("Thanks for using the program")		