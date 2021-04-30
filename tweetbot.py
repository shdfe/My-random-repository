import tweepy
import requests
auth = tweepy.OAuthHandler('xxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
auth.set_access_token('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
api = tweepy.API(auth)


res = requests.get(
    'https://icanhazdadjoke.com',
    headers={'Accept':'application/json'}
    )
if res.status_code == requests.codes.ok:
    api.update_status(res.json()['joke'])
else:
    pass
 
