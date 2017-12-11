'''
In this program, we print out all the text data from our twitter JSON file.

For students who finish this part of the program quickly, 
they might try it on the larger JSON file to see how much longer that takes.
'''

import json

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#print data
for tweet in tweetData:
	print("Tweet text: " + tweet["text"])