#write a program to print third, fifth and seventh elements from a list using enumerate function

L =[1,2,3,4,5,6,7,7,8,9,10]
for index, item in enumerate(L):
	if index == 2 or index == 4 or index == 6:
		#print(index, item)
		print(f"The {index + 1}th element is {item}")