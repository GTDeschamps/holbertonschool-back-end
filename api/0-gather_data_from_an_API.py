#!/usr/bin/python3
"""creation first API to request Employee ID"""


import requests
from sys import argv


API_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    """action performed online when the script is run directly"""

    employee_id = int(argv[1])
    base_url = 'https://jsonplaceholder.typicode.com/users'
    employee_url = f"{base_url}/{employee_id}"
    todos_url = f"{employee_url}/todos"

    try:
        """Fetch employee information"""
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        user_id = employee_data.get('id')
        employee_name = employee_data.get('name')

        """Fetch TODO list for the employee"""
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        """Calculate progress"""
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])

        """Display progress information"""
        print("Employee {} is done with tasks ({}/{}): "
              .format(employee_name, completed_tasks, total_tasks))

        """Display titles of completed tasks"""
        completed_task_titles = [todo['title']
                                 for todo in todos_data if todo['completed']]
        for title in completed_task_titles:
            print(f"\t{title}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit(1)
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)
