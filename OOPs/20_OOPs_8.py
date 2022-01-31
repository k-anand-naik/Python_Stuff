#StaticMethod   function = method

class Employee:
	company = "Google"
	def getSalary(self, signature):
		print(f"The salary for this employee working in {self.company} is {self.Salary}\n{signature}")
	@staticmethod
	def greet():
		print("Good morning, ma'am ")
			
harry = Employee()
harry.greet()
harry.Salary = 100000
harry.getSalary("Thanks!")	

