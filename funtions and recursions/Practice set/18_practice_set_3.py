#write a python program to convert inches to centimeters

def cm(inchs):
	return inchs*2.54

inchs = float(input("enter the number: "))
print(inchs,"inchs =",cm(inchs),"cm")

# enter the number: 10
#10 inchs = 25.4 cm	 	