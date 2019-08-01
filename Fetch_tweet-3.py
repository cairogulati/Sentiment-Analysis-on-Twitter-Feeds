import sys
import os
import jsonpickle
import tweepy
from textblob import TextBlob
import re

consumer_key = 'DKSrx5YH13hLd4pR8StLkwxTH'
consumer_secret = 'n6hLm4H0Z9zfkZhtFTJGqzOTmwa4Mu9zce1g2XgsBVfXW0W0cX'
access_token = '1538132845-S7RXlGdrJ1ey7DC3kECUCZ8hBx3s0yRUpbpoTJP'
access_token_secret = 'Zq0pq2jlCyGB6mA7kBjvuOytN2Uaj1cQrgp74yzchNc9X'

def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
    #print(tweet)
    # set sentiment
    #print(analysis.sentiment.polarity)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        #print(tweet)
        return 'neutral'
    else:
        
        return 'negative'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
if (not api):
    print ("Problem connecting to API")

places = api.geo_search(query="Delhi", granularity="neighborhood")

place_id = places[0].id

#print('id is: ',place_id)

#Switching to application authentication
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

#Setting up new api wrapper, using authentication only
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
 
#Error handling
if (not api):
    print ("Problem Connecting to API")
searchQuery = 'place:{}#BJP OR' \
              '"modi" '.format(place_id)

#Maximum number of tweets we want to collect 
maxTweets = 1000000

#The twitter Search API allows up to 100 tweets per query
tweetsPerQry = 150
Pos_tweet=[]
Neg_tweet=[]
Neut_tweet=[]
def BMP(s):
        return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))
    
for tweet in tweepy.Cursor(api.search,q=searchQuery,lang='en').items(maxTweets) :
    #tweet=tweet["text"].encode('utf-8')
    #tweet=" ".join(re.findall("[a-zA-Z]+",tweet))
    #print(tweet.place)
    #print(tweet.place)
    pred=get_tweet_sentiment(BMP(tweet.text))
    if(pred=='positive'):
        Pos_tweet.append(tweet)
    elif(pred=='negative'):
        Neg_tweet.append(tweet)
    else:
        Neut_tweet.append(tweet)
tot_tweet=len(Pos_tweet)+len(Neg_tweet)+len(Neut_tweet)
print(tot_tweet)
print("Percentage positive tweets:"+str(len(Pos_tweet)*100/tot_tweet))
print("Percentage negative tweets:"+str(len(Neg_tweet)*100/tot_tweet))
print("Percentage neutral tweets:"+str(len(Neut_tweet)*100/tot_tweet))
#print(tot_tweet)
    #print(tweet.place)
#print(api.rate_limit_status()['resources']['search'])
##print("----------------------------------------------------------------------------------------------------")
##auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
##auth.set_access_token(access_token, access_token_secret)
##api = tweepy.API(auth)
##class MyStreamListener(tweepy.StreamListener):
##    
##    #Overload the on_status method
##    def on_status(self, status):
##        try:
##                print("It came here")
##            #Open a text file to save tweets to
##            
##                
##                #Check if the tweet has coordinates, if so write it to text
##                if (status.coordinates is None):
##                    print(BMP(status.text))
##                    print(status.coordinates)
##                return True
##         
##        #Error handling
##        except BaseException as e:
##            print("Error on_status: %s" % str(e))
##            
##        return True
## 
##    #Error handling
##    def on_error(self, status):
##        print(status)
##        return True
##
##    #Timeout handling
##    def on_timeout(self):
##        return True 
##twitter_stream = tweepy.Stream(auth, MyStreamListener())
##twitter_stream.filter(track=['Narendra Modi'])
##twitter_stream.filter(locations=[72.63,23.21,71.636941,24.21])

