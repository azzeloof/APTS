# APTS #
### Automatic Packet Tweeting System ###

This is an APRS-Twitter interface. It connects to the APRS-IS network and listens for tweets sent to a given callsign.
You need a Twitter API key to run the code. Before APTS.py is run for the first time you need to run resetLog.py, and create a config file as shown below.

#### config.py: ####
```python
callsign = 'N0CALL'
consumer_key = 'xxxxxxxxxx'
consumer_secret = 'xxxxxxxxxx'
access_token = 'xxxxxxxxxx'
access_token_secret = 'xxxxxxxxxx'
```