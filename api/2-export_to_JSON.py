#!/usr/bin/python3
"""Exports the TODO list of an employee to a JSON file"""
from collections import OrderedDict
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos?userId=" + user_id).json()

    username = user.get("username")
    tasks = []

    for task in todos:
        tasks.append(OrderedDict([("task", task.get("title")),
                                  ("completed", task.get("completed")),
                                  ("username", username)]))

    data = {user_id: tasks}

    with open(user_id + ".json", "w") as file:
        json.dump(data, file)
