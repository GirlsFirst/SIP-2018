# --- Define your functions below! ---

# The chatbot introduces itself and gives the user instructions. 
def intro():
  print("Hi, my name is Phyllis. Let's talk!")
  print("Type something and hit enter.")

# Choose a response based on the user's input.
def process_input(answer):
  # Define a list of possible ways the user might say hello.
  greetings = ["hi", "hello", "hey", "hey there", "sup"]

  if is_valid_input(answer, greetings):
    say_greeting()
  else:
    say_default()

# Display a greeting message to the user.
def say_greeting():
  print("Hey there!")

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
  while True:
    answer = input("(What will you say?) ")
    process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()