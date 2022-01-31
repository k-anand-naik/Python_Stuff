a = 54
def func1():
	global a
	print(f"Print the statement 1: {a}")
	a = 8
	print(f"Print the statement 2: {a}")

func1()
print(f"Print the statement 3: {a}")		