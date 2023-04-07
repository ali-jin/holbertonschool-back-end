#!/usr/bin/python3
"""Records all tasks that are owned by this employee"""
import json
import requests
from sys import argv

api_url = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    data = requests.get(f"{api_url}/users/{argv[1]}")
    employee_data = data.json()

    list_tasks = requests.get(f"{api_url}/todos?userId={argv[1]}")
    tasks_data = list_tasks.json()

    username = employee_data["username"]

    employee_tasks = []

    for task in tasks_data:
        dict_task = {}
        dict_task["task"] = task["title"]
        dict_task["completed"] = task["completed"]
        dict_task["username"] = username
        employee_tasks.append(dict_task)

    dict_user = {}
    dict_user[argv[1]] = employee_tasks

    with open(f"{argv[1]}.json", 'w') as f:
        json.dump(dict_user, f)
