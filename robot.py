"""
Gizoogle Twitter Robot.
Carlos Saucedo, 2018
"""
import twitter
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from TwitterFollowBot import TwitterBot
from BeautifulSoup import BeautifulSoup
import requests
import json
from time import sleep
URL = "http://www.gizoogle.net/textilizer.php" #Gizoogle URL

#Twitter API keys
tokenfile = open("auth_tokens.txt", "r")
tokens = tokenfile.read().splitlines()
CONSUMER_KEY = tokens[0]
CONSUMER_KEY_SECRET = tokens[1]
ACCESS_KEY = tokens[2]
ACCESS_KEY_SECRET = tokens[3]

#Global variables
cleanedTweet = "null"
tweetText = "null"

#Instantiates tweepy bot
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_KEY_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

"""
Translates given text.
"""
def translate(text):
    html = requests.post(URL, data={"translatetext": text}).text
    return BeautifulSoup(html).textarea.contents[0].strip()

"""
Cleans up tweet to be able to be read.
"""
def cleanUpTweet(text):
    output = text.encode("ascii", "ignore")
    output = output.replace("@GizoogleBot", "")
    output = output.replace("#GizoogleThis", "")
    output = output.replace("@gizooglebot", "")
    output = output.replace("#gizooglethis", "")
    return output

#Actual code
print("starting bot.")
class listener(StreamListener):
    def on_status(self, status):#when a new tweet with a matching filter is created
        cleanedTweet = cleanUpTweet(status.text)
        if "RT @" not in cleanedTweet:#Check to see if tweet is retweet
            processedTweet = "@" + status.user.screen_name + ": " + translate(cleanedTweet)
            api.update_status(processedTweet)
            return True
    def on_error(self, status):
        print status
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["@GizoogleBot"])