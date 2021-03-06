#!/usr/bin/python3
""" displays the 10 hot reddit posts in a specified subreddit """
import requests


def top_ten(subreddit):
    """ Queries the Reddit API and prints the titles """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-Agent': 'Fredhii'}
    req = requests.get(url, headers=user_agent, allow_redirects=False,
                       params={'limit': 10})
    if req.status_code == 200:
        req = req.json()
        data = req.get('data')
        children = data.get('children')
        if data is not None and children is not None:
            for post in children:
                post_data = post.get('data')
                title = post_data.get('title')
                print(title)
    else:
        print('None')
