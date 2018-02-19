#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

numTries = 0 # don't need this variable in for loops
while True: # for numTries in range(3):
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	numTries += 1
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
		continue
	else:
		guess = int(guess) # converts a string to an integer

	# check if correct
	if guess == aRandomNumber:
		print("You go it!")
		break

	# check if out of tries
	if numTries >= 3: #numTries >= 2
		print("Sorry! You failed.")
		break

	# give hints
	if(guess > aRandomNumber):
		print("Try a smaller number next time.")
	elif(guess < aRandomNumber):
		print("Try a bigger number next time.")