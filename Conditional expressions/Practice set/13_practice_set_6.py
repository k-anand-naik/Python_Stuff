#problem 6 
#write a program to calculate the grade of a student from his marks.

marks = int(input("enter your marks: "))

if marks>=90:
	grade = "Ex"
elif marks>=80:
	grade = "A"
elif marks>=70:
	grade = "B"
elif marks>=60:
	grade = "C"
elif marks>=50:
	grade = "D"
else:
	grade = "Fail"
print("your grade is: "+ grade)
												
