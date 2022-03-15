#!/usr/bin/python3 

### python script to interact with Beeminder
### from @deanishe tutorial 
### giovanni, Wednesday, March 31, 2021
## version 2 for Python3



import sys
import os
import time
from datetime import datetime

import random
import urllib.request 

from urllib.parse import urlencode
import json

from config import TOKEN, BEEUSER

# get seed from environment variable or current time
seed = float(os.getenv('seed') or time.time())
# initialise RNG with seed to get deterministic values
random.seed(seed)


def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)

def get_goals():
    
    url= 'https://www.beeminder.com/api/v1/users/'+ BEEUSER + '/goals.json' #gets a list of goals with basic info
    params = urlencode({'auth_token':TOKEN}) 
    myURL=url+"?"+params
    
    URLrequest = urllib.request.Request(myURL)

    with urllib.request.urlopen(URLrequest) as URLresponse: 
            goals = json.load(URLresponse)
            #log(URLresponse.status) 
            #log(goals) 
    
    return goals



currTime = int (time.time())

goals=get_goals()


    # Loop through the returned goals and add an item for each to
    # the list of results for Alfred





result = {"rerun": 1,
"variables": {
        "seed": str(seed)
    },
    "items": []}

for goal in goals:
    
    myStamp = goal['losedate']-currTime
    if myStamp < 86400: # less than 24 hours from derailing
        myIcon = "img/redDot.png"
    elif myStamp < 172800: # less than 2 days from derailing
        myIcon = "img/orangeDot.png"
    else:
        myIcon = "img/greenDot.png"

    readable = datetime.fromtimestamp(myStamp)
    readable = readable.strftime('%M:%S')
    myHou = int(myStamp/3600)
    result["items"].append({
    "title": goal['slug'] + " - " + goal['title'] + " ($"+ str(int(goal['pledge'])) + ")",
    "subtitle": str(myHou) + ":" + str(readable)  + " " + goal['limsumdate'],
    
    "icon": {
                                "path": myIcon
                            },
    "valid":'TRUE',
    "uid":goal['slug'] + str(seed),
    
    "arg":goal['slug']
    })

    

# Send the results to Alfred as JSON
print (json.dumps(result))


 

