# --- Define your functions below! ---

# The chatbot introduces itself and gives the user instructions. 
def intro():
  print("Hi, my name is Phyllis. Let's talk!")
  print("Type something and hit enter.")

# Choose a response based on the user's input.
def process_input(answer):
  # Define a list of possible ways the user might say hello.
  greetings = ["hi", "hello", "hey", "hey there", "sup"]

  # Define a list of possible ways the user might say bye.
  farewells = ["bye", "see ya", "goodbye", "quit", "exit"]

  if is_valid_input(answer, farewells):
    say_goodbye()
    return True # The user wants to exit!
  elif is_valid_input(answer, greetings):
    say_greeting()
  elif 'joke' in answer:
    say_joke()
  else:
    say_default()
  return False # The chatbot will continue asking for user input.

# Display a greeting message to the user.
def say_greeting():
  print("Hey there!")

# Display a farewell message to the user.
def say_goodbye():
  print("See you next time!")

# Tell the user an interactive knock-knock joke.
def say_joke():
  print("Let me tell you a joke!")

  # "Knock knock!" "Who's there"?
  valid_responses = ["who's there", "whos there", "who's there?", "whos there?"]
  done = False
  while not done:
    answer = input("Knock knock! ")
    if not is_valid_input(answer.lower(), valid_responses):
      print("No, you're supposed to say, 'Who's there?'")
    else:
      done = True

  # "Little old lady." "Little old lady who?"
  valid_responses = ["little old lady who", "little old lady who?"]
  done = False
  while not done:
    answer = input("Little old lady. ")
    if not is_valid_input(answer.lower(), valid_responses):
      print("No, you're supposed to say, 'Little old lady who?'")
    else:
      done = True

  # Say the punchline!
  print("I didn't know you could yodel!")

# Display a default message to the user.
def say_default():
  print("That's cool!")

# Check if user_input matches one of the elements
#  in valid_responses.
def is_valid_input(user_input, valid_responses):
  for item in valid_responses:
    if user_input == item:
      # If you find a matching response, the input is
      #  valid for this kind of response.
      return True
  # If you didn't find a matching response, after
  #  going through the entire list, the input
  #  isn't valid for this kind of response.
  return False

# --- Put your main program below! ---
def main():
  intro()
  done = False # Use this to keep track of when the user wants to exit.
  while not done:
    answer = input("(What will you say?) ")
    done = process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()