##############################################################
###                       _____ _______ _____              ###
###                 /\   |  __ \__   __/ ____|             ###
###                /  \  | |__) | | | | (___               ###
###               / /\ \ |  ___/  | |  \___ \              ###
###              / ____ \| |      | |  ____) |             ###
###             /_/    \_\_|      |_| |_____/              ###
###            Automatic Packet Tweeting System            ###
###                  Adam Zeloof / KD2MRG                  ### 
###                 http://adam.zeloof.xyz                 ###
###                      May 21, 2019                      ###
##############################################################                             

# This file requires a config.py file to run (see readme)

import aprslib
import tweepy
import pickle
import time
from config import *

global messageLog
global twitter
global timeout

# The number of seconds after which a message
# is no longer considered a duplicate.
timeout = 43200

with open('messageLog.data', 'rb') as filehandle:
    messageLog = pickle.load(filehandle)

def sendTweet(origin, text):
    # Publishes the tweet
    message = text + '\n' + 'de ' + origin
    print(message)
    twitter.update_status(status = message) 


def messageGood(msg):
    # Check that a message is not a duplicate
    curTime = time.time()
    if msg not in messageLog:
        return True
    elif msg['time'] < curTime - timeout:
        return True
    else:
        return False


def callback(packet):
    try:
        if 'addresse' in packet:
            # Find messages addressed to callsign-10
            if packet['addresse'] == callsign + '-10':
                msg = {}
                origin = packet['from']
                text = packet['message_text'].split('{')[0]
                ticks = time.time()
                msg['from'] = origin
                msg['text'] = text
                msg['time'] = ticks
                # Check that the message has not been logged previously
                if messageGood(msg):
                    messageLog.append(msg)
                    pickle.dump(messageLog, open('messageLog.data', 'wb'))
                    sendTweet(origin, text)
    except:
            print('error processing packet:')
            print(packet)
            print('\n')


# Initialize Twitter interface
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret) 
twitter = tweepy.API(auth) 

# Initialize APRS interface
AIS = aprslib.IS(callsign)
AIS.connect()
AIS.consumer(callback, raw=False)
