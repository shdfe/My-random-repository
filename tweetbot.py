import tweepy
import requests
auth = tweepy.OAuthHandler('TFQ8j7iucP5OBpFl4RrxBN5h8', 'AlKCktwXKFyBHlMt4ZqRSPKpJ6YDapm79d1wyAI5TbJ4PEt1ue')
auth.set_access_token('1233849629256503296-8id8G71A9RcfqrAurLDQiIX1RNsYEW', 'rIkKFwmrL4a331835GGiDYMtGnOrhZE2zBub3qHqCM1BF')
api = tweepy.API(auth)


res = requests.get(
    'https://icanhazdadjoke.com',
    headers={'Accept':'application/json'}
    )
if res.status_code == requests.codes.ok:
    api.update_status(str(res.json()['joke']))
else:
    pass
 
