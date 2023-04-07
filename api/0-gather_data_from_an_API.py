#!/usr/bin/python3
"""Returns information about the employee todo list progress
that match the id"""
import requests
from sys import argv

api_url = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    data = requests.get(f"{api_url}/users/{argv[1]}")
    employee_data = data.json()

    list_tasks = requests.get(f"{api_url}/todos?userId={argv[1]}")
    tasks_data = list_tasks.json()

    tasks_complete = [task for task in tasks_data if task["completed"]]

    employee_name = employee_data["name"]
    nb_tasks_done = len(tasks_complete)
    total_task = len(tasks_data)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, nb_tasks_done, total_task
    ))

    for task in tasks_complete:
        print(f"\t {task['title']}")
