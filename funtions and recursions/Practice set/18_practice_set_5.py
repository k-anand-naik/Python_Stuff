#write a python funtion to print multiplication table of a given number
def table(n):
	print("the multiplication table of",n)
	for i in range(1,11):  
		
	#for i in range(10,0,-1): #reverse order table
		   print(n,"X",i,"=",n*i)
		   
		   
n = int(input("The value of n: "))
print(table(n))			