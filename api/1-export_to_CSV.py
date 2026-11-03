#!/usr/bin/python3
"""Exports the TODO list of an employee to a CSV file"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/" + user_id).json()
    todos = requests.get(url + "todos?userId=" + user_id).json()

    username = user.get("username")

    with open(user_id + ".csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username,
                             task.get("completed"), task.get("title")])
