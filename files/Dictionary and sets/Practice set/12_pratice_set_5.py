#problem 6 
#create an empty dictionary, Allow 4 friends to enter their favourite languages as values and use keys as their names. Assume the names are unique

favLang = {} # empty_dict
a = input("Enter the fav language of swathi: ")
b = input("Enter the fav language of anand: ")
c = input("Enter the fav language of ram: ")
d = input("Enter the fav language of jai: ")

#favLang["swathi"] = a
#favLang["anand"] = b
#favLang["ram"] = c
#favLang["jai"] = d

#print(favLang)
#print(" ")
#print(tuple(favLang)) #here it wont print their names:languages just prints their names
#print(list(favLang)) #here it wont print their names:languages just prints their names
 
#problem 7 , if names of 2 friends are same, what will happen to the program 6?
#favLang["anand"] = a
#favLang["anand"] = b
#favLang["ram"] = c
#favLang["jai"] = d

#print(favLang) #if same name prints the last one

#problem 8, if languages of 2 friends are same, what happens to the program?
favLang["swathi"] = a
favLang["anand"] = b
favLang["ram"] = c
favLang["jai"] = d
print(favLang)

#problem 9, 
#Can you change the values inside a list which is contained in set s?
s = {8,7,12,"harry",[1,2,3]}

#Ans   the given question is wrong.
#   Note:1 = a set can not have a list in it.
# Note: 2 = given problem is a set, set itself unmutable, which  can not be changed.  