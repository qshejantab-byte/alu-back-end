#!/usr/bin/python3
"""Exports the TODO list of all employees to a JSON file"""
from collections import OrderedDict
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    all_data = OrderedDict()

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []

        for task in todos:
            if task.get("userId") == user_id:
                tasks.append(OrderedDict([("username", username),
                                          ("task", task.get("title")),
                                          ("completed",
                                           task.get("completed"))]))

        all_data[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as file:
        json.dump(all_data, file)
