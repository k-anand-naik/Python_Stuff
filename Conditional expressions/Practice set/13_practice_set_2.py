#problem 2
#write a program to find out whether a student is pass or fail, it requires total of 40% and atleast 33% in eachsubject to pass. input user

sub1 = int(input("Enter 1st subject marks: "))
sub2 = int(input("Enter 2nd subject marks: "))
sub3 = int(input("Enter 3rd subject marks: "))
print("  ")
if sub1<33 or sub2<33 or sub3<33:
	print("You are failed due to the less marks in atleast one subject")
elif(sub1+sub2+sub3)/3 <40:
	print("you arre failed due to less marks campared to the total marks required")
else:
	print("Congo! you are passed")	