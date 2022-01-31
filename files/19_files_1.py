#reading mode
f = open('mydata_1.txt','r')
#text = f.read()
#print(text)
#f.close()

#reading mode with required number of times
#text = f.read(10)
#print(text)
#f.close()

#reading mode with reading only required number of times
f = open('mydata_1.txt')     #if you wont mention the type of the mode, it will take 'r' by default

#reads first line 
text = f.readline()
print(text,end="")
#print(len(text))
#print(text.upper(),end="")
#print(text.capitalize(),end="") # if you give space in end=" " you get space at starting of the  line2 and line3 

#reads second line
text = f.readline()
print(text,end="")
#print(text.upper(),end="")
#print(text.capitalize(),end="")

#reads 3rd line
text = f.readline()
print(text,end="")
#print(text.upper(),end="")
#print(text.capitalize(),end="")

f.close()