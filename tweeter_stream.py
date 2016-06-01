import tweepy
from tweepy import OAuthHandler
from tweepy import Stream


access_token = "1927765340-qgMNquKSLkrAni2FnriXUw8EV7rx37Jg2BDFIxe"
access_token_secret = "9y0XYwAgN0TCc18a0p0u3b9Vh55jM1wLqx1TTu2TSC3Fz"
consumer_key = "D6eoukDGNqtzsT0hxJhXZtloQ"
consumer_secret="Rf93BsXvND6LIHT9Y6OkxvNofkWQjCKPFGtxH6uW137JxX6ed4"


#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)



myStreamListener = MyStreamListener()

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())