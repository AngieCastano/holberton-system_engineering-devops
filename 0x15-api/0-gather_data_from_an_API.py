#!/usr/bin/python3
""" This is about consuming APIs, GET mehod"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    getting = "users?id={}".format(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/{}".format(getting)
    response = requests.get(url)
    list_of_dictionary = response.json()
    us = user_name = list_of_dictionary[0].get("name")
    getting = "todos?userId={}&completed=true".format(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/{}".format(getting)
    response = requests.get(url)
    dt = list_of_done_tasks = response.json()
    getting = "todos?userId={}".format(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/{}".format(getting)
    response = requests.get(url)
    t = ist_of_tasks = response.json()
    print("Employee {} is done with tasks({}/{}):".format(us, len(dt), len(t)))
    for task in list_of_done_tasks:
        print("\t {}".format(task.get("title")))
