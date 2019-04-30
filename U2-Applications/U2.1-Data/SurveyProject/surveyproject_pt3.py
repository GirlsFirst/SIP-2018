'''
This program expands the previous program by saving any new data to an existing
JSON file. This requires file i/o commands, as well as parsing the data to save
the responses as a correctly formatted file.

If students finish this section quickly, encourage them to define functions to make
their program more modular and might allow them to reuse pieces of the code later.
'''
import json

# Create a list of survey questions and a list of related keys that will be used when storing survey results.
survey = [
    "What is your name?",
    "How old are you?",
    "What is your hometown?",
    "What is your date of birth? (DD/MM/YYYY)"]

keys = ["name", "age", "hometown", "DOB"]

# Create a list that will store each person's survey responses as a separate dictionary.
list_of_answers = []

# Continue to create new entries until the user exits.
done = "NO"
while done == "NO":

    # Create the dictionary to store the responses.
    answers = {}
    print("New entry! Please answer the questions below.")

    # Iterate over the list of survey questions and take in user responses.
    for x in range(len(survey)):
        response = raw_input(survey[x] +":     ")
        answers[keys[x]] = response

    list_of_answers.append(answers)
    done = raw_input("\nAre you done collecting information? Type YES or NO.     ")

# Open the file containing all past results and append them to our current list.
f = open("allanswers.json", "r")
olddata = json.load(f)
list_of_answers.extend(olddata)
f.close()

# Reopen the file in write mode and write each entry in json format.
f = open("allanswers.json", "w")
f.write('[\n')
index = 0
for t in list_of_answers:
    if (index < len(list_of_answers)-1):
        json.dump(t, f)
        f.write(',\n')
    else:
        json.dump(t, f)
        f.write('\n')
    index += 1

f.write(']')
f.close()
