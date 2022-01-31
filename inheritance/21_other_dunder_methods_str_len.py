#operators in python can be overloaded using dudnder methods __dunder__

class Number:
	def __init__(self, num1):
		self.num1 = num1
	
	def __add__(self, num2):
		return self.num1 + num2.num1
	
	def __mul__(self, num2):
		return self.num1 * num2.num1
		
	def __sub__(self, num2):
		return self.num1 - num2.num1
		
	def __truediv__(self, num2):
		return self.num1 / num2.num1
		
	def __floordiv__(self, num2):
		return self.num1 // num2.num1
	
	def __str__(self):
		return f"Decimal Number {self.num1}"												
	
	def __len__(self):
		return 2												
													
N1 = Number(int(input("Enter the 1st number:")))
N2 = Number(int(input("Enter the 2st number:")))
print()
sum = N1 + N2
mul = N1*N2
sub = N1-N2
div = N1/N2
mod = N1//N2
print("Lets add")
print(sum)
print()
print("Lets multiply")
print(mul)
print()
print("Lets substract")
print(sub)
print()
print("Lets divide") # ans is 1.1818181818
print(div)
print()
print("Lets module") # and is 1 because 13/11 = 1.18181818 ,here floor dividion give 1 
print(mod)
print()

N = Number(N1)
print(N)
print(len(N))
															