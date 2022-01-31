#Single inheritance (inheritance a way of creating a new class from an existing class)

class Employee:
	company = "Google"
	lan = "java"
	
	def showDetails(self):
		print("This is an Employee")   #upto this base class
	
class Programmer(Employee):
	#language = "Python"
	company = "YouTube"
	def getLanguage(self):
		print(f"The language is {self.language}")
	
	def showDetails(self):
		print("This is an Programmer")         #from line 10 to line 17 child class
										
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)
print(e.company)
print(e.lan)
#print(p.language)
