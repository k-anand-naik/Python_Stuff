#strip function

#this = "          Anand        "
#print(this)
#print(this.strip()) #eleminates all spaces and returs the string



#write a python funtion to remove a given word from a string and strip it at the same time

def remove_and_split(string,word):
	newstr = string.replace(word," ")
	return newstr.strip()

this = input("Enter the string: ") #"    anand where are you?   "
print(remove_and_split(this,"anand"))		