# --- Define your functions below! ---

# The chatbot introduces itself and gives the user instructions. 
def intro():
  print("Hi, my name is Phyllis. Let's talk!")
  print("Type something and hit enter.")

# Choose a response based on the user's input.
def process_input(answer):
  if answer == "hi":
    say_greeting()
  else:
    say_default()

# Display a greeting message to the user.
def say_greeting():
  print("Hey there!")

# Display a default message to the user.
def say_default():
  print("That's cool!")
  

# --- Put your main program below! ---
def main():
  intro()
  while True:
    answer = input("(What will you say?) ")
    process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()