#importing the methods needed from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#variables that contains credentials for accesing twitter API
access_token = "1927765340-qgMNquKSLkrAni2FnriXUw8EV7rx37Jg2BDFIxe"
access_token_secret = "9y0XYwAgN0TCc18a0p0u3b9Vh55jM1wLqx1TTu2TSC3Fz"
consumer_key = "D6eoukDGNqtzsT0hxJhXZtloQ"
consumer_secret="Rf93BsXvND6LIHT9Y6OkxvNofkWQjCKPFGtxH6uW137JxX6ed4"

#this is a basic listener that just prints received tweets to stdout

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    #this handles twitter authentification and the connection to twitter streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth,l)

    #this line filter twitter stream to capture data by the keywords: 'python', 'Javascript', 'ruby'
    stream.filter(track=['python','javascript','ruby'])







