#problem 4
#write a program to find whether a given username containes less than 10 charecters or not

u_name = input("enter your user name: ")
b = len(u_name)
if b<10:
	print("This user name has charecters less than 10")
else:
	print("This user name has characters more than 10")	