#sum of n natural numbers using the recursive method

#def sum(n):
#	if n==0:
#		return 0
#	else:
		#return n+sum(n-1)
#		return (n*n)+(sum(n-1))
			
#n = int(input("Enter the number for sum: "))
#print("The sum of",n,"natural numbers is: ",sum(n))

#def square(n):
#	if n==0:
#		return 0
#	else:
#		return (n*n)+(square(n-1))
#			
#n = int(input("Enter the number for sum: "))
#print("The sum of squares of",n,"natural numbers is: ",square(n))

def cube(n):
		if n==0:
			return 0
		else:
			#return n+sum(n-1)
			#return (n*n)+(sum(n-1))
			return (n*n*n)+cube(n-1)
			
n = int(input("Enter the number for sum: "))
print("The sum of cubes of ",n,"natural numbers is: ",cube(n))
