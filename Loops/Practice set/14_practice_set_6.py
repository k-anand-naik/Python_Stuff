#problem 5
#sum of n natural numbers
n = int(input("enter the number N: "))
sum = 0 #starting sum = 0

i = 1 # for loop to run # no need of initilising the value while using the for loop
while i<=n:
	#for i in range(1,n+1)
	sum = sum+(i) #sum of n natural numbers
	#sum = sum+(1*i) #sum of squares of n natural numbers
	#sum = sum+(i*i*i) #sum of cubes of n natural numbers
	i = i+1

print("The sum of the first",n,"Natural numbers is: ", sum)		
