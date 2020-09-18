#!/usr/bin/python3
""" This is about consuming reddit API's """

import requests


def recurse(subreddit, hot_list=[], after="start"):
    """recursive function """
    if not after:
        return(hot_list)
    url = "https://www.reddit.com/r/{}/.json?after={}".format(subreddit, after)
    headers = {'User-agent': 'Chrome'}
    kwargs = {'allow_redirects': False, 'headers': headers, 'url': url}
    response = requests.get(**kwargs)
    if response.status_code != 200:
        return(None)
    after = response.json()['data']['after']
    t = [item['data']['title'] for item in response.json()['data']['children']]
    hot_list.extend(t)
    return (recurse(subreddit, hot_list, after))
