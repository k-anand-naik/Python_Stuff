#constructors  __init__()

class Employee:
	company = "Google"
	
	def __init__(self,name,salary,sub_unit):
		self.name = name
		self.salary = salary
		self.sub_unit = sub_unit
		print("*******Employee is created*******")
	
	def getDetails(self):
		print(f"The name of employee is {self.name}")
		print(f"The salary of employee is {self.salary}")
		print(f"The sub_unit of employee is {self.sub_unit}")
	
	def getSalary(self, signature):
		print(f"the salary for this employee working in {self.company} is {self.salary}\n{signature}")
	
	@staticmethod
	def greet():
		print("Good morning!")
	
	@staticmethod
	def time():
		print("The time is 9:00 in the morning!")
																																
harry = Employee("Harry",100000,"YouTube")
harry.getDetails()