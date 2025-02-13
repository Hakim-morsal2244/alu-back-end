#!/usr/bin/python3
"""
Fetches TODO list progress of an employee using a REST API.
"""
import requests
import sys

if __name__ == "__main__":
    # Check if an argument is provided
    if len(sys.argv) != 2:
        sys.exit()

    user_id = sys.argv[1]

    # Define the API URLs (use .format() instead of f-strings)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    # Fetch data from API
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    # Extract employee name
    employee_name = user.get("name")

    # Filter completed tasks
    completed_tasks = [task["title"] for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    # Print output
    print("Employee {} is done with tasks({}/{}):".format(employee_name, done_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))
