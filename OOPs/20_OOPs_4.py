class Employee:
	company1 = "Google"  #specific to each class
	company2 = "YouTube" 
harry = Employee()          #object instantiation
rajath = Employee()
#print(harry.company1)
#print(rajath.company2)

Employee.company1 = "twitter"		
Employee.company2 = "Zomato"


print(harry.company1)
print(rajath.company2)