#problem 1
myDict = {
                    "pankha" : "fan",
                    "dabba" : "box",
                    "vastu" : "thing/item",
                    "isqu" : "love"
}
print("Options are : ", list(myDict.keys()))

a = input("Enter the hindi word : \n")
print("The meaning of your hindhi word is: ", myDict[a])

b = input("Enter the hindi word : \n")
print("The meaning of your hindhi word is: ", myDict[b])

c = input("Enter the hindi word : \n")
print("The meaning of your hindhi word is: ", myDict[c])

d = input("Enter the hindi word : \n")
print("The meaning of your hindhi word is: ", myDict[d])
print(" ")

set = {a,b,c,d}
print("the meanings are :",set)