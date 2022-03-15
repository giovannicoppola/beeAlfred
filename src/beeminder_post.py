#!/usr/bin/python3 

### python script to interact with Beeminder
### from @deanishe tutorial 
### giovanni, Sunday, April 4, 2021, 11:46 AM 
## March 2022, version 2.0 for Python3


import sys
from config import TOKEN, BEEUSER, BEECOMMENT
from urllib import request, parse

def post_goals(mySlug,myValue,myComment):
	
	
	url = 'https://www.beeminder.com/api/v1/users/' + BEEUSER + '/goals/' + mySlug + '/datapoints.json' + 'post'

	datastring = dict()
	datastring['auth_token'] = TOKEN
	datastring['value'] = myValue
	datastring['comment'] = myComment + BEECOMMENT
	data = parse.urlencode(datastring).encode()
	req =  request.Request(url, data=data) # this will make the method "POST"
	request.urlopen(req)
	
	
	



myText = sys.argv[2]
myComment = ''

myValue = myText.split(' ', 1)[0]

if (len(myText.split(' ', 1))>1):
	myComment = myText.split(' ', 1)[1]+' '
	

post_goals (sys.argv[1],myValue,myComment)


