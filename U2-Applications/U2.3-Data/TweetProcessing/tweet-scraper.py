import twitter
import json
import sys

# Read keys and secrets from separate credentials file
credentials_file = open("credentials", "r")

consumer_key = credentials_file.readline().rstrip()
consumer_secret = credentials_file.readline().rstrip()
access_token_key = credentials_file.readline().rstrip()
access_token_secret = credentials_file.readline().rstrip()

# Create an API instance using the credentials
api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

# Get a batch of tweets
try:
  tweets = api.GetSearch(term="automation", count=100)
except twitter.error.TwitterError as e:
  print("Could not make initial query.")
  print(e)
  sys.exit()

# Get as many tweets as you can before hitting your rate limit
oldest = tweets[-1].id
rounds = 0
hitRateLimit = False
while hitRateLimit == False:
  try:
    data = api.GetSearch(term="automation", count=100, max_id=oldest)
    tweets.extend(data)
    oldest = data[-1].id
    rounds += 1
  except twitter.error.TwitterError as e:
    print("Requests made: " + str(rounds))
    print(e)
    hitRateLimit = True
    pass

# Open a file to write results to
f = open('tweets.json', 'w')

f.write('[\n')
index = 0
for t in tweets:
  if (index < len(tweets)-1):
    f.write(t.AsJsonString() + ',\n')
  else:
    f.write(t.AsJsonString() + '\n')
  index += 1
  
f.write(']')
f.close()
