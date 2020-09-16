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
    us = user_name = list_of_dictionary[0].get("name")
    getting = "todos?userId={}&completed=true".format(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/{}".format(getting)
    response = requests.get(url)
    dt = list_of_done_tasks = response.json()
    getting = "todos?userId={}".format(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/{}".format(getting)
    response = requests.get(url)
    t = list_of_tasks = response.json()
    print("Employee {} is done with tasks({}/{}):".format(us, len(dt), len(t)))
    for task in list_of_done_tasks:
        print("\t {}".format(task.get("title")))
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open("USER_ID.csv", "w", newline="") as csv_file:
        thewriter = csv.DictWriter(csv_file, fieldnames=fieldnames)
        thewriter.writeheader()
        for task in list_of_tasks:
            thewriter.writerow({"USER_ID": sys.argv[1], "USERNAME": us,
                                "TASK_COMPLETED_STATUS": task.get("completed"),
                                "TASK_TITLE": task.get("title")})
