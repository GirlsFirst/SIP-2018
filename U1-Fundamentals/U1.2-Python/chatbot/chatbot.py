def intro():
  print("Hi, my name is Phyllis. Let's talk! Type something and hit enter.")

def processInput(answer):
  default_response()

def default_response():
  print("That's cool!")

# Put your main program below!
intro()
done = False

while not done:
  answer = input("(What will you say?) ")
  processInput(answer)