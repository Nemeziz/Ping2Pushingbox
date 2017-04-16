#!/usr/bin/env python 


#Script to check if a specific host is reachable.
#if not available it will send a notification via Pushinbox.com 
#add this script to crontab to execute i.e. every 5 minutes 
# scriptname.py IP address (scriptname.py 192.168.1.2)


import urllib, urllib2
#import socket
import time
import argparse
import os
import configparser


parser = argparse.ArgumentParser()
parser.add_argument("URL", help="Checks connection to this URL. Write 192.168.1.2")

args = parser.parse_args()

config = configparser.ConfigParser()
config.read('myconfig.ini’)
key = config['DEFAULT']['PushingBoxKey'] #Pushingbox.com scenario Key

#set alarmtime at zero at programstart
alarmtime=0 

class pushingbox():
	url = ""
	def __init__(self, key):
		url = 'http://api.pushingbox.com/pushingbox'
		values = {'devid' : key}
		try:
			data = urllib.urlencode(values)
			req = urllib2.Request(url, data)
			sendrequest = urllib2.urlopen(req)
		except Exception, detail:
			print "Error ", detail


hostname = args.URL

while 1:
 response = os.system("ping -c 3 " + hostname)
 if response == 0:
   print "network active"
 else:
   print"network inactive"
   #only one pushingbox trigger per 600 seconds
   if (time.time() > alarmtime+600):
     pushingbox(key)
     alarmtime = time.time()
 #test connectivity every x seconds
 time.sleep(20) 
 print "End of while loop, again!!"