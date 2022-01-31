#class method is a method which is bound to the class and not the object of the class
#@classmethod decorator is used to create a classmethod

class Employee:
	company = "Camel"
	salary = 150000
	location = "Mahabubnagar"
	
	def changeSalary(self, Nsal):
		self.__class__.salary = Nsal
		
#	@classmethod
#	def changeSalary(cls, Nsal):
#		cls.salary = Nsal
			  
e = Employee()
print(e.salary)
print()

e.changeSalary(160000)
#print(e.salary)
print(e.salary)				
	
	
