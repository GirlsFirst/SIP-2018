'''
In this program, we will generate a word cloud from tweet data.

For students who finish this part of the program quickly, 
they might try it on the larger JSON file to see what clouds they can get.
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Search term used for this tweet
#We want to filter this out!
tweetSearch = "automation" 

#Get the JSON data
tweetFile = open("../TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#Combine All the Tweet Texts
combinedTweets = ""
for tweet in tweetData:
	combinedTweets += tweet['text']

#Create a Combined Tweet Blob
tweetblob = TextBlob(combinedTweets)

#This can be useful to see what's possible 
#to do with a Textlob object
#print(dir(tweetblob))

#Filter Words
wordsToFilter = ["about", "https", "in", "the", "thing", "will", "could", tweetSearch]
filteredDictionary = dict()

for word in tweetblob.words:
	#skip tiny words
	if len(word) < 2:
		continue
	#skip words with random characters or numbers
	if not word.isalpha():
		continue
	#skip words in our filter
	if word.lower() in wordsToFilter:
		continue
	#don't want lower case words smaller than 5 letters
	if len(word) < 5 and word.upper() != word:
		continue;
	
	#Try lower case only, try with upper case!
	filteredDictionary[word.lower()] = tweetblob.words.count(word, case_sensitive=False) 

#Create the word cloud
wordcloud = WordCloud().generate_from_frequencies(filteredDictionary)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

