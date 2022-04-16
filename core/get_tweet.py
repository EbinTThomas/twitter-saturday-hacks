import tweepy

consumer_key = "IxDfaoaW2feAqHXuOsQSJr0an"
consumer_secret = "scrFUHIPSxBV4P9LsxAGwPjfvTsm7LcVuqLnfgrAUKDbr9tQO7"
access_key = "1491153168566083584-Hn0jIWfo5rMQs3VwsymfTaLq4cCAmz"
access_secret = "GKAUa86GDVW9dVk5tTS7aCu79HRy63cCkoW67nWnqXg9z"

def get_tweets(username):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)

  api = tweepy.API(auth)
  tweets = api.user_timeline(screen_name=username)

  tmp=[]

  tweets_text = [tweet.text for tweet in tweets]
  for j in tweets_text:
    tmp.append(j)
  print(tweets_text)
  return tmp

if __name__ == '__main__':
	get_tweets("@elonmusk")
