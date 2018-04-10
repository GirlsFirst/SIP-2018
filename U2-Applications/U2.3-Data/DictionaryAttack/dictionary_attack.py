def main():

  f = open("dictionary.txt","r")
  in_dictionary = False

  print("Can your password survive a dictionary attack?")
  test_password = input("Type in a trial password: ")

  for line in f:
    test_password = find_variations(test_password)
    if line.strip() == test_password.strip():
      in_dictionary = True
      print("Password match found: ", line.strip())
      break

  if not in_dictionary:
    print("Password not found... in this dictionary attack")

# For extension project only:
# Check and convert common letter-to-number substitutions
def find_variations(password):
  password = password.replace("1", "l")
  password = password.replace("!", "i")
  password = password.replace("2", "z")
  password = password.replace("3", "e")
  password = password.replace("@", "a")
  password = password.replace("4", "a")
  password = password.replace("$", "s")
  password = password.replace("5", "s")
  password = password.replace("6", "g")
  password = password.replace("7", "t")
  password = password.replace("8", "b")
  password = password.replace("9", "g")
  password = password.replace("0", "o")
  return password

if __name__ == '__main__':
  main()