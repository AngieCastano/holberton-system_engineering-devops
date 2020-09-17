#!/usr/bin/python3
""" This is about consuming reddit API's """

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers """
    number_of_subscribers = 0
    url = "https://www.reddit.com/r/{}/.json".format(subreddit)
    headers = {'User-agent': 'Chrome'}
    response = requests.get(url, headers=headers)
    list_of_dictionary = response.json()
    for key, diction in list_of_dictionary.items():
        if type(diction) == dict:
            for mini_key, mini_value in diction.items():
                if type(mini_value) == list:
                    for mini_item in mini_value:
                        if type(mini_item) == dict:
                            for sub_key, sub_value in mini_item.items():
                                if type(sub_value) == dict:
                                    for m_s_k, m_s_value in sub_value.items():
                                        if m_s_k == "subreddit_subscribers":
                                            number_of_subscribers = m_s_value
    return(number_of_subscribers)
