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

# Print the list of dictionaries.
print(list_of_answers)

# Create a list to store all of the names from the survey results, and print the names.
names = []
for s in range(len(list_of_answers)):
    names.append(list_of_answers[s]["name"])
print(names)

# Open a json file and append entries to the file.
f = open("allanswers.json", "a")
json.dump(list_of_answers, f)
