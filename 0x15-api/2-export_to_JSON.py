#!/usr/bin/python3
""" This is about consuming APIs, GET mehod"""

import json
import requests
import sys

if __name__ == "__main__":
    _id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)
    url_1 = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(_id)
    all_todo = requests.get(url_1)
    user_name = requests.get(url).json()['username']
    inner_list = []

    for task in all_todo.json():
        inner_list.append(
            {"task": task.get("title"),
             "completed": task.get("completed"),
             "username": user_name}
        )
    last_dictionary = {_id: inner_list}

    with open("{}.json".format(sys.argv[1]), 'w') as f:
                    json.dump(last_dictionary, f)
