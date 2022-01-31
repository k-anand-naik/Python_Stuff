#problem 1
#write a program to print multiplication table of a given number using for loop
num = int(input("Enter the number: "))
for i in range(1,11,1): #(star,end,step_size) the step_size must not be 0
	#print(str(num)+"X"+str(i)+"="+str(i*num))
#             or f"strings"
	print(f"{num}*{i}={num*i}")	