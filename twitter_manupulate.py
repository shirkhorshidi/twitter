import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path,"r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print len(tweets_data)

#writing the resulted json to a file

with open('sample_json.txt','w') as outfile:
    json.dump(tweets_data,outfile)
