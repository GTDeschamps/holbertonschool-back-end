#!/usr/bin/python3
"""creation first API to request Employee ID"""


import csv
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'

def export_tasks_to_csv(USER_ID, USER_NAME, TASKS_TITLE):
    file_name = f"{USER_ID}.csv"
    with open(file_name, mode='w', newline='', encoding='utf-8')as csv_file:
        writer = csv.writer(csv_file)
        for TASK in TASKS_TITLE:
            writer.writerow(['{}, "{}", "{}", "{}'
                            .format(USER_ID, USER_NAME,
                                    TASK["completed"], TASK["title"])])


if __name__ == '__main__':
    """action performed online when the script is run directly"""

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
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
        print(f"Employee {employee_name} is done with tasks
              ({completed_tasks}/{total_tasks}): ")

        """Display titles of completed tasks"""
        completed_task_titles = [todo['title']
                                 for todo in todos_data if todo['completed']]
        for title in completed_task_titles:
            print(f"\t{title}")

        """Export completed tasks to CSV"""
        export_tasks_to_csv(employee_id, employee_name, todos_data)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
