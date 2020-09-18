#!/usr/bin/python3
""" This is about consuming reddit API's """

import requests


def recurse(subreddit, hot_list=[], after="start"):
    """recursive function """
    if not after:
        return(hot_list)
    url = "https://www.reddit.com/search/.json?q={}&sort=hot&after={}".format(subreddit, after)
    headers = {'User-agent': 'Chrome'}
    response = requests.get(url, headers=headers)
    after = response.json()['data']['after']
    t = [item['data']['title'] for item in response.json()['data']['children']]
    hot_list.extend(t)
    recurse(subreddit, hot_list, after)
