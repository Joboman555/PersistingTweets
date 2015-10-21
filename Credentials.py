import json
import tweepy

__author__ = 'jspear'


def getCredential(credential, credentialsLocation):
    "Get a credential from a json file from a given location"
    try:
        with open(credentialsLocation) as data_file:
            data = json.load(data_file)
            return data[credential]
    except:
        return ""


def getConsumerKey(credentialsLocation):
    local_consumer_key = getCredential("ConsumerKey", credentialsLocation)
    if local_consumer_key:
        return local_consumer_key
    else:
        return raw_input("Enter your consumer key: ")


def getConsumerSecret(credentialsLocation):
    local_consumer_secret = getCredential("ConsumerSecret", credentialsLocation)
    if local_consumer_secret:
        return local_consumer_secret
    else:
        return raw_input("Enter your consumer secret: ")


def getAccessToken(credentialsLocation):
    local_access_token = getCredential("AccessToken", credentialsLocation)
    if local_access_token:
        return local_access_token
    else:
        return raw_input("Enter your access token: ")


def getAccessTokenSecret(credentialsLocation):
    local_access_token_secret = getCredential("AccessTokenSecret", credentialsLocation)
    if local_access_token_secret:
        return local_access_token_secret
    else:
        return raw_input("Enter your access token secret: ")


def getAuthentication(credentialsLocation):
    consumer_key = getConsumerKey(credentialsLocation)
    consumer_secret = getConsumerSecret(credentialsLocation)

    access_token = getAccessToken(credentialsLocation)
    access_token_secret = getAccessTokenSecret(credentialsLocation)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return auth
