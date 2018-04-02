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
URL = 'http://www.gizoogle.net/textilizer.php' #Gizoogle URL

#Twitter API keys
CONSUMER_KEY = ''
CONSUMER_KEY_SECRET = ''
ACCESS_KEY = ''
ACCESS_KEY_SECRET = ''

#Instantiates tweepy bot
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_KEY_SECRET)
api = tweepy.API(auth)

#Search test
for result in api.search(q="#python"):
    print result.text

"""
Removes Twitter labels from string.
"""
def removeTwitterTags(string):
    string.replace('@GizoogleBot', '')
    string.replace('#GizoogleThis','')

"""
Translates given text.
"""
def translate(text):
    html = requests.post(URL, data={'translatetext': text}).text
    return BeautifulSoup(html).textarea.contents[0].strip()