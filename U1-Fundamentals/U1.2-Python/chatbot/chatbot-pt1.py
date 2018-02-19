# --- Define your functions below! ---

# The chatbot introduces itself and gives the user instructions. 
def intro():
  print("Hi, my name is Phyllis. Let's talk!")
  print("Type something and hit enter.")


# --- Put your main program below! ---
def main():
  intro()
  while True:
    answer = input("(What will you say?) ")
    print("That's cool!")


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()