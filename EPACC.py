from lxml import html
import requests
import twitter
from settings import *
import datetime


page = requests.get('https://www.epa.gov/climatechange')
tree = html.fromstring(page.content)

str_title = tree.xpath('//h1[@class="page-title"]/text()')

print(str_title)

file = open("filename.txt","r")

baseline = file.read()

file.close()



#baseline = "This page is being updated."

print("Page Title: %s" % str_title[0])
print("Baseline  : %s" % baseline)



if(str_title[0] == baseline):
		print("NO CHANGE!!!  NO CHANGE!!!")
else:
		## Run entire twitter infrasctucture
		print("Change has come")
		print('establish the twitter object')
		# see "Authentication" section below for tokens and keys
		api = twitter.Api(consumer_key=CONSUMER_KEY,
			consumer_secret=CONSUMER_SECRET,
			access_token_key=OAUTH_TOKEN,
			access_token_secret=OAUTH_SECRET,
        )

		print('twitter object established')
		lex = len(str_title[0])
		if lex < 210:
			message = "The EPA Climate Change website has changed.  The new title is: "+str_title[0]
			api.PostDirectMessage(message,screen_name="@ejgertz")
			print(message)
		else:
			message = "The EPA Climate Change website has changed.  The new title is: "+(str_title[0][:210])
			api.PostDirectMessage(message,screen_name="@ejgertz")
			print(message)
	
        #api.PostUpdate(message)
		#print(message)
		print(api)

	


file = open("filename.txt","w")

file.write(str_title[0])

file.close()
