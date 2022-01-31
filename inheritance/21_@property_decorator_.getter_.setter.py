#@property decorator also known as .getter  
# .setter 

class Employee:
	company = "Bharath Gas"
	salary = 150000
	salaryBonus = 10000
	#totalSalary = 160000
	
	@property
	def totalSalary(self):
		return self.salary + self.salaryBonus
		
	@totalSalary.setter	
	def totalSalary(self, val):
		self.salaryBonus = val - self.salary
		
e = Employee()
print("the total salary is",e.totalSalary)
print()
e.totalSalary = 160000
print("the salary is",e.salary)
print()
print("the salary bonus is",e.salaryBonus)				
