#multi level inheritance (occurs when a child class become a parent class for anpother child class)

class Person:
	country = "India"
	
	def takeBreath(self):
		print("I am breathing....")  #upto this parant class
	
class Employee(Person):
	company = "Honda"
	
	def getSalary(self):
		print(f"Salary is {self.salary}")
	def takeBreath(self):
		print("I am an Employee so iam luckily breathing....")  #from line 9 to line 15 child class 1
		
class Programmer(Employee):
	company = "Fiverr"
	
	def getSalary(self):
		print(f"No salary to Programmer")
	def takeBreath(self):
		print("I am an Programmer so i am breathing+++...")
		
p = Person()
p.takeBreath()

e = Employee()
e.takeBreath()

pr = Programmer()
pr.takeBreath()

#print(p.company) #throws an error
print(p.country)
print(e.company)
print(pr.company)																																																																																																																																																																