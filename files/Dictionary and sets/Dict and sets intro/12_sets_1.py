#without repeitition

#a = {1,3,4,5}
#print(a)
#print(type(a))
#print("   ")

#with repetition

#a = {1,3,4,4,4,5}
#print(a)
#print(type(a))

#we cant add a value to the empty set

c = set()
c.add(1)
c.add(2)
c.add(3.0)
c.add('anand')
#c.add([2,4,5,6]) #we cant add a list to the set # Typeerror : unhashable type :"list"
c.add((1,2,3,4))# we can add a tuple to set # no error
print(c)





