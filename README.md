# APTS #
### Automatic Packet Tweeting System ###

This is an APRS-Twitter interface. It connects to the APRS-IS network and listens for tweets sent to a given callsign.
You need a Twitter API key to run the code.
You will also need to create a config file:

#### config.py: ####
```python
callsign = 'N0CALL'
consumer_key = 'xxxxxxxxxx'
consumer_secret = 'xxxxxxxxxx'
access_token = 'xxxxxxxxxx'
access_token_secret = 'xxxxxxxxxx'
```