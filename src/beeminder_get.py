# encoding: utf-8
### python script to interact with Beeminder
### from @deanishe tutorial 
### giovanni, Wednesday, March 31, 2021


import sys
import os
import json
import time
from datetime import datetime
from workflow import Workflow3, ICON_WEB, web
import random

from config import TOKEN, BEEUSER

# get seed from environment variable or current time
seed = float(os.getenv('seed') or time.time())
# initialise RNG with seed to get deterministic values
random.seed(seed)



def get_goals():
    
    url= 'https://www.beeminder.com/api/v1/users/'+ BEEUSER + '/goals.json' #gets a list of goals with basic info
    params = dict(auth_token=TOKEN)
    r = web.get(url, params)
    r.raise_for_status()

     # Parse the JSON returned by beeminder and extract the goals
    
    result = r.json()
    goals = result
 

    return goals


def main(wf):
    currTime = int (time.time())
    #myRandString = wf.args[0]
    goals=get_goals()
    
    
     # Loop through the returned goals and add an item for each to
     # the list of results for Alfred
    
    wf.rerun = 1
    wf.setvar('seed', str(seed))
    
    

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
        myHou = myStamp/3600
        
        wf.add_item(title=goal['slug'] + " - " + goal['title'] + " ($"+ str(int(goal['pledge'])) + ")",
            subtitle=str(myHou) + ":" + str(readable)  + " " + goal['limsumdate'],
            icon = myIcon,
            valid='TRUE',
            uid=goal['slug'] + str(seed),
            arg=goal['slug'])

     # Send the results to Alfred as JSON
    wf.send_feedback()


 

if __name__ == u"__main__":
    wf = Workflow3()
    log = wf.logger
    
    sys.exit(wf.run(main))



