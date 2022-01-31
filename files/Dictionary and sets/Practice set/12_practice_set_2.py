#problem 1
myDict = {
                    "pankha" : "fan",
                    "dabba" : "box",
                    "vastu" : "thing/item",
                    "isqu" : "love"
}
print("Options are : ", list(myDict.keys()))
# if we enter a wrong word, it show error, in order to avoid error we use myDict.get() funtion

a = input("Enter the hindi word : \n")
#print("The meaning of your hindhi word is: ", myDict[a])
print("The meaning of your hindhi word is: ", myDict.get(a)) #shows None

