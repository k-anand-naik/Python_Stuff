#super() method is used to access the method of a super class in the derived class

class Person:
	country = "India"
	
	def takeBreath(self):
		print("I am breathing....")  #upto this parant class
	
class Employee(Person):
	company = "Honda"
	
	def getSalary(self):
		print(f"Salary is {self.salary}")
	def takeBreath(self):
		super().takeBreath()     #super() method prints Person class takeBreath()
		print("I am an Employee so iam luckily breathing....")  #from line 9 to line 15 child class 1
		
class Programmer(Employee):
	company = "Fiverr"
	
	def getSalary(self):
		print(f"No salary to Programmer")
	def takeBreath(self):
		super().takeBreath()
		print("I am an Programmer so i am breathing+++...")
		
p = Person()
p.takeBreath()
print()

e = Employee()
e.takeBreath()
print()

pr = Programmer()
pr.takeBreath()
print()

#print(p.company) #throws an error
print(p.country)
print(e.company)
print(pr.company)			

#               Output

#I am breathing....

#I am breathing....
#I am an Employee so iam luckily breathing....

#I am breathing....
#I am an Employee so iam luckily breathing....
#I am an Programmer so i am breathing+++...

#India
#Honda
#Fiverr																																																																																																																																																																																																																																																																																																																										