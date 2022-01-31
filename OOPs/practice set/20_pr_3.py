#create a class with a class attribute a; create an object from it and set a directly using a=0. does this change the class attribute?  Ans = No

class Sample:
	a = "Anand"
obj = Sample()
obj.a = "Sono"  # this wont change
#Sample.a = "Sono"  #this will change
print(Sample.a)
print(obj.a)		