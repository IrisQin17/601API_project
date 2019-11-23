#copyright 2019 Bowen Qin
#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy, csv, json

def getHashtagTweets(maxNum, hashtag):

	# Twitter API credentials
	consumer_key = ""
	consumer_secret = ""
	access_key = ""
	access_secret = ""

    #authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	# # Mention the maximum number of tweets that you want to be extracted.
	# maxNum = int(input("Enter the number of tweets that you want to extract: "))

	# # Mention the hashtag that you want to look out for
	# hashtag = input("Enter the hashtag you want to scrape: #")
	file = open("tweets#" + hashtag + ".txt", "a")
	# file = open("tweets#" + hashtag + ".json", "w")
	for tweet in tweepy.Cursor(api.search, q="#" + hashtag, rpp=100).items(maxNum):
		#json.dump(tweet._json, file)
		file.write(str(tweet.text.encode("utf-8")) + "\n" + "\n")
	file.close()
