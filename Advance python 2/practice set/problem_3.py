#A list containing the multiplication table of num. Write a program to convert it to a virtical string of some numbers.


num = int(input("Enter your number: "))
L = [str(i*num) for i in range(1,11)]
#print(L) #prints in a list format
verticalTable = "\n".join(L)
print(verticalTable)