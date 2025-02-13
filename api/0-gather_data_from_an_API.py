#!/usr/bin/python3
import requests
import sys

def gather_data(user_id):
    # Fetch user details
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    user = user_response.json()

    # Fetch todos for the user
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    # Get completed tasks
    completed_tasks = [task['title'] for task in todos if task['completed']]

    # Display the progress
    print(f"Employee {user['name']} is done with tasks"
          f"({len(completed_tasks)}/{len(todos)}):")

    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    # Check if user provided an argument (employee ID)
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            gather_data(employee_id)
        except ValueError:
            print("Please provide a valid integer for employee ID.")
