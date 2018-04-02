"""
Gizoogle Twitter Robot.
Carlos Saucedo, 2018
"""
import twitter
import tweepy
from TwitterFollowBot import TwitterBot
from BeautifulSoup import BeautifulSoup
import requests
import json
from time import sleep
URL = "http://www.gizoogle.net/textilizer.php" #Gizoogle URL

#Twitter API keys
tokenfile = open("auth_tokens.txt")
tokens = tokenfile.readlines()
CONSUMER_KEY = tokens[0]
CONSUMER_KEY_SECRET = tokens[1]
ACCESS_KEY = tokens[2]
ACCESS_KEY_SECRET = tokens[3]

#Other text files
tweetfile = open("tweets_text.txt")
tweets = tweetfile.readlines()
usernamefile = open("tweets_usernames.txt")
usernames = usernamefile.readlines()
tweetlog= open("tweetlog.txt")

#Global variables
currentTweet = "null"
cleanedTweet = "null"
isEnabled = True

#Instantiates tweepy bot
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_KEY_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

"""
Resets the tweet list.
"""
def resetList():
    tweets = open("tweets_text.txt", "w")
    usernames = open("tweets_usernames.txt", "w")

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
"""
while(isEnabled):
    print("Starting Bot.")
    for result in api.search(q="@GizoogleBot", count=1):
        if(currentTweet != result.text):
            currentTweet = result.text
            print("tweet author: " + result.author.screen_name)
            print(translate(cleanUpTweet(currentTweet)))
        sleep(60)
"""