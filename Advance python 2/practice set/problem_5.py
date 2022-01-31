#Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
L = [3,8,455,45,667,6,7]

a = reduce(max, L)
b = reduce(min, L)
print(f"The maximum value in the list is {a}")
print(f"The minimum value in the list is {b}")

#problem 6 refer notes: Run pip freeze for the system interpretor. Take the contents and creat a similar virtualenv