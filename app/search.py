import tweepy
import config
import json


def getClient():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN,
                           consumer_key=config.API_KEY,
                           consumer_secret=config.API_KEY_SECRET,
                           access_token=config.ACCESS_TOKEN,
                           access_token_secret=config.ACCESS_TOKEN_SECRET)
    return client



def searchTweets(client, query, max_results):

    tweets = client.search_recent_tweets(query=query, max_results=max_results)

    tweet_data =  tweets.data
    results = []

    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in tweet_data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            results.append(obj)

    return results



def getTweet(client, id):
    tweet = client.get_tweet(id, expansions=['author_id'], user_fields=['username'])
    return tweet



def returnSearchTweetList(query, max_results):
    client = getClient()
    tweets = searchTweets(client, query, max_results)

    objs = []

    if len(tweets) > 0:
        for tweet in tweets:
            twt = getTweet(client, tweet['id'])
            obj = {}
            obj['text'] = tweet['text']
            obj['username'] = twt.includes['users'][0].username
            obj['id'] = tweet['id']
            obj['url'] = 'https://twitter.com/{}/status/{}'.format(twt.includes['users'][0].username, tweet['id'])
            objs.append(obj)

    return objs




def retweet(id):
    client = getClient()
    client.retweet(id)
