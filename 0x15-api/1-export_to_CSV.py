#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
from asyncio import tasks
import csv
import json
from sys import argv
from urllib import request


url_user = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
with request.urlopen(url_user) as response:
    user = json.loads(response.read().decode())

    url_task = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    with request.urlopen(url_task) as response:
        tasks = json.loads(response.read().decode())
        with open(f"{user.id}.csv", "wb") as csvfile:
            filewriter = csv.writer(csvfile, delimiter=",", )
            for t in tasks:
                filewriter.writerow([user.get("id"),
                                    user.get("username"),
                                    t.get("completed"),
                                    t.get("title")])
