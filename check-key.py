import twitter

# load credentials 
from ConfigParser import SafeConfigParser
config = SafeConfigParser()
config.read('config.ini')

#print config.get("auth", "access_key")
# create twitter API object
twitter = twitter.Api(
    config.get("auth", "consumer_key"),
    config.get("auth", "consumer_secret"),
    config.get("auth", "access_key"),
    config.get("auth", "access_secret")
  )

# get whoami
whoami = twitter.VerifyCredentials()
print whoami.screen_name
