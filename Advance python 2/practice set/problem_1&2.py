# Problem 1 refer notes:  Create two virtual environments, install few packages in the first onne. How do you create a similar environment in the second one

#Problem 2 :  write a program to input name, marks and phone number of a student and format it using the format funtion like below: "The name if the student is Anand, his marks are 74 and phone number is 9090909090"

name = input("Enter your name: ")
marks = input("Enter your marks: ")
phone = input("Enter your phone number: ")

templete = "The name of the student is {},\nhis marks are {},\nhis phine number is {}"
print(templete.format(name, marks, phone))