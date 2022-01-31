a = {1,3,4,5}
print(a)
print(type(a))
print("   ")

#a.add()
#print("      1.a.add() function")
a.add(12)
#print(a)
#print("  ")
 
#len(a) 
print("      2.len(a) function")
print(len(a)) #it shows 5 because perviously we added 12 
print("  ")

#a.remove(x)
#print("      3.remove(x) function")
#print(a.remove(12))
#print(a)

#or 

b = a.remove(12)
print(a) # it wont print any output, it shows an error Keyerror : 12 # if print(b) it shows : None

#b = a.remove(1)
#print(a)
#print("   ")

#a.pop() #removes the orbitary element and returen the element being removed
#print("       4.a.pop() function")
#print(a.pop())
#print(a)
#print("  ")

#a.clear()
#print("       5.a.clear() function") 
#d = a.clear() #empties the entire set and returns the empty set : set()
#print(a)
#print("   ")
  
#a.union({x,y})
#print("         6.a.union({x,y}) funtction") 
#v = a.union({7,10})
#print(v) # if print(a) it returns ony the original 'a' set = {1,3,4,5}
#print("   ")
 
#a.intersection({x,y})
#print("         7.a.intersection")
#n = a.intersection({3,4})
#print(n)