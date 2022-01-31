#(x,y) means no of ways you can partition x using parts upto y


def count_partitions(n,m):
		 if n==0:
		 	return 1
		 elif m==0 or n<0:
		 	return 0		 		  
		 else:
		 	return count_partitions(n-m,m) + count_partitions(n,m-1)
		 	
n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))
print("Required no.of partitions: ",count_partitions(n,m))
		  	  				  	  	
		  
