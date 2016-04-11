import tweepy, time, sys
argfile = str(sys.argv[1])
  
CONSUMER_KEY = "qMChojDsZ6J6qGlViY1tHvvdJ"
CONSUMER_SECRET = "rmSlUG0JI9K5x8rVJdcqpKGjCjUMJ7B1y7i5jj6SS1JLZ9PESN"
ACCESS_KEY = "395543545-NiwKwFC3IlA8WtaKQ4aeRaCP1pbs5KiALOy0NNF3" # Access Token
ACCESS_SECRET = "jsgNJsJrXcXyryttFw9mO5ZhFNXdGB98bQpk2Hb8EQHOE" # Access secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
     
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
     
for line in f:
    api.update_status(line)
    time.sleep(600) #Tweet every 10 minutes
