'''
In this program, we will generate a three word clouds from tweet data.
One for positive tweets, one for negative, and one for neutral tweets.

For students who finish this part of the program quickly, 
they might try it on the larger JSON file to see how much longer that takes.
They might also want to try subjective vs objective tweets.
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Wrap this in a function because we'll use it several times
def GetFilteredDictionary(tweetblob, tweetSearch):
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
		filteredDictionary[word.lower()] = tweetblob.word_counts[word.lower()]

	return filteredDictionary

#Wrap this in a function so we can use it three times
def AddFigure(filteredDictionary, plotnum, title):
	wordcloud = WordCloud().generate_from_frequencies(filteredDictionary)
	plt.subplot(plotnum)
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.title(title)
	plt.axis("off")

#Search term used for this tweet
#We want to filter this out!
tweetSearch = "automation" 

#Get the JSON data
tweetFile = open("../TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

#Combine All the Tweet Texts
positiveTweets = ""
negativeTweets = ""
neutralTweets = ""
for tweet in tweetData:
	tweetblob = TextBlob(tweet['text'])
	#Play with the numbers here
	if tweetblob.polarity > 0.2:
		positiveTweets += tweet['text']
	elif tweetblob.polarity < -0.2:
		negativeTweets += tweet['text']
	else:
		neutralTweets += tweet['text']

#Create a Combined Tweet Blob
positiveblob = TextBlob(positiveTweets)
negativeblob = TextBlob(negativeTweets)
neutralblob = TextBlob(neutralTweets)

#Create a matplotlib figure
plt.figure(1)

#Create the three word clouds
AddFigure(GetFilteredDictionary(negativeblob, tweetSearch), 131, "Negative Tweets")
AddFigure(GetFilteredDictionary(neutralblob, tweetSearch), 132, "Neutral Tweets")
AddFigure(GetFilteredDictionary(positiveblob, tweetSearch), 133, "Positive Tweets")

#Show all at once
plt.show()

