'''
In this program, we iterate over a list of survey questions and save
the responses in a dictionary with a related, easier to read key that
corresponds with each question.

For students who finish this part of the program quickly, a student might
extend the program to catch invalid or blank responses.
'''



# Create the dictionary to store the responses.
answers = {}

# Create a list of survey questions and a list of related keys that will be used when storing survey results.
survey = [
    "What is your name?",
    "How old are you?",
    "What is your hometown?",
    "What is your date of birth? (DD/MM/YYYY)"]
keys = ["name", "age", "hometown", "DOB"]

# Iterate over the list of survey questions and take in user responses.
for x in range(len(survey)):
    response = input(survey[x] +":     ")
    answers[keys[x]] = response

# Print the entire dictionary.
print(answers)
