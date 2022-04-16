import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

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
