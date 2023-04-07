#!/usr/bin/python3
"""Records all tasks that are owned by this employee"""
import csv
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
    csvheader = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    for task in tasks_data:
        listing = [f"{argv[1]}", username, task["completed"], task["title"]]
        employee_tasks.append(listing)

    with open(f"{argv[1]}.csv", 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(csvheader)
        writer.writerows(employee_tasks)
