#!/usr/bin/python3
""" This is about consuming APIs, GET mehod and transfering it to CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    getting = "users?id={}".format(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/{}".format(getting)
    response = requests.get(url)
    list_of_dictionary = response.json()
    us = name = list_of_dictionary[0].get("name")
    user_name = list_of_dictionary[0].get("username")
    getting = "todos?userId={}&completed=true".format(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/{}".format(getting)
    response = requests.get(url)
    dt = list_of_done_tasks = response.json()
    getting = "todos?userId={}".format(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/{}".format(getting)
    response = requests.get(url)
    t = list_of_tasks = response.json()

    with open("USER_ID.csv", "w", newline="") as csv_file:
        thewriter = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in list_of_tasks:
            thewriter.writerow(["{}".format(sys.argv[1]), user_name,
                                task.get("completed"), task.get("title")])
