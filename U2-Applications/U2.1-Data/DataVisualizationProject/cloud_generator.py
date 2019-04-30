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

title = "CS Topics"
mainDict = dict()
mainDict["variables"] = 1
mainDict["loops"] = 1
mainDict["conditionals"] = 1
mainDict["functions"] = 1
mainDict["algorithms"] = 2
mainDict["decomposition"] = 2
mainDict["sorting"] = 4
mainDict["linked lists"] = 3
mainDict["hash maps"] = 3
mainDict["recursion"] = 3
mainDict["binary search trees"] = 4
mainDict["regular expressions"] = 4
mainDict["A* search"] = 4
mainDict["machine learning"] = 4
mainDict["wireframing"] = 1
mainDict["pseudocoding"] = 2
mainDict["state machines"] = 2



#Wrap this in a function so we can use it three times
def AddFigure(dictionary, plotnum, title):
	wordcloud = WordCloud().generate_from_frequencies(dictionary)
	plt.subplot(plotnum)
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.title(title)
	plt.axis("off")


#Create a matplotlib figure
plt.figure(1)

#Create the three word clouds
AddFigure(mainDict, 111, title)

#Show all at once
plt.show()

