# encoding: utf-8
### python script to interact with Beeminder
### from @deanishe tutorial 
### giovanni, Sunday, April 4, 2021, 11:46 AM 


import sys
from workflow import Workflow3, ICON_WEB, web
from beeminder_get import get_goals

from config import TOKEN, BEEUSER, BEECOMMENT


def post_goals(mySlug,myValue,myComment):
	
	url = 'https://www.beeminder.com/api/v1/users/' + BEEUSER + '/goals/' + mySlug + '/datapoints.json' + 'post'

	datastring = dict()
	datastring['auth_token'] = TOKEN
	datastring['value'] = myValue
	datastring['comment'] = myComment + BEECOMMENT.decode ('utf-8')
	r = web.post(url, data=datastring)

	r.raise_for_status()
	


def main(wf):
	myText = wf.args[1]
	myComment = ''

	myValue = myText.split(' ', 1)[0]

	if (len(myText.split(' ', 1))>1):
		myComment = myText.split(' ', 1)[1]+' '
		
	
	post_goals(wf.args[0],myValue,myComment)
	
	

if __name__ == u"__main__":
	wf = Workflow3()
	log = wf.logger
	sys.exit(wf.run(main))




