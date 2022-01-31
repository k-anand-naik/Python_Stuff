#problem 7
#write a program to find out whetgher a given post is talking about "Anand" or not

#post = input("Enter the post: ")
#if "Anand" in post:
#	find = True
#elif "anand" in post:
#	find = True
#else:
#	find = False
#if (find):
#	print("yes! the post contains the name 'Anand' !")
#else:
#	print("nope! the post does'nt contains the name 'Anand' !")				

#OR

post = input("Enter the post: ")
if "ANAND" in post.upper(): #we should take the upper lettered word here like "ANAND"
	print("yes!")
else:
	print("Nope!")
	

post = input("Enter the post: ")
if "anand" in post.lower(): #we should take the lower lettered word here like "anand"
	print("yes!")
else:
	print("Nope!")						