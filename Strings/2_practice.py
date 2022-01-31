#problem 1 
name = input("enter your name: ")
print("good morning! " + name)

#problem 2
name = input("Enter your name: \n")
print("good morning! " + name)

#problem 3
letter = '''dear <|NAME|>,
congo! you are selected!
date: <|DATE|>'''
name = input("enter you name: \n")
date = input("enter date \n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)

#problem 4
st = "this sentence is having  double space!"
doubleSpace = st.find("  ")
print(doubleSpace)

#problem 5
st2 = "this sentence has no double spaces!"
nodoubleSpace = st2.find("  ")
print(nodoubleSpace)

#problem 6
st3 = "here iam !"
a = st3.replace("iam","we're")
print(a)

#problem 7
st4 = "ths line has double  space!"
b = st4.replace("  "," ")
print(b)


