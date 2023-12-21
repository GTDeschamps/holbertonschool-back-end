#!/usr/bin/python3
"""creation first API to request Employee ID"""
import json
import requests
from sys import argv


API_URL = "https://jsonplaceholder.typicode.com"

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

        """prepare data to json"""
        json_data = {user_id: []}
        for todo in todos_data:
            task_completed_status = todo['completed']
            task_title = todo['title']
            json_data[user_id].append({"task": task_title,
                                       "completed": task_completed_status,
                                       "username": employee_name})

        """Export tasks to JSON"""
        json_filename = f"{user_id}.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(json_data, json_file)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit(1)
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)
