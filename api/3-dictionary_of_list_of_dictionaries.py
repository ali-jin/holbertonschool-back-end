#!/usr/bin/python3
"""Records all tasks from all employees"""
import json
import requests
from sys import argv

api_url = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    data_user = requests.get(f"{api_url}/users")
    employee_data = data_user.json()

    dict_all_user = {}
    for user in employee_data:
        user_id = user["id"]

        list_tasks = requests.get(f"{api_url}/todos?userId={user_id}")
        tasks_data = list_tasks.json()

        username = user["username"]

        employee_tasks = []

        for task in tasks_data:
            dict_task = {}
            dict_task["task"] = task["title"]
            dict_task["completed"] = task["completed"]
            dict_task["username"] = username
            employee_tasks.append(dict_task)

        dict_all_user[user_id] = employee_tasks

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dict_all_user, f)
