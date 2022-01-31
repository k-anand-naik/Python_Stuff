#sum of n natural numbers using iterative method

def sum(n):
	result = 0
	for i in range(n+1):
		result = result+i   #sum n natural numbers
		#result = result+(i*i*i)
		#result = result+(i*i) #sum of squares of n natural numbers
	return result

n = int(input("Enter the number for sum: "))
print("The sum of",n,"non-negative integers is:",sum(n))				