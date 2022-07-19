# rProjectZomboid

This bot will take hot posts from r/ProjectZomboid on Reddit and post them on Twitter.

To view the bot on action, here is the Twitter profile: https://twitter.com/rProjectZomboid

## How to use

Install Python

Install requirements.txt
```pip install requirements.txt```

Open config.py and fill the fields

From https://www.reddit.com/prefs/apps create a application and you'll get the keys

```
client_id='client id'
client_secret='client secret'
password='reddit password'
user_agent='Any title for your script'
username='reddit username'
```

From https://developer.twitter.com/en create a application and get the keys

```
api_key='api key'
api_key_secret='api key secret'
bearer_token='bearer token'
access_token='access token'
access_token_secret='access token secret' 
```

## Running

Run main.py