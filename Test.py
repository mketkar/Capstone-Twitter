'''
Created on Sep 14, 2013

@author: mayank
'''
from TwitterSearch import *
from pymongo import MongoClient

connection = MongoClient("ds041198.mongolab.com", 41198)
db = connection["testmongo"]
db.authenticate("mketkar", "Mongolab_321") 
Test1 = db.Test1

f = open('/home/mayank/Documents/Capstone/queryWords.txt','r')
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
  #  tso.setKeywords(['ObamaCare','health care','ACA']) # let's define all words we would like to have a look for
    ts = TwitterSearch(
        consumer_key = '',
        consumer_secret = '',
        access_token = '',
        access_token_secret = ''
     )
    tso.setLanguage('en') # we want to see German tweets only
    tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
    tso.setIncludeEntities(False) # and don't give us all those entity information
    stateszip = [', CA',', CO',', CT',', GA',', IN',', KY',', ME',', MO',', NV',', NH',', NY',', OH',', VA',', WI']
    # it's about time to create a TwitterSearch object with our secret tokens



    for lineKeyWord in f:
        tso.setKeywords([lineKeyWord])
        print lineKeyWord
        for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
            count = 0
            for state in stateszip:
                if (tweet['user']['location'].find(state) > 0):
                    count = count + 1
                    if count > 0 :
                        dic = {}
     #   dic["name"] = tweet['user']['screen_name']
                        dic["location"] = tweet['user']['location']
     #   dic["time"]=  tweet['created_at'] 
                        dic["tweettext"] = tweet['text'] 
        #Test1.insert(dic)
                        print dic["location"].split(',')[1]+ ":" + dic["tweettext"]



except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e) 

print "completed"
