#problem 3
#write the code of problem 1 using while(multiplication table)
num = int(input("Enter the number: "))
i = 1 #must be 1 if in range the initial value is 1
while i in range(1,11):
	print(f"{num}*{i}={num*i}")
	i = i+1