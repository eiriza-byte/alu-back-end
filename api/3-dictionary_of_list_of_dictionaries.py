#!/usr/bin/python3
"""Exports the TODO list data of all employees to a JSON file."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    data = {}
    for user in users:
        user_id = user.get("id")
        data[str(user_id)] = [{"username": user.get("username"),
                               "task": t.get("title"),
                               "completed": t.get("completed")}
                              for t in todos if t.get("userId") == user_id]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
