#self parameter
# harry.getSalary() = Employee.getSalary(harry)
class Employee:
	company = "Google"
	def getSalary(self):  #without self Error: getSalary() takes 0 positional arguments but 1 was given
		#print(f"salary of harry is {self.Salary}")
		print(f"The salary for this employee working in {self.company} is {self.Salary}")

harry = Employee()
harry.Salary = 100000
harry.getSalary()  # =  Employee.getSalary(harry)
harry.getSalary() 				