#!/usr/bin/python3
""" This is about consuming APIs, GET mehod generate json of every id"""

import json
import requests

if __name__ == "__main__":
    url_id = 'https://jsonplaceholder.typicode.com/users/'
    get_the_ids = requests.get(url_id).json()
    only_ids = []
    for i, mini_dict in enumerate(get_the_ids):
        only_ids.append(get_the_ids[i].get("id"))
    last_dictionary = {}
    for _id in only_ids:
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(_id)
        url_1 = f'https://jsonplaceholder.typicode.com/todos?userId={_id}'
        all_todo = requests.get(url_1)
        user_name = requests.get(url).json()['username']
        inner_list = []

        for task in all_todo.json():
            inner_list.append(
                {"task": task.get("title"),
                 "completed": task.get("completed"),
                 "username": user_name}
            )
        to_update = {_id: inner_list}
        last_dictionary.update(to_update)

    with open("todo_all_employees.json", 'w') as f:
        json.dump(last_dictionary, f)
