#map applies a function to all items in an input-list
def square(num):
	return num*num
L = [2,4,6]

#Method-1
L2 = []
for item in L:
	L2.append(square(item))
print(L2)

#Method-2
print(list(map(square, L)))		
			
	