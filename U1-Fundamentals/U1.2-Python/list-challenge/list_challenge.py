### LEVEL 1 ###

from random import *

#Code below is the skeleton for a simple name generator.

#Create the list of words you want to choose from.
word_list = ["frank", "bean", "jean", "louis", "lisa", "pisa", "italy", "spaghetti"]

name = ""

for x in range(2):

    #Generates a random integer.
    x = randint(0, len(word_list)-1)
    name += word_list[x] + " "

print(name)
print("")

### LEVEL 2 ###

from random import *

#Code below is the skeleton for a menu generator.

#Create the list of words you want to choose from.
side = ["beans", "rice", "salsa", "guac", "chips"]
main = ["tamale", "burrito", "enchilada", "tostada"]
dessert = ["flan", "rice pudding", "sopapillas"]

sides_selected = []

for x in range(2):

    #Generates a random integer.
    x = randint(0, len(side)-1)
    sides_selected.append(side[x])

print("sides: ", sides_selected)

#Generates a random integer.
x = randint(0, len(main)-1)
print("main: ", main[x])

x = randint(0, len(dessert)-1)
print("dessert: ", dessert[x])


print("")

### LEVEL 3 ###

from random import *

#Code below is the skeleton for a simple haiku generator.

#Create the list of words you want to choose from.
five_syllable = ["Hey, I just met you", "First I was afraid", "Love the one you’re with"]
seven_syllable = ["Now, winter chills on my feet", "A time of joy, peace and love", "Your shadow, one can not find"]

first_sentence = ""
second_sentence = ""
third_sentence = ""

#Generates a random integer.
x = randint(0, len(five_syllable)-1)
print(five_syllable[x])

x = randint(0, len(seven_syllable)-1)
print(seven_syllable[x])

x = randint(0, len(five_syllable)-1)
print(five_syllable[x])
