def intro():
  print("Hi, my name is Phyllis. Let's talk! Type something and hit enter.")

def processInput(answer):
  answer = answer.lower()
  if answer == "bye":
    say_goodbye()
    return True
  elif 'hi' in answer:
    say_greeting()
  else:
    default_response()
  return False

def say_greeting():
  print("Hey there!")

def say_goodbye():
  print("See you next time!")

def default_response():
  print("That's cool!")

# Put your main program below!
intro()
done = False

while not done:
  answer = input("(What will you say?) ")
  done = processInput(answer)