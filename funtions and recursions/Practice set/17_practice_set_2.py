#write a program using funtion to convert celsius to fahrenhite
def fahr(cel):
	return cel*(9/5)+32

cel = int(input("enter the temperature in celsuis degree: "))
print("The fahrenhite value of",cel,"C is: ",fahr(cel))	 	 