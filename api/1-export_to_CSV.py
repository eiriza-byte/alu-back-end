#!/usr/bin/python3
"""Exports an employee's TODO list data to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    username = user.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, lineterminator="\n")
        for t in todos:
            writer.writerow([user_id, username, t.get("completed"),
                             t.get("title")])
