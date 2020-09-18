#!/usr/bin/python3
""" This is about consuming reddit API's , print titles"""

import requests


def top_ten(subreddit):
    """prints the titles of the first10hotpostslisted for a given subreddit"""
    titles = None
    url = "https://www.reddit.com/r/{}/.json?count=10".format(subreddit)
    headers = {'User-agent': 'Chrome'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        list_of_dictionary = response.json()
        for key, diction in list_of_dictionary.items():
            if type(diction) == dict:
                for mini_key, mini_value in diction.items():
                    if type(mini_value) == list:
                        for mini_item in mini_value:
                            if type(mini_item) == dict:
                                for sub_key, sub_value in mini_item.items():
                                    if type(sub_value) == dict:
                                        for m_s_k, m_s_v in sub_value.items():
                                            if m_s_k == "title":
                                                titles = m_s_v
                                                print(titles)
