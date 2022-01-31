#Reduce applies a rolling computation to sequential pair of elements

from functools import reduce
sum = lambda a,b: a+b
L = [1,2,3,4]
val = reduce(sum, L)
print(val)