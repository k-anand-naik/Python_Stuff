i = int(input("Enter the number:"))

while i in range(0,100) and i%2==0:
	print(str(i)+" is: "+"even")
	i = i+1
while i in range(0,100) and i%2!=0:	
	print(str(i)+" is: "+"odd")
	i = i+1	

#else:
	#print(str(i)+" is: "+"even")	
	#i = i+1
	