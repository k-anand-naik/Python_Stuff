#Write a program to filter a list of numbers which are divisible by 5

L = [5,10,25,6,7,45,67,35,6,78]
a = filter(lambda a: a%5 == 0, L)
print(list(a))