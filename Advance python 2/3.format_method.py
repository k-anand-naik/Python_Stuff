#if you want to print argumants randomely use indexing in {}
name = input("Enter the name: ")
Class = input("Enter the Class: ")
type = input("Enter the type: ")

templet = "This is {0} and his {1} class is {2}".format(name, Class, type)
print(templet)