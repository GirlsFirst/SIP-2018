import random

# A list of words that 
potential_words = ["example", "words", "someone", "can", "guess"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()


guesses = []
numfails = 0
maxfails = 7
wordToGuess = []

for letter in word:
	wordToGuess.append("_")

done = False

while not done:
	print("-----------------------------------")
	print("Lives Left: ", maxfails - numfails)
	print("Guesses So Far: ", guesses)
	print("Current Word: ", wordToGuess)

	guess = input("Guess a letter: ")
	guess = guess.lower()

	if(len(guess) > 1):
		print("That's too long!")
	elif(guess.isalpha() == False):
		print("That's not a letter!")
	elif(guess in guesses):
		print("You already guessed that!")
	else:
		guesses.append(guess)

		if(guess in word):
			print("You got a letter!")
			for idx in range(0, len(word)):
				if word[idx] == guess:
					wordToGuess[idx] = guess

			done = True
			for idx in range(0, len(wordToGuess)):
				if wordToGuess[idx] == "_":
					done = False
					break
			if done:
				print("You won! It was: " + word)
		else:
			print("Wrong guess!")
			numfails += 1

			if numfails >= maxfails:
				print("You lost!")
				done = True