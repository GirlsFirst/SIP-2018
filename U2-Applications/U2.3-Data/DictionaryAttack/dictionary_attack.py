f = open("dictionary.txt","r")
in_dictionary = False


print("Can your password survive a dictionary attack?")
test_password = input("Type in a trial password: ")

for line in f:
        if line.strip() == test_password.strip():
                in_dictionary = True
                break

if in_dictionary:
        print("Found password")
else:
        print("Password not found... in this dictionary attack")
