#!/usr/bin/python3
"""  queries the Reddit API and returns the number of subscribers  """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'Custom'}
    req = requests.get(url, headers=user_agent, allow_redirects=False)
    if req.status_code == 200:
        req = req.json()
        data = req.get('data')
        subscribers = data.get('subscribers')
        if data is not None and subscribers is not None:
            return subscribers
    return 0
