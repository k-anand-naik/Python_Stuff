a = [1, 3, 'anand', 45.7, 27, True]
print(a)
print(a[2])
print(type(a[3]))
print(type(a[2]))
#a[3] = 123
#print(a)
#c = a[0]+a[3]
#print(c)

d = input("enter your name: \n")
print(d +"\nyour item in the list is " , a[1]) # no need of +(though it runs) & need (,) for int, float, True etc
print(d +"\nyour item in the list is "  +a[2]) #no need of (,) & need + . for strings
print(d +"\nyour item in the list is " , a[5])