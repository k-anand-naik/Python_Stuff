#multiple inheritance (occurs when child class inherits from more than one parent clas)

class freeLancers:
	company = "Fiverr"
	level = 0
	
	def upgradeLevel(self):
		self.level = self.level + 1    #upto this Base 1 (class)
	
class Employee:
	company = "Visa"
	eCode = 120   #from line 8 to line 9 Base 2(class)
					
class Programmer(freeLancers, Employee): #inheriting programmer form freeLancer(base 1) and Employee(base 2)
	name = "Anand"
	salary = "150000"
		
p = Programmer()
p.upgradeLevel()
print(p.company)
print(p.level)
print(p.salary)	