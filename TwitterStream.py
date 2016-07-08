
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time 

# please plug your authentication key below.
# you can get your keys from Twitter developer API

ckey = 'IjxrnZXcwR7jLzPigo3VgkQAr'
csecret = 'MUBxNvNo2wWfnDE5Bj6bF9VFuEhueXkeGEU22lcQpNss8Uag0E'
atoken = '190906175-hqCQTNLSKNfCA3nc4oXDVWjWfjH7yf0omoSVSX0i' 
asecret = 'ehnPeqark1QseCaCbrm1kFFnAOpZW28yFWcfFrVu1bmBh'

class listener(StreamListener):

    def on_data(self, data):
    	try:
    		#print data
    		
    	
    		
    		tweet = data.split(',"text":"')[1].split('","source')[0]
    		print tweet
    		
    		
    		saveThis = str(time.time())+'::'+tweet
                # you can set your file save path, in here it will save to your Desktop
    		saveFile = open('soccer.csv','a')
    		saveFile.write(saveThis)
    		saveFile.write('\n')
    		saveFile.close()
    		return True
	except BaseException, e:
    		print 'failed ondata,' , str(e)
    		time.sleep(5)    
    		
    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
# you can change here to any key word you like to stream tweet
twitterStream.filter(track=["besiktas","galatasaray", "fenerbahce"])

