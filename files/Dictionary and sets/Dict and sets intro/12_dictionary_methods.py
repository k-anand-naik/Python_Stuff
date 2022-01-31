myDict = { 
                     "fast" : "in a quick manner" ,
                     "anand" : "a student",
                     "marks": [1,2,4,5],
                      
                      "tuple" : (1,2,3,4,),                                
                      "newDict" : {'nani' : 'sono'}   #newDict should be at the last    
}

#a.key() funtion
print("           a.key() funtions")
print(myDict.keys())
print(type(myDict.keys()))
print(list(myDict.keys()))
print(tuple(myDict.keys()))

print("   ")
#a.values() funtion
print("           a.values() funtion")
print(myDict.values())
print(type(myDict.values()))
print(list(myDict.values()))
print(tuple(myDict.values()))
print("  ")

#a.items() funtion
print("           a.items() funtion")
print(myDict.items())
print("   ")
print(list(myDict.items()))
print(tuple(myDict.items()))
print("  ")

#a.update({"key": "values") funtion
updateDict = {"kya?":"what?"}
myDict.update(updateDict)
print(myDict)

updateDict1 = {"kaha?":"where?"}
myDict.update(updateDict1)
print(myDict)

#important difference between  dict.get(x) and dict[x]
print(myDict.get("anand")) #prints the value of specific key

print(myDict["anand"]) # also prints the values of specific key
 
print("  ")
#what if we enter a wrong key in the code for output
print(myDict.get("naik")) # shows output as None

print(myDict["naik"]) #show output as Keyerror : 'naik' 

