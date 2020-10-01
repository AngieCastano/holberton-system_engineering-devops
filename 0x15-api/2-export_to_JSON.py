#!/usr/bin/python3
""" This is about consuming APIs, GET mehod"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    getting = "users?id={}".format(sys.argv[1])
    response_id = requests.get("{}{}".format(url, getting))
    list_of_dictionary = response_id.json()
    us = user_name = list_of_dictionary[0].get("name")
    to_do_format = "todos?userId={}&completed=true".format(sys.argv[1])
    to_do_response = requests.get("{}{}".format(url, to_do_format))
    dt = list_of_done_tasks = to_do_response.json()
    getting = "todos?userId={}".format(sys.argv[1])
    response = requests.get("{}{}".format(url, getting))
    t = ist_of_tasks = response.json()
    inner_list = []
    for task in list_of_done_tasks:
        inner_list.append(
            {"task": task.get("title"),
             "completed": task.get("completed"),
             "username": user_name}
        )
    last_dictionary = {sys.argv[1]: inner_list}

    with open("{}.json".format(sys.argv[1]), 'w') as f:
                    json.dump(last_dictionary, f)
