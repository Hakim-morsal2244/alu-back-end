#!/usr/bin/python3
import requests
import sys

def gather_data(employee_id):
    """Fetches and displays the TODO list progress of a given employee."""
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve data for employee ID {}".format(employee_id))
        return

    tasks = response.json()
    total_tasks = len(tasks)
    completed_tasks = [task['title'] for task in tasks if task['completed']]
    
    if not completed_tasks:
        print("Employee {} has no completed tasks.".format(employee_id))
        return

    employee_name_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_response = requests.get(employee_name_url)

    if employee_response.status_code != 200:
        print("Failed to retrieve employee information for ID {}".format(employee_id))
        return

    employee_name = employee_response.json().get("name", "Unknown Employee")
    
    print("Employee {} is done with tasks({}/{})".format(employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        gather_data(employee_id)
    except ValueError:
        print("Employee ID should be an integer.")
        sys.exit(1)
