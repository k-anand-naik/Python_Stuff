#Store the multiplication table generated in problem in a file named Tables.txt

num = int(input("Enter your number: "))
table = [num*i for i in range(1,11)]
print(table)
with open("Tables.txt", 'a') as f:
	f.write(str(table))
	f.write("\n")