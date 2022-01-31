class Employee:
	company = "Google"
	salary = 100000

harry = Employee()
rajath = Employee()

#creating instance attribute salary for both the objects
harry.salary = 200000
rajath.salary = 300000
print(harry.salary)
print(rajath.salary)
#print(Employee.salary)
#print(harry.address) # error Employee' object has no attribute 'address'
				