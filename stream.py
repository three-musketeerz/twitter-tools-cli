# load library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# load credentials 
from ConfigParser import SafeConfigParser
config = SafeConfigParser()
config.read('config.ini')

# basic listener
# -> prints to stdout
class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True
    def on_error(self, status):
        print status

if __name__ == '__main__':
    # auth handler
    l = StdOutListener()
    auth = OAuthHandler(
				config.get("auth", "consumer_key"),
				config.get("auth", "consumer_secret")
				)
    auth.set_access_token(
				config.get("auth", "access_key"),
				config.get("auth", "access_secret")
				)
    stream = Stream(auth, l)

    # filter by the keywords: 'jakarta'
    stream.filter(track=['jakarta'])