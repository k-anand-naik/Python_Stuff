import random
def gameWin(comp,you):
	if comp == you:
		return None
	#if two values are equal, declare a tie!
	elif comp == 's':
		if you == 'w':
			return False
		elif you == 'g':
			return True	
	#check all possibilities when comp chhose 's'
	
	elif comp == 'w':
		if you == 'g':
			return False
		elif you == 's':
			return True		
	#check all possibilities when comp chhose 'w'
			
	elif comp == 'g':
		if you == 's':
			return False
		elif you == 'w':
			return True
	#check all possibilities when comp chhose 'g'
	
print("Computer turn: snake(s) water(w) or gun(g)?")
randNo = random.randint(1,3)

if randNo == 1:
	comp = 's'
elif randNo == 2:
	comp = 'w'
elif randNo == 3:
	comp = 'g'

you = input("Your turn: snake(s) water(w) or gun(g)?")
a = gameWin(comp,you)

print(f"computer choose {comp}")
print()
print(f"You choose {you}")
print()
if a == None:
	print("The game is a tie! \n Try again")
elif a:
	print("hurry! You win!")
else:
	print("Sorry! you lose! \n try again")																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																					