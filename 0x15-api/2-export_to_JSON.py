#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
from sys import argv
from urllib import request

if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users/{}"\
                .format({argv[1]})
    with request.urlopen(url_user) as response:
        user = json.loads(response.read().decode())

        url_task = "https://jsonplaceholder.typicode.com/users/{}/todos"\
                   .format({argv[1]})
        with request.urlopen(url_task) as response:
            tasks = json.loads(response.read().decode())
            with open("{}.json".format(user.get("id")), "w") as file:
                data = {}
                list_task = []
                for t in tasks:
                    list_task.append({
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": user.get("username")
                    })
                data[user.get("id")] = list_task
                json.dump(data, file)
