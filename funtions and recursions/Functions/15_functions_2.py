def age_func(age):
	new_age = float(age) + 50
	return new_age


age = int(input("Enter your age: "))

print("Enter the age: ",age_func(age))