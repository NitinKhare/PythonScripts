import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob as tb

consumerKey    = ""
consumerSecret = ""

accessToken  = ""
accessTokenSecret = ""

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
toSearchFor = input("Enter the subject to search for ")
allTweets = api.search(toSearchFor)
labels = 'Happy', 'Neutral', 'Angry'
colors = ['gold','#f0f0f0','Red']

happy = 0
neutral = 0
angry = 0

for tweet in allTweets:
    analyze = tb(tweet.text)
    if analyze.sentiment.polarity > 0:
        happy +=1
    elif analyze.sentiment.polarity < 0:
        angry +=1
    else:
        neutral +=1

sizes = [happy, neutral, angry]
explode = (0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('How are people feeling about '+toSearchFor+' on Twitter')
plt.axis('equal')
plt.show()


