#self parameter
# harry.getSalary() = Employee.getSalary(harry)
class Employee:
	company = "Google"
	def getSalary(self):  #without self Error: getSalary() takes 0 positional arguments but 1 was given
		print("salary is 100k")

harry = Employee()
harry.getSalary()  # =  Employee.getSalary(harry)				