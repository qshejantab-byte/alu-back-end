#!/usr/bin/python3
"""Gets the TODO list progress of an employee from an API"""
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos?userId=" + user_id).json()

    name = user.get("name")
    total = len(todos)
    done = 0
    titles = []

    for task in todos:
        if task.get("completed") is True:
            done = done + 1
            titles.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for title in titles:
        print("\t {}".format(title))
