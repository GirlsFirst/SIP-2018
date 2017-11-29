
# Create a list of survey questions and a list of related keys that will be used when storing survey results.
survey = [
    "What is your name?",
    "How old are you?",
    "What is your hometown?",
    "What is your date of birth? (DD/MM/YYYY)"]
keys = ["name", "age", "hometown", "DOB"]

# Create a list that will store each person's individual survey responses.
list_of_answers = []

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

    done = raw_input("Are you done collecting information? Type YES or NO.     ")

# Print the list of dictionaries.
print(list_of_answers)

# Example of how to iterate over the list of dictionaries and pull out particular pieces of information.
names = []
for s in range(len(list_of_answers)):
    names.append[list_of_answers[s]["name"]]
print(names)
