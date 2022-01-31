import random
randNumber = random.randint(1,50)
#print(randNumber) # prints whatever the computer guessed (but we dont wanted to cheat so remove it)

userGuess = None
guesses = 0

while(userGuess != randNumber):
	userGuess = int(input("Enter your number: "))
	print()
	guesses += 1
	
	if (userGuess == randNumber):
		print("Hurry!🤸, You guessed it right! ")
		print()
	else:
		if(userGuess > randNumber):
			print("Sorry!, you guessed it wrong! Enter a smaller number: ")
		else:
			print("Sorry!, you guessed it wrong! Enter a higher number: ")

print(f"You guessed the number in {guesses} guesses")						

with open("HighScore.txt", 'r') as f:
	HighScore = int(f.read())

if(guesses < HighScore):
	print("Wow!😯, You have just broken the high score!😎")
else:
	print("Sorry😭, you have not broken the high score! ")	
	with open("HighScore.txt", 'w') as f:
		f.write(str(guesses))																								