#filter creates a list of items for which the function returns True

def greater_than_5(num):
	if num > 5:
		return True
	else:
		return False

g10 = lambda num: num>10
L = [1,2,3,4,34,55,65,4,78,7,8,90]
print(list(filter(greater_than_5, L)))
print(list(filter(g10, L)))						