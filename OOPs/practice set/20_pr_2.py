#Write a class Calculator capable of finding square , squareroot and cube of a given number
class Calculator:
	def __init__(self,num):
		self.number = num
	def square(self):
		print(f"The value of {self.number} square is {self.number**2}")
	def squareroot(self):
		print(f"The value of {self.number} square-root is {self.number**0.5}")		
	def cube(self):
		print(f"The value of {self.number} cube is {self.number**3}")
	def cuberoot(self):
		print(f"The value of {self.number} cube-root is {self.number**(1/3)}")
	
   
#a = Calculator(3)
num1 = float(input("Enter the number for your result: "))
a = Calculator(num1)
a.square()
a.squareroot()
a.cube()
a.cuberoot()				