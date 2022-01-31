#write a program to print the content of a list using while loop

fruits = ["banana", "mango","kiwi","jamalai"]
i = 0
j = 1
print("the fruits in the list are: ")
while i<len(fruits) and j<5:
	
	print(str(j)+". " + fruits[i])
	i = i+1
	j = j+1
	
	  