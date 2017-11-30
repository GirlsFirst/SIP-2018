'''
This program loads survey data that is saved in a JSON file and does some simple analysis
of the data.
'''

import json
from pprint import pprint


# Open a json file and append entries to the file.
f = open("allanswers.json", "r")
data = json.load(f)
print(type(data))
print(data)
f.close()

'''
Do some analysis with your data.
You can do whatever you choose, but this code calculates
the average age of people in your data set.
'''

# Example of how to iterate over the list of dictionaries and pull out particular pieces of information.
ages = []
for s in range(len(data)):
    if data[s]['age'] is not '': # Catches and skips over blank entries.
        ages.append(int(data[s]['age']))

print(ages)
total = sum(ages)
average = total/len(ages)

print(average)
