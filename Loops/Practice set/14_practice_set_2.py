#problem 2
#write a program to greet the person names stored in a list l1 and which starts with S
l1 = ["Sami","ramulu","ramesh","Shanker","Sai"]
for name in l1:
	if name.startswith("S"):
	#if name.startswith("S") or name.startswith("r"): #and boolean is not working
		print("Hello! " + name)