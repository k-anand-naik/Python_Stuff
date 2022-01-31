#problem 3 = spam detector
#write a program to detect a spam in text entered by the user

text = input("enter the text/sentence:\n")
 
if "make a lot money" in text:
 	spam = True
elif "buy now" in text:
	 spam = True
elif "click here" in text:
	 spam = True
elif "subscribe this" in text:
	 spam = True
else:
 	spam = False
 
if(spam):
  print("this text is spam")
else:
  print("this text is not spam") 		 	 	  		 	 	    		 	 	  		 	 	   		 	 	  
 		 	 	  		 	 	  
 		 	 	  		 	 	  		 	 	  		 	 	  